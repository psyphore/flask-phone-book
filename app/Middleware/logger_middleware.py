class LoggerMiddleware(object):
  def __init__(self, app):
    self.app = app

  def __call__(self, environ, start_response):
    print('----Logger Function called----')
    return self.app(environ, start_response)