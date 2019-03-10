import graphene

from app.People.graphql_types import PersonType

class SearchType(graphene.InputObjectType):
    '''Search, 
        :query, your search phrase
        :first, how many are you fetching in a set
        :offest, number to offset by a set
    '''
    query = graphene.NonNull(graphene.String)
    first = graphene.Int(10)
    offset = graphene.Int(0)
    # class Arguments:
    #     query = graphene.String(required=True)
    #     first = graphene.Int(10)
    #     offset = graphene.Int(0)

class SearchResultType(graphene.ObjectType):
    '''Search Result, containing a count of items contained in the items member'''

    count = graphene.Int(0)
    data = graphene.List(lambda: PersonType)
