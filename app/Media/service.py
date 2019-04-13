import maya
from py2neo.ogm import Node

from app.graph_context import GraphContext

from .models import Media
from .cypher_queries import (fetch_media_query, save_media_query)


class MediaService():
    '''
    This Media Service houses all the actions can be performed against the building object
    '''

    def __init__(self):
        self.media = Media()

    def fetch(self, id, height, width):
        '''Fetch a single media item with matching id'''

        try:
            if id is None:
                return None

            value = GraphContext().exec_cypher(fetch_media_query(id=str(id)))
            # might want to manipulate the height and width here
            return value
        except Exception as ex:
            print(f'ms_f X exception: {ex}')
            return None

    def save_media(self, media):
        '''Save media'''

        try:
            items = [item for item in building.team.node.get("people")]
            if items is not None:
                return items
            return []
        except Exception as ex:
            print(f'ms_fp X exception: {ex}')
            return []
