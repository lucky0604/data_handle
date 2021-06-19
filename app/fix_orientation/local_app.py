import os
from PIL import Image, ExifTags
import shutil

def pick_imgs(path):
    for root, dirs, filelist in os.walk(path):
        for filename in filelist:
            if filename != '.DS_Store':
                img = Image.open(os.path.join(root, filename))
                try:
                    for orientation in ExifTags.TAGS.keys() : 
                        if ExifTags.TAGS[orientation]=='Orientation' : break 
                    exif=dict(img._getexif().items())
                    if exif[orientation] == 6:
                        root_name = root[2:]
                        output_path = os.path.join('./output_bak', root_name)
                        print(output_path)
                        if os.path.exists(output_path) == False:
                            os.makedirs(output_path)

                        shutil.move(os.path.join(root, filename), output_path + '/' + filename)
                except:
                    pass

if __name__ == '__main__':
    pick_imgs('./data')