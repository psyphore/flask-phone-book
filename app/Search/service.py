import maya
from py2neo.ogm import Node

from app.graph_context import GraphContext

from .cypher_queries import (filter_person_query_3)


class SearchService():
    '''
    This Search Service performs searches against person object
    '''

    def filter(self, query, limit=10, skip=0):
        '''Filter will fuzzy match the query on firstname and limit the result to what has been passed in as limit (default=10)'''

        try:
            matched = GraphContext().exec_cypher(query=filter_person_query_3(name=query, skip=str(skip), first=str(limit)))
            if matched is not None:
                return [Node.cast(node.values()) for node in matched]
            return []
        except Exception as ex:
            print(f'x exception: {ex}')
            return []
