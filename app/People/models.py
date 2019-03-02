from py2neo.ogm import GraphObject, Property, RelatedTo

from app.models import BaseModel
# from app.Products.models import Product
# from app.Buildings.models import Building
# BaseModel, 

class Person(GraphObject):
    '''
    Person object, this represent a person in this system
    '''
    __primarykey__ = 'firstname'

    title = Property()
    firstname = Property()
    lastname = Property()
    mobile_number = Property('mobileNumber')
    email_address = Property('emailAddress')
    date_updated = Property('updatedOn')

    # products = RelatedTo('Product', 'KNOWS')
    # building = RelatedTo('Building', 'LOCATED_IN')
    team = RelatedTo('Person')
    manager = RelatedTo('Person', 'MANAGES')

    @classmethod
    def all(self, graph_instance):
        return self.match(graph_instance)

    @classmethod
    def filter(self, graph_instance, criteria):
        return self.match(graph=graph_instance).where(f"_.firstname = ~'{criteria}.*'")

    def as_dict(self):
        return {
            'title': self.title,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'mobileNumber': self.mobile_number,
            'email': self.email_address,
            'lastUpdatedOn': self.date_updated
        }

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
