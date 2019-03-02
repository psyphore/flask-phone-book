import maya
from py2neo import Graph

from app import settings


class GraphContext(object):
  '''
  GraphContext, will give you a connection to graph database specified on the .env
  '''
  # graph=None
  def __init__(self):
    self.graph = Graph(
        host=settings.NEO4J_HOST,
        port=settings.NEO4J_PORT,
        user=settings.NEO4J_USER,
        password=settings.NEO4J_PASSWORD,
    )
    # print(f'> Graph {dir(self.graph)} initialized')


  def get_instance(self):
    return self.graph

  def close_instance():
    pass
