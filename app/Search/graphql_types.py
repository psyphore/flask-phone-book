import graphene

from app.People.graphql_types import PersonType

class SearchType(graphene.InputObjectType):
    '''Search, 
        :query, your search phrase
        :first, how many are you fetching in a set
        :offest, number to offset by a set
    '''
    query = graphene.NonNull(graphene.String)
    first = graphene.Int()
    offset = graphene.Int()

    @property
    def criteria(self):
        return f"({self.query},{self.first},{self.offset})"

class SearchResultType(graphene.ObjectType):
    '''Search Result, 
        containing a count of items contained in the data member
    '''

    count = graphene.Int(0)
    data = graphene.List(lambda: PersonType)
