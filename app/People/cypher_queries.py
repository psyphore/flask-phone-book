def get_person_query():
  query='''
  OPTIONAL MATCH (p:Person)
  WHERE p.firstname =~ '{name}'.*
  RETURN p
  SKIP {skip}
  LIMIT {first}
  '''
  return query

