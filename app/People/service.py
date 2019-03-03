import maya
from py2neo import NodeMatcher


from app.graph_context import GraphContext

from .models import Person

class PeopleService():
    '''
    This People Service houses all the actions can be performed against the person object
    '''
    
    graph=None
    person=None
    matcher=None

    def __init__(self):
        # context = GraphContext()
        # self.graph = context.get_instance()
        self.graph = GraphContext().get_instance
        self.person = Person()
        self.matcher = NodeMatcher(graph=self.graph)

    
    def fetch(self, id):
        '''Fetch a single person with matching id'''

        try:
            matcher = NodeMatcher(graph=GraphContext().get_instance)
            return Person.wrap(matcher.match('Person',id=id).first())
        except Exception as ex:
            print(f'x exception: {ex}')
            return None

    def fetch_all(self, limit=100):
        '''Fetch all Person nodes stored ordered by firstname limited (default=100)'''

        try:
            matcher = NodeMatcher(graph=GraphContext().get_instance)
            response = list(matcher.match('Person').order_by("_.firstname").limit(limit))
            return [Person.wrap(r) for r in response]
        except Exception as ex:
            print(f'x exception: {ex}')
            return []

    def filter(self, query, limit=100):
        '''Filter will fuzzy match the query on firstname and limit the result to what has been passed in as limit (default=100)'''

        try:
            matcher = NodeMatcher(graph=GraphContext().get_instance)
            response = list(matcher.match('Person').where(f"_.firstname =~ '{query}.*'").order_by("_.firstname").limit(limit))
            if len(response) > 0:
                parsed = [Person.wrap(r) for r in response]
                return parsed
            return []
        except Exception as ex:
            print(f'x exception: {ex}')
            return []
