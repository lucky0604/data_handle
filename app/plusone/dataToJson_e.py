# Plusone 数据导出


import os
# import pandas as pd
import urllib3
import json
import requests
http = urllib3.PoolManager()
#json.loads() str to dict
#json.dump() dict to str and write to a file-like object
#json.load() read data from json file
#json.dumps() dict to str

from requests.packages.urllib3.exceptions import InsecureRequestWarning
 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class DataTransfer:

    def getData(self):
        r = requests.post('https://app.labelhub.cn/api/product/productDataJson?pid=9515&status=1&check=1', verify=False)
        # r = http.request(
        #     'POST', 'http://app.labelhub.cn/api/product/productDataJson?pid=5679')
        json_data = json.loads(r.text)    # str to dict
        return json_data['data']

    def transferData(self):
        data = self.getData()
        data_json = {}
        for i in data:

            # print(i, ' data i -----')
            data_json['shapes'] = []
            detail = json.loads(i['detail'])
            for j in detail['svgArr']:
                shape_obj = {}
                shape_obj['shape_type'] = j['tool']
                shape_obj['points'] = []
                # print(j)
                if not j['data']:
                    continue
                for k in j['data']:
                    # if 'x' in k and k['x'] and 'y' in k and k['y']:
                    if k['x'] == 0:
                        print(k['x'], '---------------------00')


                    points_arr = []
                    points_arr.append(k['x'])
                    points_arr.append(k['y'])
                    shape_obj['points'].append(points_arr)

                data_json['shapes'].append(shape_obj)
                shape_obj['flags'] = {}
                shape_obj['group_id'] = None
                shape_obj['label'] = j['name']
            data_json['imagePath'] = i['iname']
            data_json['flags'] = {}
            data_json['imageWidth'] = i['width']
            data_json['imageHeight'] = i['height']
            with open('./9515/' + i['iname'].split('.')[0] + '.json', 'w') as f:
                json.dump(data_json, f, indent = 4)

transDir = DataTransfer()
transDir.transferData()
