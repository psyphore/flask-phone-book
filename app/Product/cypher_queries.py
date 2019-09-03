def get_product_query(name,first,skip):
  return '''
  OPTIONAL MATCH (p:Product)
  WHERE p.name =~ '{name}'.*
  RETURN p
  SKIP {skip}
  LIMIT {first}
  '''.replace('{skip}', skip).replace('{name}',name).replace('{first}',first)

def get_product_by_id_query(id):
  return '''
  OPTIONAL MATCH (p:Product{id:$id})
  RETURN p { 
  .name,
  .description,
  .id } AS product
  '''.replace('$id', id)