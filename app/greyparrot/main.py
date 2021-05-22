#!/usr/bin/env python
#-*- coding:utf-8 -*-
#   Greyparrot 标签修改
import os
import os.path
import json
# from collections import defaultdict


def changeId(path):
    for parents,dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(parents,file)
            with open(filepath,'r') as f:
                oldfile = json.load(f)
                categories = []
                for c in oldfile['categories']:
                    categ_info={}
                    categ_info['name']=c['name']
                    categ_info['id']=c['id']
                    categories.append(categ_info)

                for a in oldfile['annotations']:
                    for b in categories:
                        if a['category_id'] == b['name']:
                            a['category_id']=b['id']


                with open(filepath,'w') as f:
                    json.dump(oldfile, f, indent = 4)


path = './Json/'
changeId(path)
