import tensorflow as tf
from ai_application import app
import numpy as np
import PIL.Image as Image

IMAGE_SHAPE = (224, 224)
model = tf.keras.models.load_model(app.config['RECOGNIZER_MODEL'])
normalization_layer = tf.keras.layers.Rescaling(1./255)
class_names = np.array(
    ['маргаритка', 'одуванчик', 'розы', 'подсолнухи', 'тюльпаны'])


def recognize_flower(full_path):
    uploaded_image = Image.open(full_path).resize(IMAGE_SHAPE)
    normalized_uploaded_image = normalization_layer(uploaded_image)

    img_array = tf.keras.utils.img_to_array(normalized_uploaded_image)
    img_array = tf.expand_dims(img_array, 0)

    result_batch = model.predict(img_array)
    result_batch_id = tf.math.argmax(result_batch, axis=-1)

    prediction = class_names[result_batch_id]
    return prediction
