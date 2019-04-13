from py2neo.ogm import GraphObject, Property

class Media(GraphObject):
    '''
    Media object, 
        this represent a media entity
    '''

    id = Property()
    mime = Property()
    data = Property()
    
    def as_dict(self):
        return {
            'id': self.id,
            'data': self.data,
            'mime': self.mime
        }

    def __str__(self):
        return f'{self.id} {self.mime}'
