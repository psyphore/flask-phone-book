import maya
from py2neo.ogm import Node

from app.graph_context import GraphContext

from .models import Building
from .cypher_queries import get_buildings_query, get_building_by_id_or_name_query


class BuildingService():
    '''
    This Building Service houses all the actions can be performed against the building object
    '''

    building = None

    def __init__(self):
        self.building = Building()

    def fetch(self, id):
        '''Fetch a single building with matching id'''

        try:
            value = GraphContext().exec_cypher(
                get_building_by_id_or_name_query(id=id, name=None))
            return value
        except Exception as ex:
            print(f'x exception: {ex}')
            return None

    def fetch_all(self, limit=100):
        '''Fetch all building nodes stored ordered by name limited (default=100)'''

        try:
            response = GraphContext().exec_cypher(get_buildings_query(skip=0, first=limit))
            return response
        except Exception as ex:
            print(f'x exception: {ex}')
            return []

    def fetch_people(self, person):
        '''Fetch all people who share the same current building'''

        try:
            items = [item for item in person.team.node.get("people")]
            if items is not None:
                return items
            return []
        except Exception as ex:
            print(f'ps_ft X exception: {ex}')
            return []
