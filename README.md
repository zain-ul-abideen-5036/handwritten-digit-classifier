# Handwritten Digit Classification System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-brightgreen)

A complete end-to-end system for classifying handwritten digits using deep learning, featuring a web-based interface and REST API.
---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
---

## Overview
This project implements a convolutional neural network (CNN) trained on the MNIST dataset to recognize handwritten digits (0-9). The system includes:

- A Keras/TensorFlow deep learning model
- Flask-based REST API
- Interactive web interface
- Model training/evaluation scripts
- Preprocessing pipeline

Achieves 97.5%+ accuracy on test data while maintaining real-time prediction capabilities.
---

## Features

### Technical Features
- Model Training Pipeline
- Data Preprocessing Utilities
- REST API Endpoints
- Web Interface with Canvas Drawing
- Cross-Origin Resource Sharing (CORS) Support
- Error Handling and Input Validation

### User Features
- Real-time digit prediction
- Interactive drawing canvas
- Mobile-responsive design
- Clear/reset functionality
- Prediction confidence display
- Drag-and-drop image support
---

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup

### Clone repository
```bash
git clone https://github.com/zain-ul-abideen-5036/handwritten-digit-classifier.git
cd handwritten-digit-classifier
```

### Create virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies
```
pip install -r requirements.txt
```
---

## Usage

### Model Training
```bash
python train.py
```

### Start Web Server
```bash
python app.py
```

Access the web interface at ```http://localhost:5000```

### API Endpoint
```bash
POST /predict
Content-Type: multipart/form-data

curl -X POST -F "file=@digit.png" http://localhost:5000/predict
```
---

## Project Structure
```
handwritten-digit-classifier/
├── app.py                                          - Flask application entry point
├── HandwrittenDigitClassification.ipnyb            - Model training script
├── mnist_model.h5                                  - Pretrained model weights
├── requirements.txt                                - Dependency list
├── README.md                                       - Project documentation
│
└── templates/                                      - Frontend templates
   └── index.html                                   - Main interface
```

---

## Contact
For questions or feedback, contact: abideen5036@gmail.com
---
