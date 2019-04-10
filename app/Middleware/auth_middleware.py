from json import (dumps)
from app.utilities import (get_user_info)
class AuthMiddleware(object):
  def __init__(self, app):
    self.app = app
    self.token = None

  def __call__(self, environ, start_response):
    self.token = environ.get("HTTP_AUTHORIZATION")
    print(f'> token: {self.token}')
    # print(f'> content: {dumps(get_user_info(token=self.token))}')
    return self.app(environ, start_response)