import uuid
import pymysql
import json
import os

connection = pymysql.connect(host='rm-bp1r66l8s2tl5q81jfo.mysql.rds.aliyuncs.com',
                             user='labelhub_user',
                             password='Jxxl-label2020',
                             database='zhengshi_labelhub',
                             cursorclass=pymysql.cursors.DictCursor)

def load_json(path):
    for root, dirs, filelist in os.walk(path):
        for filename in filelist:
            if filename.split('.')[-1] == 'json':
                with open(os.path.join(root, filename), 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                    with connection.cursor() as cursor:
                        sql = 'SELECT * FROM product WHERE id = 8859;'
                        cursor.execute(sql)
                        result = cursor.fetchone()
                        print(result['label'], ' --- ')


# with connection.cursor() as cursor:
#     # Read a single record
#     sql = "SELECT * FROM product where `id` = 8858;"
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     tools = json.loads(result["label"])
#     print(tools["tools"])

# connection.close()

load_json('./data')