from py2neo.ogm import Node

from app.graph_context import GraphContext

from .models import Media
from .cypher_queries import (fetch_media_query, save_media_query)
from .utilities import (another_image_processor_2, scale_image_2, generator, grey_out_image_2)

class MediaService():
    '''
    This Media Service houses all the actions can be performed against the building object
    '''

    def __init__(self):
        self.media = Media()

    def fetch(self, id):
        '''Fetch a single media item with matching id'''

        try:
            if id is None:
                return None

            return [Node.cast(node.values()) for node in GraphContext().exec_cypher(fetch_media_query(id=str(id)))]
        except Exception as ex:
            print(f'ms_f X exception: {ex}')
            return None

    def fetch_with_dimensions(self, id, height, width, grey_out=False):
        '''Fetch a single media item with matching id
            
        '''

        try:
            if id is None:
                return None

            media = self.fetch(id)
            if len(media) > 0:
                item = Media.wrap(media[0]).as_dict()
                image_binary = another_image_processor_2(item['data'])
                value = scale_image_2(image_binary, height, width)
                
                if grey_out:
                    value = grey_out_image_2(value)

                return {
                    'data': generator(value),
                    'mime': item['mime']
                }
            return None
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
