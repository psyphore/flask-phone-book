import graphene
from graphql import GraphQLError

from app.People.models import Person
from .service import SearchService
from app.People.graphql_types import  PersonType
from .graphql_types import SearchType, SearchResultType

# service = SearchService()

class SearchQuery(graphene.ObjectType):   
    '''Search Query, 
        fetch person entries matching to provided criteria
    '''

    search = graphene.Field(SearchResultType, query=graphene.NonNull(graphene.String), limit=graphene.Int(10))
    search_advanced = graphene.Field(SearchResultType, criteria=graphene.NonNull(SearchType))
    
    def __init__(self):
        self.service = SearchService()

    def resolve_search(self, info, **args):
        q, l = args.get("query"), args.get("limit")
        result = self.service.filter(query=q,limit=l)

        if result is None:
            raise GraphQLError(f'"{q}" has not been found in our people list.')

        sr = SearchResultType()
        sr.count = len(result)
        sr.data = [PersonType(**Person.wrap(r).as_dict()) for r in result]

        return sr

    def resolve_search_advanced(self, info, criteria):
        result = self.service.filter(query=criteria.query,limit=criteria.first,skip=criteria.offset)

        if result is None:
            raise GraphQLError(f'"{criteria.query}" has not been found in our people list.')

        sr = SearchResultType()
        sr.count = len(result)
        sr.data = [PersonType(**Person.wrap(r).as_dict()) for r in result]

        return sr

schema = graphene.Schema(query=SearchQuery, auto_camelcase=True)
