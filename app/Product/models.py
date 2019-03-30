from py2neo.ogm import GraphObject, Property

class Product(GraphObject):
    '''
    Product object, 
    this represent a product entity
    '''

    id = Property()

    name = Property()
    description = Property()
    category = Property()

    def as_dict(self):
        return {
            'id':self.id,
            'name': self.name,
            'description': self.description
        }

    def __str__(self):
        return f'{self.name} {self.description}'
