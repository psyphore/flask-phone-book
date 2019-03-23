import graphene
from flask_graphql_auth import (AuthInfoField, query_jwt_required, mutation_jwt_refresh_token_required, mutation_jwt_required)
from app.utilities import (create_tokens)

from .models import Person
from .service import PeopleService
import app.Building.graphql_types
import app.Product.graphql_types
import app.People.graphql_types
from app.Search.service import SearchService

service = PeopleService()


class Character(graphene.Interface):
    id = graphene.ID(required=True)

    title = graphene.String(required=True)
    firstname = graphene.String(required=True)
    lastname = graphene.String(required=True)
    bio = graphene.String()
    knownAs = graphene.String()
    avatar = graphene.String()
    mobile = graphene.String()
    email = graphene.String(required=True)

    line = graphene.List(lambda: Character)
    team = graphene.List(lambda: Character)
    manager = graphene.Field(lambda: Character)

class PersonType(graphene.ObjectType):
    '''Person Type, represents a GraphQL version of a person entity'''

    class Meta:
        interfaces = (Character,)

    products = graphene.List(lambda: app.Product.graphql_types.ProductType)
    location = graphene.List(lambda: app.Building.graphql_types.BuildingType)

    def resolve_team(self, info, **args):
        return [PersonType(**Person.wrap(member).as_dict()) for member in service.fetch_team(person=self)]

    def resolve_line(self, info, **args):
        return [PersonType(**Person.wrap(member).as_dict()) for member in service.fetch_line(person=self)]

    def resolve_manager(self, info, **args):
        manager = service.fetch_manager(person=self)
        if manager is not None:
            return PersonType(**Person.wrap(manager).as_dict())
        return None

    def resolve_products(self, info, **args):
        pass

    def resolve_location(self, info, **args):
        pass

class ProtectedPersonType(graphene.ObjectType):
    person = graphene.Field(lambda: Person)
    leave_items = graphene.List(lambda: graphene.String)
    salary_level = graphene.Int()
    next_of_keen = graphene.String()
    birth_date = graphene.Date()
    employment_anniversary = graphene.Date()
    authorization_key = graphene.String()

class AuthorizationType(graphene.ObjectType):
    access_token = graphene.String()
    refresh_token = graphene.String()

class CreatePerson(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        firstname = graphene.String(required=True)
        lastname = graphene.String(required=True)
        bio = graphene.String()
        knownAs = graphene.String()
        avatar = graphene.String()
        mobile = graphene.String()
        email = graphene.String(required=True)

    success = graphene.Boolean()
    person = graphene.Field(lambda: PersonType)

    @mutation_jwt_required
    def mutate(self, info, **kwargs):
        person = Person(**kwargs)
        person.save()

        return CreatePerson(person=person, success=True)

class UpdatePerson(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

        title = graphene.String(required=True)
        firstname = graphene.String(required=True)
        lastname = graphene.String(required=True)
        bio = graphene.String()
        knownAs = graphene.String()
        avatar = graphene.String()
        mobile = graphene.String()
        email = graphene.String(required=True)

    success = graphene.Boolean()
    person = graphene.Field(lambda: PersonType)

    @mutation_jwt_required
    def mutate(self, info, **kwargs):
        person = Person(**kwargs)
        person.save()

        return UpdatePerson(person=person, success=True)

class Authenticate(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        
    success = graphene.Boolean()
    authorization = graphene.Field(lambda: AuthorizationType)

    def mutate(self, info, **kwargs):
        criteria = kwargs.get('email')
        search_svc = SearchService()

        matched = [PersonType(**Person.wrap(m).as_dict()) for m in search_svc.filter(query=criteria,limit=1,skip=0)]
        
        if matched is not None and len(matched) > 0:
            tokens = create_tokens(identity=matched[0].id)
            payload = AuthorizationType(**tokens)
            return Authenticate(authorization=payload, success=True)
        
        return Authenticate(authorization=None, success=False)
