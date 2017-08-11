#coding:utf-8

import json
from PIL import Image, ImageTk
import tkinter as tk
import numpy as np

def read():
    img_root = 'crawler/crawler/imgs/'
    path = 'crawler/crawler/min_ht.json'
    f = open(path, 'r')
    jsonData = json.load(f)
    imgs = [img_root + x['images'][0]['path'] for x in jsonData]
    print('imgs',len(imgs))
    f.close()
    th = int(len(imgs)*6/10)
    train = np.array([read_img(x) for x in imgs[0:th]])
    test =  np.array([read_img(x) for x in imgs[th+1:]])
    return train, test

def read_img(path):
    print('read_img => ',path)
    img = Image.open(path, 'r')
    resized = img.resize((160, 160))
    return np.asarray(resized)

def main():
    (train, test) = read()
    print('train',len(train))
    print('test',len(test))
    print(train.shape)
    x = train[0]
    print(x[0][0])
    print(x[80][80])
    x = x.astype('float32') / 255.
    print(x.shape)
    print(x[80][80])

def show(img):
    img = Image.fromarray(np.uint8(img))
    root = tk.Tk()
    tkimage = ImageTk.PhotoImage(img)
    tk.Label(root, image=tkimage).pack()
    root.mainloop()

if __name__ == '__main__':
    main()
