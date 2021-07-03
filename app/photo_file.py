import os
from PIL import Image


BASE_DIR = os.path.dirname(__file__)
DATA_FILE = BASE_DIR + '/data/photos.sqlite3'
FILES_DIR = BASE_DIR + '/files'

def get_path(file_id, ptype=''):
    return FILES_DIR + '/' + str(file_id) + ptype + '.jpg'

def make_thubnail(file_id, size):
    src = get_path(file_id)
    des = get_path(file_id, '-thumb')
    if os.path.exists(des):
        return des
    img = Image.open(src)
    msize = min(img.width, img.height)
    img_crop = image_crop_center(img, msize)
    img_resize = img_crop.resize((size, size))
    img_resize.save(des, quality=95)
    return des

def image_crop_center(img, size):
    cx = int(img.width / 2)
    cy = int(img.height / 2)
    img_crop = img.crop((
        cx - size / 2, cy - size / 2,
        cx + size / 2, cy + size / 2
    ))
    return img_crop