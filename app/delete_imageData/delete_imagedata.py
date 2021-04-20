import os
import json

def delete_imgData(path):
    for root, dirs, filelist in os.walk(path):
        for filename in filelist:
            if filename.split('.')[-1] == 'json':
                with open(os.path.join(root, filename), 'r') as f:
                    json_obj = json.load(f)
                    json_obj['imageData'] = None
                    with open(os.path.join(root, filename), 'w') as wf:
                        json.dump(json_obj, wf)

delete_imgData('./2020100505')