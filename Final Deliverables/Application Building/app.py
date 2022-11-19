from flask import Flask, render_template, request
import os
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf

app = Flask(__name__)
model = load_model("mnistCNN.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize')
def recognize():
    return render_template('recognize.html')

@app.route('/predict', methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        basepath=os.path.dirname(__file__)
        filepath=os.path.join(basepath,'uploads', f.filename)
        f.save(filepath)
        img = image.load_img(filepath,target_size=(64,64))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis=0)
        pred = np.argmax(model.predict(x), axis=1)
        index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        text = "The classified text is: "+str(index[pred[0]])
    return text


if _name_ == '__main__':
    app.run(debug = True)


