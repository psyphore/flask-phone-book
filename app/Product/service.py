import maya
from py2neo.ogm import Node

from app.graph_context import GraphContext

from .models import Person
from .cypher_queries import get_person_by_id_query


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
            value = GraphContext().exec_cypher(get_person_by_id_query(id), id=id)
            print(f'{value}')
            return value
            # matcher = GraphContext().get_node_matcher
            # return matcher.match('Person', id=id).first()
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

    def fetch_team(self, person):
        '''Fetch all people who share the same manager as current person'''

        try:
            items = [item for item in person.team.node.get("team")]
            if items is not None:
                return items
            return []
        except Exception as ex:
            print(f'ps_ft X exception: {ex}')
            return []

    def fetch_line(self, person):
        '''Fetch all people who report the current person'''

        try:
            items = [item for item in person.team.node.get("line")]
            if items is not None:
                return items
            return []
        except Exception as ex:
            print(f'ps_fl X exception: {ex}')
            return []

    def fetch_manager(self, person):
        '''Fetch all people who share the same manager as current person'''

        try:
            item = person.manager.node.get("manager")
            if item is not None:
                return item
            return None
        except Exception as ex:
            print(f'ps_fm X exception: {ex}')
            return []

    def fetch_x(self, query, params):
        '''
        Fetch X, use cyper queries
        '''

        try:
            response = GraphContext().graph_cypher_exec(query, **params)
            # [r for r in response]
        except Exception as ex:
            print(f'x exception: {ex}')
            return []
