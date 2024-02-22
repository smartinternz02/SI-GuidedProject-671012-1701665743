import re
import numpy as np
import os
from flask import Flask, app,request,render_template
from keras import models
from keras.models import load_model
from keras.preprocessing import image
from tensorflow.python.ops.gen_array_ops import concat
from keras.applications.inception_v3 import preprocess_input
import requests
from flask import Flask, request,render_template, redirect, url_for
from keras.utils import load_img, img_to_array
import tensorflow as tf

from PIL import Image

# Loading the model
model = load_model('C:\\Users\\Ganesh\\Desktop\\Major Project\\InceptionV3.h5')

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=["GET", "POST"])
def res():
    if request.method == "POST":
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'pred_files', f.filename)
        f.save(filepath)

        class_labels = ['negative', 'positive']

        img = Image.open(filepath)
        img = img.resize((227,227))
        x = np.array(img)
        x = np.expand_dims(x, axis=0)
        
        # preprocess the input image
        x = tf.keras.applications.inception_v3.preprocess_input(x)

        # Make predictions
        predictions = model.predict(x)
        predicted_class = np.argmax(predictions[0])
        predicted_label = class_labels[predicted_class]

        return render_template('classification.html', prediction=predicted_label)

if __name__ == '__main__':
    app.run(debug=True)

