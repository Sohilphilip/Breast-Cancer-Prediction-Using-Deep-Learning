import os
import numpy as np
from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load the trained model
model = load_model(r'breastcancer.h5')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print("Received POST request")  # Debug line
        file = request.files['image']
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Image preprocessing
        img = image.load_img(filepath, target_size=(50, 50))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)[0][0]
        predicted_label = "Malignant" if prediction > 0.5 else "Benign"
        confidence = round(float(prediction) * 100, 2) if prediction > 0.5 else round(float(1 - prediction) * 100, 2)

        return render_template("bcancer.html", label=predicted_label, confidence=confidence, image_file=filename)

    return render_template("bcancer.html", label=None, confidence=None, image_file=None)

if __name__ == '__main__':
    app.run(debug=True)
