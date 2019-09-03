import graphene

class ProductType(graphene.ObjectType):
    id = graphene.ID()

    name = graphene.String()
    description = graphene.String()
    category = graphene.String()

