import graphene
from graphql import GraphQLError

from .models import Person
from .service import PeopleService
from .graphql_types import Character, TeamType, ProductType, PersonType, CreatePerson
from app.Search.graphql_types import SearchResultType

service = PeopleService()

class PeopleQuery(graphene.ObjectType):   
    '''People Query, fetch person entries matching to provided criteria'''

    person = graphene.Field(PersonType, id=graphene.NonNull(graphene.ID))
    people = graphene.List(lambda: PersonType, limit=graphene.Int(10))
    me = graphene.Field(PersonType, id=graphene.NonNull(graphene.ID))

    def resolve_person(self, info, **args):
        identity = args.get("id")
        person = service.fetch(id=identity)
        if person is None:
            raise GraphQLError(
                f'"{identity}" has not been found in our people list.')

        return PersonType(**Person.wrap(person).as_dict())

    def resolve_people(self, info, **args):
        l = args.get("limit")
        people = service.fetch_all(limit=l)
        if people is None:
            raise GraphQLError('we did not find any people, please populate first.')

        return [PersonType(**Person.wrap(p).as_dict()) for p in people]

    def resolve_me(self, info, **args):
        identity = args.get("id")
        person = service.fetch(id=identity)
        if person is None:
            raise GraphQLError(
                f'"{identity}" has not been found in our people list.')

        return PersonType(**Person.wrap(person).as_dict())


class PeopleMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()
    # submit_receipt = SubmitReceipt.Field()


schema = graphene.Schema(query=PeopleQuery, mutation=None, auto_camelcase=True, types=[PersonType, SearchResultType])
