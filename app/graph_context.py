from py2neo import Graph, NodeMatcher, RelationshipMatcher

from app import settings

class GraphContext(object):
  '''
  GraphContext, will give you a connection to graph database specified on the .env
  '''
  
  graph=None
  
  def __init__(self):
    self.graph = Graph(f"bolt://{settings.NEO4J_HOST}:{settings.NEO4J_BOLT_PORT}", auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD))

  @property
  def get_instance(self):
    return self.graph

  @classmethod
  def close_instance():
    pass

  @property
  def get_instance_2():
    return Graph(f"bolt://{settings.NEO4J_HOST}:{settings.NEO4J_BOLT_PORT}", auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD))

  @property
  def get_node_matcher(self):
    return NodeMatcher(graph=self.get_instance)

  @property
  def get_relationship_matcher(self):
    return NodeMatcher(graph=self.get_instance)

  @staticmethod
  def graph_cypher_exec(self, cypher_query, **parameters):
    try:
      return self.get_instance.evaluate(cypher_query,parameters=parameters)
    except Exception as ex:
      print(f'x exception: {ex}')
      return []