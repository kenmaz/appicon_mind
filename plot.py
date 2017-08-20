import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk

SIZE=17500
UNIT=175

def render(apps):
    raw = np.ones((SIZE + UNIT, SIZE + UNIT, 3))
    raw = raw * 255
    bg = Image.fromarray(np.uint8(raw))
    bg.save('test_bg.png')

    root = 'crawler/crawler/imgs/'
    for app in apps:
        (x, y) = app["pos"]
        path = root + app["path"]
        print(path, x, y)
        img = Image.open(path, 'r')
        img = img.resize((UNIT, UNIT))
        img.save('test_img.png')
        bg.paste(img, (x, y))

    bg.save('test.png')

def _plot(apps):
    image_file = 'crawler/crawler/imgs/' + apps[0]['path']
    image = plt.imread(image_file)
    fig, ax = plt.subplots()
    im = ax.imshow(image)
    plt.show()

def plot(apps):
    xs = [x["point"][0] for x in apps]
    ys = [x["point"][1] for x in apps]
    minx = min(xs)
    miny = min(ys)
    xs = [x - minx for x in xs]
    ys = [y - miny for y in ys]
    maxx = max(xs)
    maxy = max(ys)
    for app in apps:
        x = int(((app["point"][0] - minx) / maxx) * float(SIZE))
        y = int(((app["point"][1] - miny) / maxy) * float(SIZE))
        app['pos'] = (x,y)

    render(apps)

def main():
    data = [
            {
                'path': 'full/42d2b9d009f81cd10593aaa823f47d937c15b3b8.jpg',
                'point': [ -7.6592953,  10.7994513]
            },
            {
                'path': 'full/6587bebf032fbf7c95512befb9e04d55e335fe83.jpg',
                'point': [-10.1849019 ,  18.42361757]
            },
            {
                'path': 'full/e93edd93272d22df931c3be30592131bbcb741f5.jpg',
                'point': [-6.00715149,  2.81301448]
            }
           ]
    plot(data)

if __name__ == '__main__':
    main()
