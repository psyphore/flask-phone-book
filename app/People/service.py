from app.graph_context import GraphContext

from .models import Person


class PeopleService():
    '''
    This People Service houses all the actions can be performed against the person object
    '''
    
    def __init__(self):
        # print(f'> initializing person service')
        context = GraphContext()
        self.graph = context.get_instance()
        print(f'Person object {dir(Person)}')
        self.person = Person()
        # print(f'> got graph instance {dir(self.graph)}')

    def fetch(self, email):
        person = self.person.match(self.graph, f'emailAddress = {email}').first()
        if person is None:
            raise GraphQLError(
                f'"{email}" has not been found in our customers list.')

        return person

    def fetch_all(self):
        people = Person.all
        if people is None:
            raise GraphQLError(
                f'we did not find any people, please populate first.')

        return people
    
    def filter(self, query):
        return list(self.person.filter(graph_instance=self.graph).where(f"_.firstname = ~'{query}.*'"))
        # people = Person.match().select(self.graph).where(f"_.firstname = ~'{query}.*'")        
        # return people
