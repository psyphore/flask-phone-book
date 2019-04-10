class AuthorizationMiddleware(object):
  def resolve(self, next, root, info, **args):
    if info.field_name == 'user':
      return None
    return next(root, info, **args)