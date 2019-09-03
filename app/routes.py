from flask import (send_file)
from flask import (stream_with_context, Response)

from app.utilities import (fetch_media, stream_media)

def media(id, height, width):
  # fetch image data
  # fetch mimetype
  # fetch cache
  result = fetch_media(id, height, width)
  if result is not None:
    return send_file(result.data,mimetype=result.mime_type,cache_timeout=result.cache)

  return None

def stream_content(name):
  return Response(stream_with_context(stream_media(name)))