import maya

from app.graph_context import GraphContext

from .models import Person


class PeopleService():
    '''
    This People Service houses all the actions can be performed against the person object
    '''

    person = None

    def __init__(self):
        self.person = Person()

    def fetch(self, id):
        '''Fetch a single person with matching id'''

        try:
            matcher = GraphContext().get_node_matcher
            return matcher.match('Person', id=id).first()
        except Exception as ex:
            print(f'x exception: {ex}')
            return None

    def fetch_all(self, limit=100):
        '''Fetch all Person nodes stored ordered by firstname limited (default=100)'''

        try:
            matcher = GraphContext().get_node_matcher
            response = list(matcher.match('Person').order_by(
                "_.firstname").limit(limit))
            return response
        except Exception as ex:
            print(f'x exception: {ex}')
            return []

    def filter(self, query, limit=100):
        '''Filter will fuzzy match the query on firstname and limit the result to what has been passed in as limit (default=100)'''

        try:
            matcher = GraphContext().get_node_matcher
            response = list(matcher.match('Person').where(f"_.firstname =~ '{query}.*'").order_by("_.firstname").limit(limit))
            if len(response) > 0:
                return response
            return []
        except Exception as ex:
            print(f'x exception: {ex}')
            return []

    def fetch_team(self, context):
        '''Fetch all people who share the same manager as current person'''

        try:
            person = self.fetch(id=context.id)
            print(f'> person: {person}')
            r_matcher = GraphContext().get_relationship_matcher
            response = list(r_matcher.match(r_type='MANAGES'))
            print(f'> response: {help(response[0].nodes)} = {response[0].nodes}')
            if len(response) > 0:
                return [r.nodes for r in response]
            return []
        except Exception as ex:
            print(f'x exception: {ex}')
            return []

    def fetch_manager(self, context):
        '''Fetch all people who share the same manager as current person'''

        try:
            matcher = GraphContext().get_relationship_matcher
            response = list(matcher.match('Person', 'MANAGES')
            .order_by("_.firstname"))
            if len(response) > 0:
                return response[0]
            return []
        except Exception as ex:
            print(f'x exception: {ex}')
            return []
