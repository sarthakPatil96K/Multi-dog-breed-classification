import os
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from django.conf import settings

# Path to the model file
MODEL_PATH = os.path.join(
    settings.BASE_DIR, 'dog_classifier', 'model_files',
    '20250815-073348-mobilenetv2_models.keras'
)

# Verify model presence
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Please add it.")

# Class labels (must match training order)
class_labels = [
    "affenpinscher", "afghan_hound", "african_hunting_dog", "airedale",
    "american_staffordshire_terrier", "appenzeller", "australian_terrier", "basenji",
    "basset", "beagle", "bedlington_terrier", "bernese_mountain_dog",
    "black-and-tan_coonhound", "blenheim_spaniel", "bloodhound", "bluetick",
    "border_collie", "border_terrier", "borzoi", "boston_bull", "bouvier_des_flandres",
    "boxer", "brabancon_griffon", "briard", "brittany_spaniel", "bull_mastiff",
    "cairn", "cardigan", "chesapeake_bay_retriever", "chihuahua", "chow", "clumber",
    "cocker_spaniel", "collie", "curly-coated_retriever", "dandie_dinmont", "dhole",
    "dingo", "doberman", "english_foxhound", "english_setter", "english_springer",
    "entlebucher", "eskimo_dog", "flat-coated_retriever", "french_bulldog",
    "german_shepherd", "german_short-haired_pointer", "giant_schnauzer",
    "golden_retriever", "gordon_setter", "great_dane", "great_pyrenees",
    "greater_swiss_mountain_dog", "groenendael", "ibizan_hound", "irish_setter",
    "irish_terrier", "irish_water_spaniel", "irish_wolfhound", "italian_greyhound",
    "japanese_spaniel", "keeshond", "kelpie", "kerry_blue_terrier", "komondor",
    "kuvasz", "labrador_retriever", "lakeland_terrier", "leonberg", "lhasa",
    "malamute", "malinois", "maltese_dog", "mexican_hairless", "miniature_pinscher",
    "miniature_poodle", "miniature_schnauzer", "newfoundland", "norfolk_terrier",
    "norwegian_elkhound", "norwich_terrier", "old_english_sheepdog", "otterhound",
    "papillon", "pekinese", "pembroke", "pomeranian", "pug", "redbone",
    "rhodesian_ridgeback", "rottweiler", "saint_bernard", "saluki", "samoyed",
    "schipperke", "scotch_terrier", "scottish_deerhound", "sealyham_terrier",
    "shetland_sheepdog", "shih-tzu", "siberian_husky", "silky_terrier",
    "soft-coated_wheaten_terrier", "staffordshire_bullterrier", "standard_poodle",
    "standard_schnauzer", "sussex_spaniel", "tibetan_mastiff", "tibetan_terrier",
    "toy_poodle", "toy_terrier", "vizsla", "walker_hound", "weimaraner",
    "welsh_springer_spaniel", "west_highland_white_terrier", "whippet",
    "wire-haired_fox_terrier", "yorkshire_terrier"
]

# Model loading using KerasLayer for tf-hub layers
model = tf.keras.models.load_model(
    MODEL_PATH, custom_objects={"KerasLayer": hub.KerasLayer}
)

# Preprocessing function
def preprocess_image(img_path, target_size=(224, 224)):
    img = tf.io.read_file(img_path)
    img = tf.io.decode_image(img, channels=3, expand_animations=False)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = tf.image.resize(img, target_size)
    img = np.expand_dims(img.numpy(), axis=0)  # Add batch dimension
    return img

# Breed prediction function
def predict_breed(img_path, top_k=3):
    img_array = preprocess_image(img_path)
    preds = model.predict(img_array)[0]
    top_indices = preds.argsort()[-top_k:][::-1]
    results = [
        {"breed": class_labels[i], "confidence": float(preds[i])}
        for i in top_indices
    ]
    return results

# Django view-compatible wrapper
def classify_image(img_path, top_k=3):
    predictions = predict_breed(img_path, top_k)
    
    # Create a short explanation string from the top prediction
    if predictions:
        explanation = f"Top prediction: {predictions[0]['breed']} ({predictions[0]['confidence']*100:.2f}%)"
    else:
        explanation = "No predictions available."
    
    return predictions, explanation


# pip install tensorflow==2.19.0 keras==3.10.0 tensorflow-hub==0.16.1
# TF version:  2.19.0
# TF hub version: 0.16.1
# Keras version: 3.10.0
