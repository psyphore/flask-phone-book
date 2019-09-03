from py2neo.ogm import GraphObject, Property

class Search(GraphObject):
    '''
    Search object
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
