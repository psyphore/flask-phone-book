from py2neo.ogm import GraphObject, Property, RelatedTo

class Person(GraphObject):
    '''
    Person object, 
    this represent a person entity and their relationships to other entities
    '''

    id = Property()
    title = Property()
    firstname = Property()
    lastname = Property()
    mobile = Property()
    email = Property()
    bio = Property()
    knownAs = Property()
    avatar = Property()

    # products = RelatedTo('Product', 'KNOWS')
    # building = RelatedTo('Building', 'BASED_IN')
    team = RelatedTo('Person')
    manager = RelatedTo('Person', 'MANAGES')
    deactivated = Property()

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'mobile': self.mobile,
            'email': self.email,
            'bio': self.bio,
            'knownAs': self.knownAs,
            'avatar': self.avatar,
            'team': self.team,
            'manager': self.manager,
            'deactivated': self.deactivated
        }

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
