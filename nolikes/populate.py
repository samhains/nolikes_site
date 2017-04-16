from nolikes import db, Image
from sqlalchemy import exc
from caption_fix import fix_caption
import json

IMG_DIR = '~/data/images/'

image_json = json.load(open('vis.json'))

Image.query.delete()
db.session.commit()

i = 0
for data in image_json:
    uuid = data['file_name'].split('/')[-1].split('.')[0]
    fname = IMG_DIR+data['file_name'].split('/')[-1]
    caption = fix_caption(data['caption'])
    image = Image(uuid, fname, caption)
    i = i+1
    print('saving image id:', i)
    db.session.add(image)
    try:
      db.session.commit()
    except exc.SQLAlchemyError, e:
      print(e)

images = Image.query.all()
