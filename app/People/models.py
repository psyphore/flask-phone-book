from py2neo.ogm import Property, RelatedTo, Label

from app.models import BaseModel


class Person(BaseModel):
    __primarykey__ = 'email'

    person = Label("Person")

    title = Property()
    firstname = Property()
    lastname = Property()
    mobile_number = Property('mobileNumber')
    email_address = Property('emailAddress')
    date_updated = Property('updatedOn')

    # receipts = RelatedTo('Receipt', 'HAS')
    # stores = RelatedTo('Store', 'GOES_TO')

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
