import os
import glob
import urllib.request

EXTENSION_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
THUMBNAILS_DIR = EXTENSION_DIR + '/thumbnails/'


def strip_list(elements):
    return [element for element in elements if len(element.strip()) > 0]


def clear_thumbnails():
    files = glob.glob(THUMBNAILS_DIR + '*')
    
    for f in files:
        os.remove(f)


def save_thumbnail(url, video_id):
    path = THUMBNAILS_DIR + video_id + '.png'

    urllib.request.urlretrieve(url, path)

    return path