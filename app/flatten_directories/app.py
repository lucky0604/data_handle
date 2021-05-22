#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import math
from shutil import copyfile

output_dir_num = 4
files_arr = []

'''
usage:
split images into several dirs by images average number
e.g: input: Master.MR.RE/mrf_data/24/multiple dirs  output: 1/ 2/ 3/
'''
# def flatten_directories(path):
#     for root, dirs, files in os.walk(path):
#
#         for i in range(output_dir_num):
#             output_path = './output/' + str(i + 1)
#             if os.path.exists(output_path) == False:
#                 os.makedirs(output_path)
#         for filename in files:
#             files_arr.append(os.path.join(root, filename))
#
#     for i in range(output_dir_num):
#         result_list = files_arr[math.floor(i / output_dir_num * len(files_arr)) : math.floor((i + 1) / output_dir_num * len(files_arr))]
#         for j in result_list:
#             output_name = '-'.join(j.split('/')[2:])
#             print(output_name)
#             copyfile(j, './output/' + str(i + 1) + '/' + output_name)

'''
usage:
merge subdirs into specific dir number
e.g: input: Master.MR.RE/mrf_data/24/multiple dirs  output: 1/ 2/
'''
sub_dir_list = []
split_dir_num = 2

def flatten_directories(path):
    for root, dirs, files in os.walk(path):
        sub_dir = root.split('/')
        if len(sub_dir) == 6:
            sub_dir_list.append(root)
    for i in range(split_dir_num):
        output_path = './output/' + str(i + 1)
        if not os.path.exists(output_path):
            os.makedirs(output_path)

    for i in range(split_dir_num):
        result_list = sub_dir_list[math.floor(i / split_dir_num * len(sub_dir_list)) : math.floor((i + 1) / split_dir_num * len(sub_dir_list))]
        for j in result_list:
            for root, dirs, files in os.walk(j):
                for filename in files:
                    print(os.path.join(root, filename))
                    output_name = '-'.join(os.path.join(root, filename).split('/')[2:])
                    copyfile(os.path.join(root, filename), './output/' + str(i + 1) + '/' + output_name)


if __name__ == '__main__':
    flatten_directories('./input')
