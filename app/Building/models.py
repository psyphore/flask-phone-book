from py2neo.ogm import GraphObject, Property, RelatedTo

class Building(GraphObject):
    '''
    Building object, this represent a building/location entity nad his relationships to other entities
    '''

    id = Property()
    name = Property()
    address = Property()
    headcount = Property()
    
    people = RelatedTo('Person')
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'headcount': self.headcount,
            'people': self.people
        }

    def __str__(self):
        return f'{self.name} {self.address}'
