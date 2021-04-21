import uuid
import pymysql
import json
import os
from pymysql.converters import escape_string

connection = pymysql.connect(host='',
                             user='labelhub_user',
                             password='Jxxl-label2020',
                             database='zhengshi_labelhub',
                             cursorclass=pymysql.cursors.DictCursor)

def load_json(path):
    for root, dirs, filelist in os.walk(path):
        for filename in filelist:
            if filename.split('.')[-1] == 'json':
                root_data = dict()
                root_data["svgArr"] = []
                root_data["classification"] = []
                with open(os.path.join(root, filename), 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                    shape_data = json_data["shapes"]
                    for i in shape_data:
                        label_data = dict()
                        # print(i, ' ---------- shape item ------')
                        with connection.cursor() as cursor:
                            sql = 'SELECT * FROM product WHERE id = 8859;'
                            cursor.execute(sql)
                            result = cursor.fetchone()

                            for j in json.loads(result["label"])["tools"]:
                                # print(j, ' tools ----------------')
                                if i["label"] == j["name"]:
                                    label_data["name"] = j["name"]
                                    label_data["uuid"] = str(uuid.uuid4())
                                    label_data["color"] = j["color"]
                                    label_data["radius"] = 3
                                    label_data["isFilling"] = str(False)
                                    label_data["related"] = []
                                    label_data["id"] = j["id"]
                                    label_data["subarea"] = 1
                                    label_data["tool"] = i["shape_type"]
                                    label_data["isClosed"] = str(True)
                                    label_data["mustShow"] = str(False)
                                    label_data["secondaryLabel"] = []
                                    label_data["min"] = "130*130"
                                    label_data["strokeW"] = 1.5
                                    label_data["data"] = []
                                    point1 = dict()
                                    point2 = dict()
                                    point3 = dict()
                                    point4 = dict()
                                    point1["x"] = i["points"][0][0]
                                    point1["y"] = i["points"][0][1]
                                    point2["x"] = i["points"][1][0]
                                    point2["y"] = i["points"][0][1]
                                    point3["x"] = i["points"][1][0]
                                    point3["y"] = i["points"][1][1]
                                    point4["x"] = i["points"][0][0]
                                    point4["y"] = i["points"][1][1]
                                    label_data["data"].append(point1)
                                    label_data["data"].append(point2)
                                    label_data["data"].append(point3)
                                    label_data["data"].append(point4)
                            cursor.close()
                        root_data["svgArr"].append(label_data)
                        
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM product_record_detail WHERE pid = 8859;"
                    cursor.execute(sql)
                    product_data = cursor.fetchall()
                    for pdata in product_data:
                        if filename.split('.')[0] == pdata['iname'].split('.')[0]:
                            print(pdata["id"])
                            update_sql = "UPDATE product_record_detail set detail = '" + escape_string(str(root_data).replace("'", '"')) + "' where id=%d" % int(pdata["id"])
                            try:
                                cursor.execute(update_sql)
                                connection.commit()
                                
                            except:
                                raise "failed"
                            print(str(root_data).replace("'", '"'), ' ------------ root data ==========')


# with connection.cursor() as cursor:
#     # Read a single record
#     sql = "SELECT * FROM product where `id` = 8858;"
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     tools = json.loads(result["label"])
#     print(tools["tools"])

# connection.close()

load_json('./data')