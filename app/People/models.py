from py2neo.ogm import Property, RelatedTo, Label

from app.models import BaseModel
# from app.Products.models import Product
# from app.Buildings.models import Building


class Person(BaseModel):
    '''
    Person object, this represent a person in this system
    '''
    __primarykey__ = 'email'

    person = Label("Person")

    title = Property()
    firstname = Property()
    lastname = Property()
    mobile_number = Property('mobileNumber')
    email_address = Property('emailAddress')
    date_updated = Property('updatedOn')

    # products = RelatedTo('Product', 'KNOWS')
    # building = RelatedTo('Building', 'LOCATED_IN')
    # team = RelatedTo('Person', 'MANAGES')
    # manager = RelatedTo('Person', 'MANAGES')

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
