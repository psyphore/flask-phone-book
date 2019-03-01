import graphene

from .models import Person
from .service import PeopleService


class PersonSchema(graphene.ObjectType):
    title = graphene.String()
    firstname = graphene.String()
    lastname = graphene.String()
    mobile_number = graphene.String()
    email_address = graphene.String()
    date_updated = graphene.DateTime()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        svc = PeopleService()
        self.customer = svc(email=self.email).fetch()

    def resolve_team(self, info):
        # return [StoreSchema(**store.as_dict()) for store in self.customer.stores]
        pass

    def resolve_manager(self, info):
        # return [ReceiptSchema(**receipt.as_dict()) for receipt in self.customer.receipts]
        pass

    def resolve_products(self, info):
        # return [ProductSchema(**product.as_dict()) for product in self.customer.products]
        pass


class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    success = graphene.Boolean()
    customer = graphene.Field(lambda: CustomerSchema)

    def mutate(self, info, **kwargs):
        customer = Customer(**kwargs)
        customer.save()

        return CreateCustomer(customer=customer, success=True)


class Query(graphene.ObjectType):
    customer = graphene.Field(lambda: CustomerSchema, email=graphene.String())
    stores = graphene.List(lambda: StoreSchema)
    products = graphene.List(lambda: ProductSchema)

    def resolve_customer(self, info, email):
        customer = Customer(email=email).fetch()
        return CustomerSchema(**customer.as_dict())

    def resolve_stores(self, info):
        return [StoreSchema(**store.as_dict()) for store in Store().all]

    def resolve_products(self, info):
        return [ProductSchema(**product.as_dict()) for product in Product().all]


class Mutations(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    submit_receipt = SubmitReceipt.Field()


schema = graphene.Schema(query=Query, mutation=Mutations, auto_camelcase=True)
