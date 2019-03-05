import graphene
from graphql import GraphQLError

from .models import Person
from .service import PeopleService
from .graphql_types import Character, TeamType, ProductType, PersonType, SearchResultType, CreatePerson

service = PeopleService()

class PeopleQuery(graphene.ObjectType):   
    '''People Query, fetch person entries matching to provided criteria'''

    person = graphene.Field(PersonType, id=graphene.NonNull(graphene.ID))
    people = graphene.List(lambda: PersonType, limit=graphene.Int(10))
    search = graphene.Field(SearchResultType, query=graphene.NonNull(graphene.String), limit=graphene.Int(10))

    def resolve_person(self, info, **args):
        identity = args.get("id")
        person = service.fetch(id=identity)
        if person is None:
            raise GraphQLError(
                f'"{identity}" has not been found in our customers list.')

        return PersonType(**Person.wrap(person).as_dict())

    def resolve_people(self, info, **args):
        l = args.get("limit")
        people = service.fetch_all(limit=l)
        if people is None:
            raise GraphQLError('we did not find any people, please populate first.')

        return [PersonType(**Person.wrap(p).as_dict()) for p in people]

    def resolve_search(self, info, **args):
        q, l = args.get("query"), args.get("limit")
        result = service.filter(query=q,limit=l)

        if result is None:
            raise GraphQLError(f'"{q}" has not been found in our customers list.')

        sr = SearchResultType()
        sr.count = len(result)
        sr.items = [PersonType(**Person.wrap(r).as_dict()) for r in result]

        return sr


class PeopleMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()
    # submit_receipt = SubmitReceipt.Field()


schema = graphene.Schema(query=PeopleQuery, mutation=None, auto_camelcase=True, types=[PersonType, SearchResultType])
