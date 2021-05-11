from PIL import Image, ExifTags
import urllib.request
import os
from dotenv import load_dotenv
import pymysql
import datetime

url = 'https://jxxl-tagtag-juexing.oss-cn-hangzhou.aliyuncs.com/5832/2021/04/30/c53d973884d65113337dd0b67fcee069.jpg'



pids = (
    9234,
    9235,
    9236,
    9237,
    9238,
    9239,
    9240,
    9241,
    9244,
    9245,
    9246,
    9248,
    9249,
    9250,
    9251,
    9252,
    9253,
    9254,
    9260,
    9262,
    9257,
    9263,
    9264,
    9265,
    9268,
    9269,
    9270,
    9271,
    9272,
    9273,
    9274,
    9276,
    9277,
    9279,
    9282,
    9293,
    9295,
    9296,
    9297,
    9298,
    9299,
    9301,
    9303,
    9304,
    9306,
    9309,
    9312,
    9345,
    9346,
    9347,
    9363,
    9146
)

# load env file
bundle_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(bundle_dir)
load_dotenv(os.path.join(root_dir, '.env'))

# mysql connector
config = {
    'host': os.environ['MYSQL_HOST'],
    'user': os.environ['MYSQL_USERNAME'],
    'password': os.environ['MYSQL_PASSWORD'],
    'database': os.environ['MYSQL_DATABASE'],
    'charset': 'utf8'
}

db = pymysql.connect(**config)
cur = db.cursor()

def fetch_imgurl():
    sql = f'SELECT * FROM product_record_detail WHERE pid in {pids}'
    cur.execute(sql)
    result = cur.fetchall()
    return result

'''
height index is 19
width index is 22
imagepath index is 4
'''
def change_w_h():
    res = fetch_imgurl()
    for i in res:
        img = Image.open(urllib.request.urlopen(i[4]))
        try:
            for orientation in ExifTags.TAGS.keys() : 
                if ExifTags.TAGS[orientation]=='Orientation' : break 
            exif=dict(img._getexif().items())
            print(exif[orientation])
            if exif[orientation] == 6 or exif[orientation] == 8:
                i[19], i[22] = i[22], i[19]
                width = i[22]
                height = i[19]
                image_id = i[0]
                sql = f'UPDATE product_record_detail set width = {width}, height = {height} WHERE id = {image_id}'
                cur.execute(sql)
                cur.commit()
        except:
            pass

    cur.close()
    db.close()

def change_local():
    for root, dirs, files in os.walk('./data'):
        for filename in files:
            if filename.split('.')[-1] == 'jpg':
                img = Image.open(os.path.join(root, filename))
                try:
                    for orientation in ExifTags.TAGS.keys() : 
                        if ExifTags.TAGS[orientation]=='Orientation' : break 
                    exif=dict(img._getexif().items())
                    print(exif[orientation])
                    print(os.path.join(root, filename))
                    if exif[orientation] == 6:
                        img = img.rotate(-90)
                    elif exif[orientation] == 8:
                        img = img.rotate(90)
                    elif exif[orientation] == 3:
                        img = img.rotate(180)
                    # img.save(os.path.join(root, filename))
                    img.save('./output/' + filename)
                except:
                    pass

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    # change_w_h()
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).seconds
    change_local()
    print(duration)