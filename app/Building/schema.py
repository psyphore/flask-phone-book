import graphene
from graphql import GraphQLError

from .models import Building
from .service import BuildingService
from .graphql_types import BuildingType

service = BuildingService()


class BuidlingQuery(graphene.ObjectType):
    '''Buidling Query, fetch building entries matching to provided criteria'''

    building = graphene.Field(
        BuildingType, id=graphene.ID(), name=graphene.String())
    buildings = graphene.Field(lambda: BuildingType, limit=graphene.Int(5))

    def resolve_building(self, info, **args):
        identity = args.get("id")
        name = args.get("name")
        building = service.fetch(id=identity, name=name)
        if building is None:
            raise GraphQLError(
                f'"{identity}" has not been found in our building listing.')

        return BuildingType(**Building.wrap(building).as_dict())

    def resolve_buildings(self, info, **args):
        print(f's_rbs > {args}')
        limit = args.get("limit")
        buildings = service.fetch_all(limit=limit)
        if buildings is None or len(buildings) is 0:
            raise GraphQLError(f'no building listings found.')

        return [BuildingType(**Building.wrap(building).as_dict()) for building in buildings]


schema = graphene.Schema(
    query=BuidlingQuery, auto_camelcase=True, types=[BuildingType])
