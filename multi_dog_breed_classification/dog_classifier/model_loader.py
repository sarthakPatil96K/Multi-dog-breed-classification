import tensorflow as tf
import os

MODEL_PATH = os.path.join("static", "models", "model_files/mobilenetv2_model.h5")
model = tf.keras.models.load_model(MODEL_PATH)

def get_model():
    return model
