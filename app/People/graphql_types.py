import graphene

from .models import Person
from .service import PeopleService

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
    
class TeamType(graphene.ObjectType):
    '''Team Type, represents a GraphQL version of a person's team member or manager entity'''

    class Meta:
        interfaces=(Character,)

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
        interfaces=(Character,)

    manager = Character
    products = graphene.List(lambda: ProductType)
    location = graphene.List(lambda: graphene.String)

    def resolve_team(self, info, **args):
        # return [StoreSchema(**store.as_dict()) for store in self.customer.stores]
        pass

    def resolve_manager(self, info, **args):
        # return [ReceiptSchema(**receipt.as_dict()) for receipt in self.customer.receipts]
        pass

    def resolve_products(self, info, **args):
        # return [ProductSchema(**product.as_dict()) for product in self.customer.products]
        pass
    
    def resolve_location(self, info, **args):
        pass

class SearchResultType(graphene.ObjectType):
    '''Search Result, containing a count of items contained in the items member'''

    count=graphene.Int(0)
    items=graphene.List(lambda: PersonType)
    
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
