import os
import subprocess as sp

way = os.path.dirname(__file__)
os.mkdir(path=os.path.join(way, 'Result')) # Фактически это нужно закомментить, после первого использования программы


def resizer(inp):
    way_s = os.path.join('Source', inp)
    way_r = os.path.join('Result', inp)
    sp.run('magick convert {} -resize 200 {}'.format(way_s, way_r))


image_list = os.listdir('Source')

for i in image_list:
    resizer(i)
