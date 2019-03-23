from base64 import (b64decode, standard_b64decode, urlsafe_b64decode)
from json import (dump, dumps)
from flask_jwt_extended import (create_access_token, create_refresh_token, decode_token)
from passlib.hash import pbkdf2_sha256 as sha256

from app import settings

def generate_hash(password):
    return sha256.hash(password)

def verify_hash(password, hash):
    return sha256.verify(password, hash)

def get_user_info(token):
  token = str(token).strip().replace('Bearer ', '')
  if token is not None:
    decoded = decode_token(encoded_token=token,allow_expired=True)
    print(f'i_gui > decoded: {decoded}')
    if decoded is not None:
      return decoded
  return None

def poor_mans_token_parser(token):
  token = str(token).strip().replace('Bearer ', '')
  b64_parts = token.split('.')
  b64 = b64_parts[1]#.replace('-','+').replace('_','/')
  decoded = urlsafe_b64decode(b64) #standard_b64decode(b64)
  return dump(decoded)
  
def create_tokens(identity):
  if str(identity).strip() is not None:
    return {
      'access_token' : create_access_token(identity),
      'refresh_token' : create_refresh_token(identity)
    }
  return None
