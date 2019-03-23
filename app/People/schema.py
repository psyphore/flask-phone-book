import graphene
from graphql import GraphQLError
from flask_graphql_auth import (query_jwt_required)

from app import utilities
from .models import Person
from .service import PeopleService
from .graphql_types import Character, PersonType, CreatePerson, UpdatePerson, ProtectedPersonType, Authenticate

service = PeopleService()

def person_resolver(identity):
    person = service.fetch(id=identity)[0]
    if person is None:
        raise GraphQLError(
            f'"{identity}" has not been found in our people list.')

    return PersonType(**Person.wrap(person).as_dict())

class PeopleQuery(graphene.ObjectType):   
    '''People Query, 
        fetch person entries matching to provided criteria
    '''

    person = graphene.Field(PersonType, id=graphene.NonNull(graphene.ID))
    people = graphene.List(lambda: PersonType, limit=graphene.Int(10))
    me = graphene.Field(lambda: ProtectedPersonType)

    def resolve_person(self, info, id):
        return person_resolver(id)

    def resolve_people(self, info, **args):
        l = args.get("limit")
        people = service.fetch_all(limit=l)
        if people is None:
            raise GraphQLError('we did not find any people, please populate first.')

        return [PersonType(**Person.wrap(p).as_dict()) for p in people]

    def resolve_me(self, info):
        decoded = utilities.get_user_info(info.context.headers.get('Authorization'))
        if decoded is not None:
            person = service.fetch_protected(decoded)
            if person is None:
                raise GraphQLError('User not authorized.')
            ppt = ProtectedPersonType(**person)
            return ppt
        return None


class PeopleMutations(graphene.ObjectType):
    '''People Mutations, 
        create new person object or 
        update an existing person object
    '''
    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()
    auth_person = Authenticate.Field()


schema = graphene.Schema(query=PeopleQuery, mutation=PeopleMutations, auto_camelcase=True)
