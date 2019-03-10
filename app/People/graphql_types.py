import graphene

from .models import Person
from .service import PeopleService

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


class TeamType(graphene.ObjectType):
    '''Team Type, represents a GraphQL version of a person's team member or manager entity'''

    class Meta:
        interfaces = (Character,)

    mobile_number = graphene.String()
    email_address = graphene.String()
    date_updated = graphene.DateTime()


class ProductType(graphene.ObjectType):
    id = graphene.ID()

    name = graphene.String()
    description = graphene.String()
    date_updated = graphene.DateTime()


class PersonType(graphene.ObjectType):
    '''Person Type, represents a GraphQL version of a person entity'''

    class Meta:
        interfaces = (Character,)

    products = graphene.List(lambda: ProductType)
    location = graphene.List(lambda: graphene.String)

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


class CreatePerson(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        firstname = graphene.String(required=True)
        lastname = graphene.String(required=True)
        mobile_number = graphene.String(required=True)
        email_address = graphene.String(required=True)

    success = graphene.Boolean()
    person = graphene.Field(lambda: PersonType)

    def mutate(self, info, **kwargs):
        person = Person(**kwargs)
        person.save()

        return CreatePerson(person=person, success=True)
