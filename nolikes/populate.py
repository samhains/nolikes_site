from nolikes import db, Image
from caption_fix import fix_caption
import json

IMG_DIR = '~/data/images/'

image_json = json.load(open('vis.json'))

for data in image_json:
    uuid = data['file_name'].split('/')[-1].split('.')[0]
    fname = IMG_DIR+data['file_name'].split('/')[-1]
    caption = fix_caption(data['caption'])
    image = Image(uuid, fname, caption)
    db.session.add(image)
    db.session.commit()

images = Image.query.all()
print(images)
