class AuthMiddleware(object):
  def __init__(self, app):
    self.app = app

  def __call__(self, environ, start_response):
    print('----Auth Function called----')
    print(f'> token: {environ.get("HTTP_AUTHORIZATION")}')
    return self.app(environ, start_response)