from graphql import GraphQLError
from app.graph_context import GraphContext

from .models import Person


class PeopleService(Person):
    '''
    This People Service houses all the actions can be performed against the person object
    '''
    
    def __init__(self):
        print(f'> initializing person service')
        context = GraphContext()
        self.graph = context.get_instance()
        print(f'> got graph instance {self.graph}')

    def fetch(self, email):
        person = Person.select(self.graph, email_address=email).first()
        if person is None:
            raise GraphQLError(
                f'"{email}" has not been found in our customers list.')

        return person

    def fetch_all(self):
        people = Person.select(self.graph)
        if people is None:
            raise GraphQLError(
                f'we did not find any people, please populate first.')

        return people
    
    def filter(self, query):
        people = Person.select(self.graph).where(f"_.firstname = ~'{query}.*'")
        if people is None:
            raise GraphQLError(
                f'"{query}" has not been found in our customers list.')

        return people
