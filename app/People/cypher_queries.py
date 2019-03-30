def get_person_query(name, first, skip):
    return '''
  OPTIONAL MATCH (p:Person)
  WHERE p.firstname =~ '{name}'.*
  RETURN p
  SKIP {skip}
  LIMIT {first}
  '''.replace('{skip}', skip).replace('{name}', name).replace('{first}', first)


def get_person_by_id_query(id):
    return '''
  OPTIONAL MATCH (p:Person{id:"$id"})
  RETURN p { 
  .firstname,
  .mobile,
  .bio,
  .id,
  .title,
  .email,
  .lastname,
  .avatar,
  .knownAs,
  manager: apoc.cypher.runFirstColumn("MATCH (m)-[:MANAGES]->(this) RETURN m LIMIT 1", {this: p}, false),
  team: [(p)<-[:MANAGES]-()-[:MANAGES]->(t) | t],
  line: [(s)<-[:MANAGES]-(p) | s],
  products: [(p)-[:KNOWS]->(pr) | pr],
  building: [(p)-[:BASED_IN]->(b) | b]
  } AS person
  '''.replace('$id', id)


def get_private_person_by_id_query(id):
    return '''
  OPTIONAL MATCH (p:Person{id:"$id"})
  RETURN p { 
  .firstname,
  .mobile,
  .bio,
  .id,
  .title,
  .email,
  .lastname,
  .avatar,
  .knownAs,
  manager: apoc.cypher.runFirstColumn("MATCH (m)-[:MANAGES]->(this) RETURN m LIMIT 1", {this: p}, false),
  team: [(p)<-[:MANAGES]-()-[:MANAGES]->(t) | t],
  line: [(s)<-[:MANAGES]-(p) | s],
  products: [(p)-[:KNOWS]->(pr) | pr],
  building: [(p)-[:BASED_IN]->(b) | b]
  } AS person,
  {
    leave_items: [],
    authorization_key: 'an auth key',
    salary_level: 4,
    birth_date : '1987/3/9',
    next_of_keen : 'Spouse',
    employment_anniversary : '2018/1/4'
  } AS private
  '''.replace('$id', id)
