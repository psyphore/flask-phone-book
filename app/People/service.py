from graphql import GraphQLError
from app.graph_context import GraphContext

from .models import Person


class PeopleService(Person):
    '''
    This People Service houses all the actions can be performed against the person object
    '''

    def __init__(self, *args, **kwargs):
        self.graph = GraphContext.get_instance()

    def fetch(self):
        customer = self.select(self.graph, self.email).first()
        if customer is None:
            raise GraphQLError(
                f'"{self.email}" has not been found in our customers list.')

        return customer

    # def __verify_products(self, products):
    #     _total_amount = 0
    #     for product in products:
    #         _product = Product(name=product.get('name')).fetch()
    #         if _product is None:
    #             raise GraphQLError(
    #                 f'"{product.name}" has not been found in our products list.')

    #         _total_amount += product['price'] * product['amount']
    #         product['product'] = _product
    #     return products, _total_amount

    # def __verify_receipt(self, receipt):
    #     customer_properties = f":Customer {{email: '{self.email}'}}"
    #     receipt_properties = f":Receipt {{timestamp: '{receipt.timestamp}', total_amount:{receipt.total_amount}}}"
    #     existing_receipts = self.graph.run(
    #         f"MATCH ({customer_properties})-[relation:HAS]-({receipt_properties}) RETURN relation").data()

    #     if existing_receipts:
    #         raise GraphQLError(
    #             "The receipt you're trying to submit already exists.")

    # def __link_products(self, products, total_amount, timestamp):
    #     receipt = Receipt(total_amount=total_amount,
    #                       timestamp=timestamp, validate=True)
    #     self.__verify_receipt(receipt)

    #     for item in products:
    #         receipt.products.add(item.pop('product'), properties=item)

    #     return receipt

    # def __verify_store(self, store):
    #     _store = Store(**store).fetch_by_name_and_address()
    #     if _store is None:
    #         raise GraphQLError(
    #             f"The store \"{store['name']}\" does not exist in our stores list.")

    #     return _store

    # def __add_links(self, store, receipt):
    #     store.receipts.add(receipt)
    #     self.stores.add(store)
    #     self.receipts.add(receipt)

    # def submit_receipt(self, products, timestamp, store):
    #     self.__add_links(
    #         self.__verify_store(store),
    #         self.__link_products(*self.__verify_products(products), timestamp)
    #     )

    #     self.save()
