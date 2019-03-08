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
        return [PersonType(**member.as_dict()) for member in service.fetch_team(context=self)]

    def resolve_manager(self, info, **args):
        pass
        # person = args.get("")
        # return [PersonType(**manager.as_dict()) for manager in service.fetch_manager(context=self)]

    def resolve_products(self, info, **args):
        # return [ProductSchema(**product.as_dict()) for product in self.customer.products]
        pass

    def resolve_location(self, info, **args):
        pass


class SearchType(graphene.InputObjectType):
    '''Search, 
        :query, your search phrase
        :first, how many are you fetching in a set
        :offest, number to offset by a set
    '''
    class Arguments:
        query = graphene.String(required=True)
        first = graphene.Int(10)
        offset = graphene.Int(0)

class SearchResultType(graphene.ObjectType):
    '''Search Result, containing a count of items contained in the items member'''

    count = graphene.Int(0)
    data = graphene.List(lambda: PersonType)


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
