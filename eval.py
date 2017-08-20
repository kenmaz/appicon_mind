from keras.models import load_model, Model
import input
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk

def fetch_single_input():
    x, _ = input.read('min_ht.json')
    x = x[2]
    #show(x)
    Image.fromarray(x).save('img-input.png')
    x = x.astype('float32') / 255.
    x = np.expand_dims(x, axis=0)
    print(x.shape)
    return x

def main():
    model = load_model('model.h5')
    print(model)

    from keras.utils import plot_model
    plot_model(model, to_file='model.png', show_shapes=True)

    x = fetch_single_input()
    y = model.predict(x)
    print(y.shape)
    y = y * 255
    print(y.shape)
    show(y[0])

def intermediate():
    model = load_model('model.h5')
    inter = Model(inputs=model.input,
                  outputs=model.get_layer('max_pooling2d_3').output)

    x = fetch_single_input()
    res = inter.predict(x)
    res = res * 255
    print(res.shape) #(1, 20, 20, 8)
    res = np.transpose(res[0])
    print(res.shape) #(1, 20, 20, 8)
    for i, img in enumerate(res):
        img = np.transpose(img)
        out = Image.fromarray(img).convert('RGB')
        out.save('img-%d.png' % i)

    res = model.predict(x)
    res = res * 255
    print(res.shape) #(1, 160, 160, 3)
    res = np.transpose(res[0])
    print(res.shape) #(3, 160, 160)
    img = np.transpose(res)
    out = Image.fromarray(np.uint8(img)).convert('RGB')
    out.save('img-out.png')

    for i, img in enumerate(res):
        img = np.transpose(img)
        out = Image.fromarray(img).convert('RGB')
        out.save('img-out-%d.png' % i)



def show(img):
    img = Image.fromarray(np.uint8(img))
    root = tk.Tk()
    tkimage = ImageTk.PhotoImage(img)
    tk.Label(root, image=tkimage).pack()
    root.mainloop()

#main()
intermediate()
