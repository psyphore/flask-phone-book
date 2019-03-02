import graphene
from graphql import GraphQLError

from .models import Person
from .service import PeopleService


class TeamType(graphene.ObjectType):
    id = graphene.ID()

    title = graphene.String()
    firstname = graphene.String()
    lastname = graphene.String()
    mobile_number = graphene.String()
    email_address = graphene.String()
    date_updated = graphene.DateTime()

class ProductType(graphene.ObjectType):
    id = graphene.ID()

    name = graphene.String()
    description = graphene.String()
    date_updated = graphene.DateTime()

class PersonType(graphene.ObjectType):

    id = graphene.ID()

    title = graphene.String()
    firstname = graphene.String()
    lastname = graphene.String()
    mobile_number = graphene.String()
    email_address = graphene.String()
    date_updated = graphene.DateTime()

    team = graphene.List(TeamType)
    manager = graphene.String()
    products = graphene.List(ProductType)
    location = graphene.String()

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
    count=graphene.Int()
    items=graphene.List(PersonType)
    
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
    person = graphene.Field(PersonType, email=graphene.String())
    people = graphene.List(PersonType)
    search = graphene.Field(SearchResultType, q=graphene.String())

    def resolve_person(self, info, **args):
        email = args.get("email")
        service = PeopleService()
        person = service.fetch(email=email)
        print(f'> fetched {person} ')
        if person is None:
            raise GraphQLError(
                f'"{email}" has not been found in our customers list.')

        return PersonType(**person.as_dict())

    def resolve_people(self, info):
        service = PeopleService()
        people = service.fetch_all()
        print(f'> fetched {people} ')
        if people is None:
            raise GraphQLError(
                f'we did not find any people, please populate first.')

        return [PersonType(**person.as_dict()) for person in people]

    def resolve_search(self, info, **args):
        q = args.get("q") 
        service = PeopleService()
        result = service.filter(query=q)
        print(f'> fetched {result} ')
        if result is None:
            raise GraphQLError(
                f'"{q}" has not been found in our customers list.')

        return SearchResultType(**result)


class PeopleMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()
    # submit_receipt = SubmitReceipt.Field()


schema = graphene.Schema(query=PeopleQuery, mutation=None, auto_camelcase=True, types=[PersonType, SearchResultType])
