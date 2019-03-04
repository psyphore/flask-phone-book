import graphene
from graphql import GraphQLError

from .models import Person
from .service import PeopleService
from .graphql_types import Character, TeamType, ProductType, PersonType, SearchResultType, CreatePerson

class PeopleQuery(graphene.ObjectType):   
    '''People Query, fetch person entries matching to provided criteria'''

    person = graphene.Field(PersonType, id=graphene.NonNull(graphene.ID))
    people = graphene.List(lambda: PersonType, limit=graphene.Int(10))
    search = graphene.Field(SearchResultType, query=graphene.NonNull(graphene.String), limit=graphene.Int(10))

    def resolve_person(self, info, **args):
        identity = args.get("id")
        service = PeopleService()
        person = service.fetch(id=identity)
        if person is None:
            raise GraphQLError(
                f'"{email}" has not been found in our customers list.')

        return PersonType(**person.as_dict())

    def resolve_people(self, info, **args):
        l = args.get("limit")
        service = PeopleService()
        people = service.fetch_all(limit=l)
        if people is None:
            raise GraphQLError('we did not find any people, please populate first.')

        return [PersonType(**person.as_dict()) for person in people]

    def resolve_search(self, info, **args):
        q, l = args.get("query"), args.get("limit")
        service = PeopleService()
        result = service.filter(query=q,limit=l)

        if result is None:
            raise GraphQLError(f'"{q}" has not been found in our customers list.')

        sr = SearchResultType()
        sr.count = len(result)
        sr.items = [PersonType(**person.as_dict()) for person in result]

        return sr


class PeopleMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()
    # submit_receipt = SubmitReceipt.Field()


schema = graphene.Schema(query=PeopleQuery, mutation=None, auto_camelcase=True, types=[PersonType, SearchResultType])
