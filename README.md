# 🧠 Breast Cancer Detection Using Deep Learning

This is a **Flask-based deep learning web application** that detects breast cancer from histopathological images using a trained Convolutional Neural Network (CNN) model.

---

### 👥 Made by - Group: SI-24556-1744082820

**Group Members:**
- Sohil S Philip (22BCE10358) [Group Leader] — 📧 sohilphilip2022@vitbhopal.ac.in
- Nimish Rao (22BAI10054) — 📧 nimishrao2022@vitbhopal.ac.in
- Priyansh Rathore (22BCY10248) — 📧 priyanshrathore2022@vitbhopal.ac.in
- Rekhansh Raje Deshmukh (22BCY10085) — 📧 rekhanshrajedeshmukh2022@vitbhopal.ac.in

---

## 🔍 Features

- Upload histopathological images (`.jpg`, `.png`).
- Predicts whether the tumor is **Benign** or **Malignant**.
- Displays prediction with **confidence percentage**.
- Displays the **uploaded image** in the center.
- **Clear** button to remove the image and prediction.

---

## 🧠 Model

The model is a CNN trained using **Keras/TensorFlow** on over **270,000+ labeled images** of breast cancer tissue.

**Model File**:  
📦 `Flask/breastcancer.h5` (included)

---

## 📂 Project Structure

```
breastcancer-detection/
├── breastcancerdataset/           # (Not uploaded due to size)
│   ├── train/
│   │   ├── benign/
│   │   └── malignant/
│   └── test/
│       ├── benign/
│       └── malignant/
│
├── Flask/
│   ├── app.py
│   ├── breastcancer.h5
│   ├── templates/
│   │   └── bcancer.html
│   ├── static/
│   │   └── images/
│   └── uploads/                  # Stores uploaded images temporarily
│
├── Breast-Training.ipynb         # Model training notebook
├── Breast-Testing.ipynb          # Model evaluation notebook
├── prepare-dataset.ipynb         # Preprocessing and dataset setup

├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Running the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/breastcancer-detection.git
cd breastcancer-detection/Flask
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Flask Server

```bash
python app.py
```

### 4. Open the App in Your Browser

Go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📁 Dataset Instructions

The dataset is **not included** in this repo due to its large size.

### 👉 Setup the Dataset:

1. **Download** the dataset from:  
   [🔗 Kaggle - Breast Histopathology Images](https://www.kaggle.com/paultimothymooney/breast-histopathology-images)

2. **Extract** the archive and rename the extracted folder to:  
   `Breast Histopathology Images`

3. Open `prepare-dataset.ipynb` and update the **source path** with the location of the extracted dataset.

4. Create a new folder named `breastcancerdataset/` inside your project root.

5. Run all cells in `prepare-dataset.ipynb` to split and organize the dataset into `train/` and `test/` folders.

✅ Your dataset is now ready for training and testing!
