from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = load_model('mnist_model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file'].read()
    image = Image.open(io.BytesIO(file)).convert('L')
    image = image.resize((28, 28))
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape(1, 28, 28)
    
    prediction = model.predict(image_array)
    predicted_digit = str(np.argmax(prediction))
    
    return jsonify({'digit': predicted_digit})

if __name__ == '__main__':
    app.run(debug=True)