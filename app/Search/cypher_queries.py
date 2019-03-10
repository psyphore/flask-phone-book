def filter_person_query(name, skip, first):
  return '''
  OPTIONAL MATCH (p:Person)
  WHERE p.firstname =~ '(?i){name}.*'
    OR p.lastname =~ '(?i){name}.*'
    OR p.title =~ '(?i).*{name}.*'
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
  ORDER BY person.lastname ASC, person.firstname ASC
  SKIP {skip}
  LIMIT {first}
  '''.replace('{name}',name).replace('{skip}',skip).replace('{first}',first)