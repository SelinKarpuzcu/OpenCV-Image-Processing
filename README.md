# 🧠 OpenCV Image Processing & Face Recognition System

This repository contains my structured implementations while learning 
Image Processing and Computer Vision using OpenCV.

It includes fundamental image operations, advanced processing techniques, and a complete end-to-end Face Detection & Recognition pipeline.

---

## 📌 Project Scope

The project is organized into progressive modules:

- 🟢 Basics
- 🔵 Advanced Image Processing
- 🟣 Face Detection & Recognition

---

## 🛠 Technologies

- Python
- OpenCV (opencv-contrib-python)
- NumPy
- Haar Cascade Classifier (local XML file)
- LBPH Face Recognizer

---

## 📂 Project Structure

OpenCV-Image-Processing/
│
├── Basics/          # Fundamental OpenCV operations
├── Advanced/        # Advanced image processing techniques
├── Faces/           # Face detection & recognition system
│   ├── face_detect.py
│   ├── face_recognition.py
│   ├── face_train.py
│   ├── face_trained.yml
│   └── haarcascade_face.xml
│
├── Resources/        # Images & dataset
│
├── venv/             # Virtual environment (excluded from Git)
├── requirements.txt
└── README.md

---

## 🟢 Basics Module

- Reading Images & Videos
- Drawing & Text
- Transformations
- Thresholding
- Contour Detection

---

## 🔵 Advanced Module

- Color Spaces
- Color Channels
- Blurring
- Gradients & Edge Detection
- Masking
- Histogram Computation
- Bitwise Operations

---

## 🟣 Face Module

### Face Detection
- Haar Cascade Classifier

### Face Recognition
- LBPH Face Recognizer
- Custom trained model
- Organized training & validation dataset

---

## ⚙️ Setup

Clone the repository:

```bash
git clone <your-repository-link>
cd OpenCV-Image-Processing

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

---

## 👩‍💻 Author

Selin Karpuzcu  
Computer Engineering Student  
Focused on Artificial Intelligence & Computer Vision
