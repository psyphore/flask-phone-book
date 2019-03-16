import graphene

import app.People.schema
import app.Search.schema
import app.Building.schema

class SuperQuery(app.People.schema.PeopleQuery,
                 app.Search.schema.SearchQuery,
                 app.Building.schema.BuildingQuery,
                 graphene.ObjectType):
    pass

class SuperMutant(app.People.schema.PeopleMutations,
                  graphene.ObjectType):
    pass

schema = graphene.Schema(
    query=SuperQuery, mutation=SuperMutant, auto_camelcase=True)
