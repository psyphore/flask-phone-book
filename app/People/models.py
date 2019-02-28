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

    receipts = RelatedTo('Receipt', 'HAS')
    stores = RelatedTo('Store', 'GOES_TO')

