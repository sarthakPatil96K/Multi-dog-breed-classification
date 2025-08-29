# 🐶 Multi-Dog Breed Classification using MobileNetV2

This project focuses on building a deep learning model to classify images of dogs into **120 different breeds** using the [Kaggle Dog Breed Identification Dataset](https://www.kaggle.com/competitions/dog-breed-identification). The model leverages **Transfer Learning** using **MobileNetV2**, which is lightweight and optimized for mobile and embedded vision applications.

The project includes a **Django web application** that allows users to upload dog images and get breed predictions in real-time.

---

## 📂 Project Structure

```
multi-dog-breed-classification/
├── mult_dog_breed_classification/     # Django project root
│   ├── dog_classifier/                # Main Django app
│   ├── media/                         # Uploaded media files
│   ├── static/                        # Static files (CSS, JS, images)
│   │   ├── images/
│   │   ├── site.css
│   │   └── style.css
│   ├── templates/                     # HTML templates
│   │   ├── about.html
│   │   ├── base.html
│   │   ├── gallery.html
│   │   ├── index.html
│   │   └── model_info.html
│   ├── theme/                         # Django theme files
│   ├── db.sqlite3                     # SQLite database
│   └── manage.py                      # Django management script
├── venv/                              # Virtual environment
├── init.txt
└── README.md
```

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

## 🌐 Django Web Application

### Features:
- **Image Upload**: Users can upload dog images through a web interface
- **Real-time Prediction**: Instant breed classification results
- **Gallery View**: Browse previously classified images
- **Model Information**: Learn about the underlying ML model
- **Responsive Design**: Works on desktop and mobile devices

### Pages:
- **Home** (`index.html`): Main page with image upload functionality
- **Gallery** (`gallery.html`): Display of classified images
- **About** (`about.html`): Project information and details
- **Model Info** (`model_info.html`): Technical details about the ML model

---

## 🚀 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd multi-dog-breed-classification
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   cd mult_dog_breed_classification
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

---

## 📊 Evaluation Metrics

- **Accuracy**
- **Top-5 Accuracy**
- **Loss Curve**
- **Confusion Matrix (optional)**
- **Breed-wise prediction probability plots**

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

## 🔮 Future Work

- Optimize model using pruning or quantization
- Convert to TensorFlow Lite for mobile deployment
- Add user authentication and image history
- Handle breed mixes and unknown breeds with thresholding
- Deploy to cloud platform (AWS/Heroku)

---

## 🛠️ Requirements

```bash
Django>=4.0
tensorflow>=2.9
matplotlib
numpy
pandas
scikit-learn
Pillow
```

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/your-username/multi-dog-breed-classification/issues).

---
 