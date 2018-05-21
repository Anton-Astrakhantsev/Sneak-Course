import os
import threading
import subprocess as sp

check = []
image_list = os.listdir('Source')


def resizer(inp):
    if inp not in check:
        check.append(inp)
        way_s = os.path.join('Source', inp)
        way_r = os.path.join('Result', inp)
        res = sp.Popen('magick convert {} -resize 200 {}'.format(way_s, way_r))
        res.communicate()
        t = threading.currentThread().getName()
        print("Выполнен процесс номер {}".format(t))


def checker():
    if len(check) == 4:
        for image in image_list:
            if image not in check:
                resizer(image)


def super_resizer(n):
    inp = image_list[n]
    resizer(inp)
    checker()


for i in range(4):
    thread = threading.Thread(target=super_resizer, args=(i,))
    thread.start()
