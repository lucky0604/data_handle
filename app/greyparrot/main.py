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

                for i in oldfile['images']:
                    filename = i['file_name']
                    i['file_name'] = filename.split('-')[-1]
                    '''
                    if '-' in i['file']:
                        i['file'] = 'Master.MR.2/' + '/'.join(i['file'].split('-')[1:])
                    '''
                    if '-' in i['file'] and i['file'].split('.')[0] == 'Master':
                        i['file'] = 'Master.MR.2/' + '/'.join(i['file'].split('-')[1:])

                    # handle the B.Fraction.MR.1 start file
                    else:
                        #i['file'] = '/'.join(i['file'].split('-'))
                        i['file'] = filename[0:15] + '/' + filename[16:21] + '/' + '/'.join(filename[22:].split('-'))
                        i['file'] = list(i['file'])
                        i['file'][21] = '-'
                        i['file'] = ''.join(i['file'])

                for c in oldfile['categories']:
                    categ_info={}
                    categ_info['name']=c['name']
                    for ch in c['name']:
                        if u'\u4e00' <= ch <= u'\u9fff':
                            return False
                        else:
                            print('no Chinese')
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
