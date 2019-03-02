from app.graph_context import GraphContext

from .models import Person


class PeopleService():
    '''
    This People Service houses all the actions can be performed against the person object
    '''
    
    def __init__(self):
        context = GraphContext()
        self.graph = context.get_instance()
        print(f'Person object {dir(Person)}')
        self.person = Person()

    def fetch(self, email):
        return self.person.match(self.graph, f'emailAddress = {email}').first()
        

    def fetch_all(self):
        return list(self.person.all())
        
    
    def filter(self, query):
        return list(self.person.filter(graph_instance=self.graph, criteria=query))
