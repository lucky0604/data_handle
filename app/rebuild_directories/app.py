#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
from shutil import copyfile

def rebuild_directories(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            folder_path = '/'.join(filename.split('-')[:len(filename.split('-')) - 1])
            output_file = filename.split('-')[-1]
            print(folder_path)
            if os.path.exists('./output_bak/' + folder_path) == False:
                os.makedirs('./output_bak/' + folder_path)
            copyfile(os.path.join(root, filename), os.path.join('./output_bak/' + folder_path, output_file))


if __name__ == '__main__':
    rebuild_directories('./input')
