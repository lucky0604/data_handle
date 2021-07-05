import subprocess
import os

def fix_image(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            image = os.path.join(root, filename)
            # print(image)
            x = subprocess.run(['exiftran', '-ai', image])
            if x.returncode != 0:
                print(filename)
            else:
                print(filename, ' fixed!')

if __name__ == '__main__':
    fix_image('./images')

