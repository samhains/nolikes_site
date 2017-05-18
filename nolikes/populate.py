from nolikes import db, Image
from sqlalchemy import exc
from caption_fix import fix_caption
import json

IMG_DIR = '~/data/images/'
image_json = json.load(open('vis.json'))

Image.query.delete()
db.session.commit()

i = 0
for filename, caption in image_json.items():
    print(filename, caption)
    uuid = filename.split('.')[0]
    fname = IMG_DIR+filename
    caption = fix_caption(caption)
    count = Image.query.filter_by(caption=caption).count()
    print(caption)
    print(count)
    image = Image(uuid, fname, caption, count)
    i = i+1
    print('saving image id:', i)
    db.session.add(image)
    try:
      db.session.commit()
    except exc.SQLAlchemyError, e:
      print(e)

images = Image.query.all()
