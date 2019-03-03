import graphene
from graphql import GraphQLError

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

    def resolve_team(self, info):
        # return [StoreSchema(**store.as_dict()) for store in self.customer.stores]
        pass

    def resolve_manager(self, info):
        # return [ReceiptSchema(**receipt.as_dict()) for receipt in self.customer.receipts]
        pass

    def resolve_products(self, info):
        # return [ProductSchema(**product.as_dict()) for product in self.customer.products]
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
