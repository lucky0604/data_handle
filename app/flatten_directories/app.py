#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import math
from shutil import copyfile

output_dir_num = 4
files_arr = []

def flatten_directories(path):
    for root, dirs, files in os.walk(path):

        for i in range(output_dir_num):
            output_path = './output/' + str(i + 1)
            if os.path.exists(output_path) == False:
                os.makedirs(output_path)
        for filename in files:
            files_arr.append(os.path.join(root, filename))

    for i in range(output_dir_num):
        result_list = files_arr[math.floor(i / output_dir_num * len(files_arr)) : math.floor((i + 1) / output_dir_num * len(files_arr))]
        for j in result_list:
            output_name = '-'.join(j.split('/')[2:])
            print(output_name)
            copyfile(j, './output/' + str(i + 1) + '/' + output_name)



if __name__ == '__main__':
    flatten_directories('./input')
