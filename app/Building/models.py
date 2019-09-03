from py2neo.ogm import GraphObject, Property

class Building(GraphObject):
    '''
    Building object, 
        this represent a building or location entity
    '''

    id = Property()
    name = Property()
    address = Property()
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }

    def __str__(self):
        return f'{self.name} {self.address}'
