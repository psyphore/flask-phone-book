import graphene
from graphql import GraphQLError

from .models import Media
from .service import MediaService
from .graphql_types import MediaType

service = MediaService()

class MediaQuery(graphene.ObjectType):
    '''
        Media Query, 
        fetch media entries matching to provided criteria
    '''

    media = graphene.Field(MediaType, id=graphene.ID(), height=graphene.Int(200), width=graphene.Int(200))
    
    def resolve_media(self, info, **args):
        media = service.fetch(id=args.get("id"), height=args.get("height"), width=args.get("width"))
        if media is None:
            raise GraphQLError(
                f'"{args.get("id")}" has not been found in our media listing.')

        return MediaType(**Media.wrap(media).as_dict())

schema = graphene.Schema(query=MediaQuery, auto_camelcase=True)
