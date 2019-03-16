from flask_jwt_extended import (create_access_token, create_refresh_token, get_jwt_identity, get_raw_jwt)
from passlib.hash import pbkdf2_sha256 as sha256


def generate_hash(password):
    return sha256.hash(password)

def verify_hash(password, hash):
    return sha256.verify(password, hash)

def get_user_info(token):
  if token is not None:
    pass
  pass

