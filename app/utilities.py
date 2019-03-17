from flask_jwt_extended import (create_access_token, create_refresh_token)
from flask_graphql_auth import (get_jwt_identity, get_raw_jwt, decode_jwt, get_jwt_data)
from passlib.hash import pbkdf2_sha256 as sha256

from app import settings

def generate_hash(password):
    return sha256.hash(password)

def verify_hash(password, hash):
    return sha256.verify(password, hash)

def get_user_info(token):
  token = str(token).strip().replace('Bearer ', '')
  if token is not None:
    # decoded = get_jwt_data(token=token, token_type='access')
    # decoded = decode_jwt(token, settings.JWT_SECRET_KEY, 'HS256', 'identity', None)
    decoded = token
    print(f'i_gui > decoded: {decoded}')
    return decoded
  return None
  
def create_tokens(identity):
  if str(identity).strip() is not None:
    return {
      'access_token' : create_access_token(identity),
      'refresh_token' : create_refresh_token(identity)
    }
  return None
