import os
from PIL import Image, ExifTags

tag_name_to_id = dict([(v, k) for k, v in ExifTags.TAGS.items()])

tag_name_to_id[270] = 'ImageDescription'
tag_name_to_id[306] = 'DateTime'
tag_name_to_id[256] = 'ImageWidth'
tag_name_to_id[257] = 'ImageLength'
tag_name_to_id[258] = 'BitsPerSample'
tag_name_to_id[40962] = 'PixelXDimension'
tag_name_to_id[40963] = 'PixelYDimension'
tag_name_to_id[305] = 'Software'
tag_name_to_id[37510] = 'UserComment'
tag_name_to_id[40091] = 'XPTitle'
tag_name_to_id[40092] = 'XPComment'
tag_name_to_id[40093] = 'XPAuthor'
tag_name_to_id[40094] = 'XPKeywords'
tag_name_to_id[40095] = 'XPSubject'
tag_name_to_id[40961] = 'ColorSpace' # Bit depth
tag_name_to_id[315] = 'Artist'
tag_name_to_id[33432] = 'Copyright'


def convert_exif_to_dict(exif):
    """
    This helper function converts the dictionary keys from
    IDs to strings so your code is easier to read.
    """
    data = {}

    if exif is None:
        return data

    for k,v in exif.items():
       if k in tag_name_to_id:
           data[tag_name_to_id[k]] = v
       else:
           data[k] = v

    # These fields are in UCS2/UTF-16
    # converting it to use within python
    for k in ['XPTitle', 'XPComment', 'XPAuthor', 'XPKeywords', 'XPSubject']:
        if k in data:
            data[k] = data[k].decode('utf-16').rstrip('\x00')

    return data

for file in os.listdir("/Users/siddeshpillai/Desktop/blah/images"):
    if file.endswith(".jpg"):
        im = Image.open(file)
        im.verify()
        exif = convert_exif_to_dict(im._getexif())