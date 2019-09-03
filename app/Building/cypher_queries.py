def get_buildings_query(first, skip):
    return '''
  MATCH (building:Building)
  RETURN building { 
    .id , 
    .name , 
    .address ,
    headcount: apoc.cypher.runFirstColumn("RETURN SIZE((this)<-[:BASED_IN]-())", {this: building}, false),
    people: [(building)<-[:BASED_IN]-(p) | p] } 
  AS building 
  SKIP {skip}
  LIMIT {first}
  '''.replace('{skip}', skip).replace('{first}', first)


def get_building_by_id_or_name_query(id, name):
    return '''
  MATCH (b:Building)
  WHERE b.name =~(?i) '.*{name}.*' OR b.id = {id}
  RETURN b { 
    .id , 
    .name , 
    .address ,
    headcount: apoc.cypher.runFirstColumn("RETURN SIZE((this)<-[:BASED_IN]-())", {this: b}, false),
    people: [(b)<-[:BASED_IN]-(p) | p] } 
  AS building
  '''.replace('{id}', id).replace('{name}', name)
