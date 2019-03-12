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

    def fetch(self, id, name):
        '''Fetch a single building with matching id'''

        try:
            query = None
            if id is not None:
                query = get_building_by_id_or_name_query(id=str(id), name=None)

            if name is not None:
                query = get_building_by_id_or_name_query(
                    id=None, name=str(name))

            if id is not None and name is not None:
                query = get_building_by_id_or_name_query(
                    id=str(id), name=str(name))

            if id is None and name is None:
                return None

            value = GraphContext().exec_cypher(query)
            return value
        except Exception as ex:
            print(f'bs_f X exception: {ex}')
            return None

    def fetch_all(self, limit=100):
        '''Fetch all building nodes stored ordered by name limited (default=100)'''

        try:
            response = GraphContext().exec_cypher(
                get_buildings_query(skip=str(0), first=str(limit)))
            return response
        except Exception as ex:
            print(f'bs_fa X exception: {ex}')
            return []

    def fetch_people(self, building):
        '''Fetch all people who share the same current building'''

        try:
            items = [item for item in building.team.node.get("people")]
            if items is not None:
                return items
            return []
        except Exception as ex:
            print(f'bs_fp X exception: {ex}')
            return []
