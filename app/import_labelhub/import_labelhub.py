import uuid
import pymysql
import json
import os
from pymysql.converters import escape_string

connection = pymysql.connect(host='rm-bp1r66l8s2tl5q81jfo.mysql.rds.aliyuncs.com',
                             user='labelhub_user',
                             password='Jxxl-label2020',
                             database='zhengshi_labelhub',
                             cursorclass=pymysql.cursors.DictCursor)

label_map = {
    'brown_board': 'corrugated_cardboard',
    'hdpe_bottles_natural': 'natural_hdpe_bottles_food',
    'pet_bottles_clear': 'clear_pet_bottles_food',
    'plastic_bottles_coloured': 'coloured_pet_bottles_nonfood',
    'plastic_pots_tubs_trays': 'other_plastic',
    'uncertain': 'uncertain_class',
    '': 'fines',
    'clear_containerclear_container': 'clear_container',
    'uncertain_plastic': 'uncertain_plastic_bottle',
    'eoffice_paper': 'office_paper',
    'fiens': 'fines',
    'clear_container.': 'clear_container',
    'vclear_pet_bottles_food': 'clear_pet_bottles_food',
    'v': 'fines',
    'uncretain_class': 'uncertain_class',
    'clear_pet_bottles_foodv': 'clear_pet_bottles_food'
}

def load_json(path):
    count = 0
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
                        count = count + 1
                        print(count, ' count =======')
                        label_data = dict()
                        # print(i, ' ---------- shape item ------')
                        with connection.cursor() as cursor:
                            sql = 'SELECT * FROM product WHERE id = 10509;'
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            count = count + 1
                            print(count)
                            for j in json.loads(result["label"])["tools"]:
                                if i["label"] in label_map:
                                    label_data["name"] = label_map[i["label"]]
                                else:
                                    label_data["name"] = i['label']
                            for j in json.loads(result["label"])["tools"]:
                                if label_data["name"] == j["name"]:
                                    label_data["uuid"] = str(uuid.uuid4())
                                    label_data["radius"] = 3
                                    label_data["isFilling"] = str(False)
                                    label_data["related"] = []
                                    label_data["id"] = j["id"]
                                    label_data["color"] = j["color"]
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
                    sql = "SELECT * FROM product_record_detail WHERE pid = 8928;"
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
                    cursor.close()



# with connection.cursor() as cursor:
#     # Read a single record
#     sql = "SELECT * FROM product where `id` = 8858;"
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     tools = json.loads(result["label"])
#     print(tools["tools"])

# connection.close()

load_json('./data')
