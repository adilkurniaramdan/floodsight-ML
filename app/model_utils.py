import numpy as np
from keras.src.saving import load_model


def load_trained_model(model_path='models/fine_tuned_flood_detection_model.keras'):
    model = load_model(model_path)
    return model

def predict(model, preprocessed_image):
    predictions = model.predict(preprocessed_image)
    labels = ['Flooding', 'No Flooding']
    result_index = np.argmax(predictions)
    return f"({result_index + 1}) {labels[result_index]}"