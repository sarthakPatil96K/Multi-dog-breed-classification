# 🐶 Multi-Dog Breed Classification using MobileNetV2

This project focuses on building a deep learning model to classify images of dogs into **120 different breeds** using the [Kaggle Dog Breed Identification Dataset](https://www.kaggle.com/competitions/dog-breed-identification). The model leverages **Transfer Learning** using **MobileNetV2**, which is lightweight and optimized for mobile and embedded vision applications.

---

## 📂 Dataset

- The dataset contains high-quality images of dogs classified into **120 unique breeds** including:
  affenpinscher, afghan_hound, african_hunting_dog, airedale,
  american_staffordshire_terrier, appenzeller, australian_terrier, ...

- Total classes: **120**
- Source: Kaggle's Dog Breed Identification Competition

---

## 🧠 Model Architecture

- **Base Model:** [MobileNetV2](https://arxiv.org/abs/1801.04381) (`imagenet` pretrained weights)
- **Customization:** Added Global Average Pooling + Dense layers for classification
- **Activation:** Softmax
- **Loss Function:** Categorical Crossentropy
- **Optimizer:** Adam
- **Input Shape:** 224 x 224 x 3 (RGB images)

---

## ⚙️ Training Details

- **Framework:** TensorFlow / Keras
- **Training Samples:** ~10,000
- **Validation Split:** 80:20
- **Epochs:** 100
- **Batch Size:** 32
- **Augmentation:** Applied `ImageDataGenerator` for real-time data augmentation (flip, zoom, shift)
- **Compute Used:** Google Colab (CPU/GPU)

---

## 📊 Evaluation Metrics

- **Accuracy**
- **Top-5 Accuracy**
- **Loss Curve**
- **Confusion Matrix (optional)**
- **Breed-wise prediction probability plots**

---

## 📈 Results

- Achieved satisfactory training and validation accuracy
- Model generalizes well across various dog breeds
- Confident breed predictions visualized using bar plots

---

## 📦 Saved Artifacts

- Trained model weights (`.h5` or `.keras`)
- Class label encoder (`class_names.npy`)
- Preprocessed test/val image sets

---

## 🖼️ Sample Predictions

- Visual outputs showing original dog image alongside:
- Predicted breed
- Top prediction probabilities
- True breed (highlighted)

---

## 🚀 Future Work

- Optimize model using pruning or quantization
- Convert to TensorFlow Lite for mobile deployment
- Add web/streamlit interface for user uploads
- Handle breed mixes and unknown breeds with thresholding

---

## 🛠️ Requirements

```bash
tensorflow>=2.9
matplotlib
numpy
pandas
scikit-learn
