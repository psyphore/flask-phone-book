import graphene
from graphql import GraphQLError
from flask_graphql_auth import (get_jwt_identity,get_raw_jwt,query_jwt_required)

from .models import Person
from .service import PeopleService
from .graphql_types import Character, ProductType, PersonType, CreatePerson, UpdatePerson
from app.Search.graphql_types import SearchResultType

service = PeopleService()

class PeopleQuery(graphene.ObjectType):   
    '''People Query, 
        fetch person entries matching to provided criteria
    '''

    person = graphene.Field(PersonType, id=graphene.NonNull(graphene.ID))
    people = graphene.List(lambda: PersonType, limit=graphene.Int(10))
    me = graphene.Field(PersonType)

    def resolve_person(self, info, id):
        identity = id
        person = service.fetch(id=identity)[0]
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

    @query_jwt_required
    def resolve_me2(self, info, **args):
        print(f's_rm > self: {self} \n info: {info} \n args: {args}')
        identity = args.get("id")
        person = service.fetch(id=identity)
        if person is None:
            raise GraphQLError(
                f'"{identity}" has not been found in our people list.')

        return PersonType(**Person.wrap(person).as_dict())

    # @query_jwt_required
    def resolve_me(self, info):
        print(f's_rm > self: {self} \n info: {info} \n options: {dir(info)}')
        pass
        # user = info.context.user
        # if user.is_anonymous:
        #     raise GraphQLError('Not logged in!')

        # return user


class PeopleMutations(graphene.ObjectType):
    '''People Mutations, 
        create new person object or 
        update an existing person object
    '''
    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()


schema = graphene.Schema(query=PeopleQuery, mutation=PeopleMutations, auto_camelcase=True)
