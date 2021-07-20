import os

def delete_jpg(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.split('.')[-1] != 'json':
                os.remove(os.path.join(root, filename))

if __name__ == '__main__':
    delete_jpg('./data')
