from keras.models import load_model, Model
import input
import plot
import numpy as np
from sklearn.cluster import KMeans
from sklearn.random_projection import SparseRandomProjection

N_CLUSTER = 50

def main():
    autoencoder = load_model('model.h5')
    model = Model(inputs = autoencoder.input,
                  outputs = autoencoder.get_layer('max_pooling2d_3').output)

    X = []
    apps = []

    json = input.load_json('res2.json')
    #json = input.load_json('min_ht.json')
    for entry in json:
        name = entry['app_name']
        path = entry['images'][0]['path']
        x = input.read_img(path)
        x = x.astype('float32') / 255.
        x = np.expand_dims(x, axis=0)
        y = model.predict(x)
        y = y.flatten()
        X.append(y)
        apps.append({"path":path})

    rp = SparseRandomProjection(n_components=2, random_state=42)
    X_projected = rp.fit_transform(X)
    for (app, point) in zip(apps, X_projected):
        app["point"] = point
    plot.plot(apps)

main()
