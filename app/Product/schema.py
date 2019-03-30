import graphene
from graphql import GraphQLError

from .models import Product
from .service import ProductService
from .graphql_types import ProductType

class ProductQuery(graphene.ObjectType):   
    '''
    Product Query, 
    fetch product entries matching to provided criteria
    '''

    product = graphene.Field(ProductType, id=graphene.NonNull(graphene.ID))
    products = graphene.List(lambda: ProductType, limit=graphene.Int(10))

    def __init__(self):
        self.service = ProductService()
    
    def resolve_product(self, info, **args):
        identity = args.get("id")
        product = self.service.fetch(id=identity)
        if product is None:
            raise GraphQLError(
                f'"{identity}" has not been found in our people list.')

        return ProductType(**Product.wrap(product).as_dict())

    def resolve_products(self, info, **args):
        l = args.get("limit")
        products = self.service.fetch_all(limit=l)
        if products is None:
            raise GraphQLError('we did not find any people, please populate first.')

        return [ProductType(**Product.wrap(p).as_dict()) for p in products]

schema = graphene.Schema(query=ProductQuery, auto_camelcase=True)
