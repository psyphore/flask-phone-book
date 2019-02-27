import maya
from py2neo import Graph

from app import settings


class GraphContext(object):
  def __init__(self):
    self.graph = Graph(
        host=settings.NEO4J_HOST,
        port=settings.NEO4J_PORT,
        user=settings.NEO4J_USER,
        password=settings.NEO4J_PASSWORD,
    )

  @staticmethod
  def get_instance(self):
    return self.graph

  @staticmethod
  def close_instance(self):
    pass
