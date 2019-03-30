def filter_person_query(name, skip, first):
  return '''
  OPTIONAL MATCH (p:Person)
  WHERE p.firstname =~ '(?i){name}.*'
    OR p.lastname =~ '(?i){name}.*'
    OR p.title =~ '(?i).*{name}.*'
    OR p.email =~ '(?i).*{name}.*'
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

def filter_person_query_2(name, skip, first):
  return '''
    WITH {name} AS query
    OPTIONAL MATCH (p:Person), (b:Building), (pr:Product)
    WHERE   p.title =~ '(?i).*{name}.*'
            OR p.firstname =~ '(?i){name}.*'
            OR p.lastname =~ '(?i){name}.*'
            OR query CONTAINS " " AND (toLower(query) = toLower(p.firstname)+ " "+ toLower(p.lastname)))
            OR query CONTAINS ", " AND (toLower(query) = toLower(p.lastname)+ ", "+ toLower(p.firstname)))
      OR ((p)--(b) AND (toLower(b.name) CONTAINS toLower(query) OR toLower(b.address) CONTAINS toLower(query)))
        OR ((p)--(pr) AND (toLower(pr.name) CONTAINS toLower(query))
    WITH p { 
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
    RETURN DISTINCT person
    ORDER BY person.lastname ASC, person.firstname ASC
    SKIP {skip}
    LIMIT {first}
  '''.replace('{name}',name).replace('{skip}',skip).replace('{first}',first)