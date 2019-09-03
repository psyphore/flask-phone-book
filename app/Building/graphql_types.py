import graphene

from .models import Building
from .service import BuildingService

from app.People.models import Person
import app.People.graphql_types

service = BuildingService()


class BuildingType(graphene.ObjectType):
    '''
    Building Type, 
        represents a GraphQL version of a building entity
    '''

    id = graphene.ID(required=True)

    name = graphene.String(required=True)
    address = graphene.String(required=True)
    headcount = graphene.Int()

    people = graphene.List(lambda: app.People.graphql_types.PersonType)

    def resolve_people(self, info, **args):
        return [app.People.graphql_types.PersonType(**Person.wrap(member).as_dict()) for member in service.fetch_people(building=self)]
