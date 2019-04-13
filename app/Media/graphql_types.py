import graphene

from .models import Media
from .service import MediaService

service = MediaService()


class MediaType(graphene.ObjectType):
    '''
    Media Type, 
        represents a GraphQL version of a media entity
    '''

    id = graphene.ID(required=True)

    mime = graphene.String(required=True)
    data = graphene.String(required=True)
