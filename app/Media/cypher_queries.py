def save_media_query(data, mimetype, parentId, label):
    return '''
  WITH apoc.create.uuid() AS mediaId
  MERGE (m:Media{ id: mediaId })
  SET m +={
    data: '{_data}',
    mime: '{_mimetype}'
  }
  WITH m AS media
  MATCH (n)
  WHERE n.id = '{_parentId}'
    AND apoc.node.labels(n)[0] = '{_label}'
  SET n.avatar = media.id
  WITH media
  RETURN media
  '''.replace('{_data}', data).replace('{_mimetype}', mimetype).replace('{_parentId}', parentId).replace('{_label}', label)


def fetch_media_query(id):
    return '''
    MATCH (media:Media{id:'{_id}'}) REUTRN media
    '''.replace('{_id}', id)
