#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIL import Image
import os

kelvin_table = {
    1000: (255,56,0),
    1500: (255,109,0),
    2000: (255,137,18),
    2500: (255,161,72),
    3000: (255,180,107),
    3500: (255,196,137),
    4000: (255,209,163),
    4500: (255,219,186),
    5000: (255,228,206),
    5500: (255,236,224),
    6000: (255,243,239),
    6500: (255,249,253),
    7000: (245,243,255),
    7500: (235,238,255),
    8000: (227,233,255),
    8500: (220,229,255),
    9000: (214,225,255),
    9500: (208,222,255),
    10000: (204,219,255)}

def convert_temp(image, temp):

    convert_image = Image.open(image)
    r, g, b = kelvin_table[temp]
    matrix = ( 255.0 / r, 0.0, 0.0, 0.0,
               0.0, 209.0 / g, 0.0, 0.0,
               0.0, 0.0, 163.0 / b, 0.0 )

    return convert_image.convert('RGB', matrix)

def change_temp(folder):
    for root, folder, filenames in os.walk(folder):
        for name in filenames:
            output_path = os.path.join('./output', root[8:])
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            print(output_path, ' --- output_bak path ---')
            after_image = convert_temp(os.path.join(root, name), 6000)
            after_image.save(output_path + '/'  + name, 'JPEG', quality = 90, optimize = True, progressive = False)

change_temp('./input')
