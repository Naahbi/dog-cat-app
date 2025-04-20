import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model('my_model.keras')


def preprocess(img):
    img = img.convert("RGB").resize((150, 150))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def predict_image(image_file):
    img = Image.open(image_file)
    x = preprocess(img)
    pred = model.predict(x)[0][0]
    label = "cane" if pred>0.5 else "gatto"
    return {"label:":label, "confidance:": round(float(pred), 2)}
