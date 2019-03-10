from py2neo.ogm import GraphObject, Property, RelatedTo

class Search(GraphObject):
    '''
    Search object, this represent a person entity nad his relationships to other entities
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

    team = RelatedTo('Person')
    manager = RelatedTo('Person', 'MANAGES')

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
            'avatar': self.avatar
        }

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
