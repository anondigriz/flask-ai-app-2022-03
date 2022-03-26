import tensorflow as tf
from ai_application import app
import numpy as np

IMAGE_SHAPE = (224, 224)
reloaded = tf.keras.models.load_model(app.config['RECOGNIZER_MODEL'])
normalization_layer = tf.keras.layers.Rescaling(1./255)
class_names = np.array(
    ['маргаритка', 'одуванчик', 'розы', 'подсолнухи', 'тюльпаны'])


def recognize(full_path):
    pass