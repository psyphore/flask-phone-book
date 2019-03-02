import graphene

from .models import Person
from .service import PeopleService


class PersonType(graphene.ObjectType):
    title = graphene.String()
    firstname = graphene.String()
    lastname = graphene.String()
    mobile_number = graphene.String()
    email_address = graphene.String()
    date_updated = graphene.DateTime()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # svc = PeopleService()
        # self.person = svc.fetch(email=self.email_address)

    def resolve_team(self, info):
        # return [StoreSchema(**store.as_dict()) for store in self.customer.stores]
        pass

    def resolve_manager(self, info):
        # return [ReceiptSchema(**receipt.as_dict()) for receipt in self.customer.receipts]
        pass

    def resolve_products(self, info):
        # return [ProductSchema(**product.as_dict()) for product in self.customer.products]
        pass

class PeopleType(graphene.ObjectType):
    people = graphene.List(PersonType)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # svc = PeopleService()
        # self.people = svc.fetch_all()

class SearchResult(graphene.Union):
    class Meta:
        types = (PersonType, PeopleType)

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
    person = graphene.Field(lambda: PersonType, email=graphene.String())
    people = graphene.List(lambda: PersonType)
    search = graphene.List(lambda: SearchResult, q=graphene.String())
    
    def __init__(self):
        self.ps = PeopleService()

    def resolve_person(self, info, **args):
        email = args.get("email")
        person = self.ps.fetch(email=email)
        return PersonType(**person.as_dict())

    def resolve_people(self, info):
        people = self.ps.fetch_all()
        return [PersonType(**person.as_dict()) for person in people]

    def resolve_search(self, info, **args):
        q = args.get("q")  # Search query

        result = self.ps.filter(query=q)

        return result

        # # Get queries
        # bookdata_query = BookData.get_query(info)
        # author_query = Author.get_query(info)

        # # Query Books
        # books = bookdata_query.filter((BookModel.title.contains(q)) |
        #                               (BookModel.isbn.contains(q)) |
        #                               (BookModel.authors.any(AuthorModel.name.contains(q)))).all()

        # # Query Authors
        # authors = author_query.filter(AuthorModel.name.contains(q)).all()

        # return authors + books  # Combine lists


class PeopleMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()
    # submit_receipt = SubmitReceipt.Field()


schema = graphene.Schema(query=PeopleQuery, mutation=None, auto_camelcase=True, types=[PersonType, PeopleType, SearchResult])
