import keras
import numpy as np
from PIL import Image
from keras_preprocessing import image

from config import Config


def preprocess_image(image_stream):
    img = Image.open(image_stream)
    img = img.resize(Config.IMAGE_SIZE)
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)
