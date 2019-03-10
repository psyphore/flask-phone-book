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

  @property
  def get_instance_2():
    return Graph(f"bolt://{settings.NEO4J_HOST}:{settings.NEO4J_BOLT_PORT}", auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD))

  @property
  def get_node_matcher(self):
    return NodeMatcher(graph=self.get_instance)

  @property
  def get_relationship_matcher(self):
    return RelationshipMatcher(graph=self.get_instance)

  @staticmethod
  def exec_cypher(query, **kwargs):
    instance = Graph(f"bolt://{settings.NEO4J_HOST}:{settings.NEO4J_BOLT_PORT}", auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD))
    return instance.run(query, **kwargs).data()

  @staticmethod
  def exec_transaction(self, query, **kwargs):
    trx = self.get_instance.begin(autocommit=True)
    trx.evaluate(query,**kwargs)
    trx.commit()
