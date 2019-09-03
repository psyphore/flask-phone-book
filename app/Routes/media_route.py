from flask import Response, json, stream_with_context

from app.Media.service import MediaService

service = MediaService()

def _handle_stream_response(data):
  if data:
    return Response(stream_with_context(data['data']), direct_passthrough=True, mimetype=data["mime"])
  return json.dumps({'result': 'image not found'}), 404, {'ContentType': 'application/json'}

def get_media(id, height, width, grey):
    try:
      media = service.fetch_with_dimensions(id, height=height, width=width, grey_out=grey)
      return _handle_stream_response(media)
    except exception as ex:
      print(f'X mr_gm: failed to fetch image, {ex}')
      return json.dumps({'result': 'failed to fetch image'}), 500, {'ContentType': 'application/json'}

def process_media(data):
    try:
      service.save_media(data)
      return json.dumps({'result': 'success'}), 200, {'ContentType': 'application/json'}
    except exception as ex:
      print(f'X mr_pm: failed to save image, {ex}')
      return json.dumps({'result': 'failed to save image'}), 500, {'ContentType': 'application/json'}