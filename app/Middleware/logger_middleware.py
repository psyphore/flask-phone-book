from time import time as timer
from datetime import (datetime)
from maya import (Datetime, when)

class LoggerMiddleware(object):
  def __init__(self, app):
    self.app = app
    self.start = timer()
    self.end = None

  def __call__(self, environ, start_response):
    self.end = timer() - self.start
    print(f'> incoming: {datetime.utcnow()} in {round(self.end * 1000, 2)} ')
    return self.app(environ, start_response)