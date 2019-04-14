import re
from io import (BytesIO)
from base64 import (b64encode, b64decode, standard_b64decode, urlsafe_b64decode)
from json import (dump, dumps)
from flask_jwt_extended import (create_access_token, create_refresh_token, decode_token)
from passlib.hash import pbkdf2_sha256 as sha256
from pandas import read_csv, read_excel
from skimage import data, io, util
from skimage.color import rgb2gray
import numpy as np
from PIL import Image

from app import settings

def generate_hash(password):
    return sha256.hash(password)

def verify_hash(password, hash):
    return sha256.verify(password, hash)

def get_user_info(token):
  token = str(token).strip().replace('Bearer ', '')
  if token is not None:
    decoded = decode_token(encoded_token=token,allow_expired=settings.DEBUG)
    if decoded is not None:
      print(f'> decoded to: {dumps(decoded)}')
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

def read_sheet_file(file_path, index_col, file_type):
  '''
  Read sheet file,
  for reading excel or csv file content
    :file_path - full path to the file to be read
    :index_col - 1st column name to read from
    :file_type - 1=csv, 2=excel
  '''
  content = None
  if file_type == 1:
    content=pd.read_csv(file_path, index_col=[index_col])

  if file_type == 2:
    content=pd.read_excel(file_path, index_col=[index_col])
  
  return content

def read_file(file_path):
  with open(file=file_path, mode='r') as content:
    data=content.read()
    return data
    