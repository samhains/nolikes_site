from nolikes import db, Image
from sqlalchemy import exc
from caption_fix import fix_caption
import json

IMG_DIR = '~/data/new_images/'
image_json = json.load(open('cap.json'))
image_json_im2txt = json.load(open('cap_im2txt.json'))


i = 0

def get_im2txt_caption(fname):
    fname = fname+".jpg"
    return fix_caption(image_json_im2txt[fname])

for data in image_json:
    uuid = data['file_name'].split('/')[-1].split('.')[0]
    fname = IMG_DIR+data['file_name'].split('/')[-1]
    caption = fix_caption(data['caption'])
    caption_im2txt = get_im2txt_caption(uuid)
    count = Image.query.filter_by(caption=caption).count()
    print(caption, caption_im2txt)
    print(count)
    image = Image(uuid, fname, 'v2_p2p_curated', caption, caption_im2txt, 0)
    i = i+1
    print('saving image id:', i)
    print('saving image id:', image)
    db.session.add(image)
    try:
      db.session.commit()
    except exc.SQLAlchemyError, e:
      print(e)




images = Image.query.all()
