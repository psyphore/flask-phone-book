import maya
from py2neo.ogm import Node

from app.graph_context import GraphContext

from .cypher_queries import get_product_by_id_query


class ProductService():
    '''
    This Product Service houses all the actions can be performed against the product object
    '''

    def fetch(self, id):
        '''Fetch a single product with matching id'''

        try:
            value = GraphContext().exec_cypher(get_product_by_id_query(id), id=id)
            print(f'{value}')
            return value
        except Exception as ex:
            print(f'X exception: {ex}')
            return None

    def fetch_all(self, limit=100):
        '''Fetch all Product nodes stored ordered by firstname limited (default=100)'''

        try:
            matcher = GraphContext().get_node_matcher
            response = list(matcher.match('Product').order_by(
                "_.name").limit(limit))
            return response
        except Exception as ex:
            print(f'X exception: {ex}')
            return []
