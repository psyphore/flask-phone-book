import re
from io import (BytesIO)
from base64 import (b64encode, b64decode)
from PIL import Image, ImageColor, ImageFilter

def generator(content):
  '''
    generic generator for streaming content
      :content = must me a bytes
  '''
  for b in BytesIO(content):
    yield b

def another_image_processor_2(payload_data):
  image_data = re.sub('^data:image/.+;base64,', '', payload_data)
  image = Image.open(BytesIO(b64decode(image_data)))
  return image

def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
 
    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print('The resized image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image.show()
    resized_image.save(output_image_path)

def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))
 
    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')
 
    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)
 
    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size
    print('The scaled image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))

def scale_image_2(data, height, width):
  original_image = data.copy()
  w, h = original_image.size

  if width and height:
      max_size = (width, height)
  elif width:
      max_size = (width, h)
  elif height:
      max_size = (w, height)
  else:
      max_size = (w, h)

  original_image.thumbnail(max_size, Image.ANTIALIAS)
  buffer = BytesIO()
  original_image.save(buffer, format='PNG')
  return buffer.getvalue()

def grey_out_image_2(data):
  original_image = Image.open(BytesIO(data)).convert('LA').filter(ImageFilter.SHARPEN)
  buffer = BytesIO()
  original_image.save(buffer, format='PNG')
  return buffer.getvalue()
  
def bytearr_to_b64s(ba):
  img = Image.fromarray(ba, 'RGB')                  
  buffer = BytesIO()
  img.save(buffer,format="PNG")
  return f"data:image/png;base64,{b64encode(buffer.getvalue())}"