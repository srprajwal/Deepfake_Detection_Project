# Identification of Fake Faces using Deep Learning  

## 📌 Overview  
With the rise of deep learning and increasing computational power, the ability to generate hyper-realistic deepfake images and videos has become a major concern. This project aims to identify AI-generated fake faces using a deep learning-based approach combining ResNeXt CNNs for feature extraction and LSTM-based RNNs for temporal analysis.  

## 🚀 Features  
- Deepfake detection using **ResNeXt CNNs + LSTM**  
- Trained on **FaceForensics++, Deepfake Detection Challenge, and Celeb-DF** datasets  
- **High accuracy** in distinguishing real vs. fake faces  
- Backend API for processing video frames  
- Web-based user interface for easy detection  

## 🛠️ Tech Stack  
- **Python**  
- **PyTorch**  
- **OpenCV**  
- **Django** 

## 📊 Datasets
The model is trained and evaluated using:
- [FaceForensics++](https://github.com/ondyari/FaceForensics)  
- [Deepfake Detection Challenge](https://www.kaggle.com/c/deepfake-detection-challenge)  
- [Celeb-DF (v2)](https://www.kaggle.com/datasets/reubensuju/celeb-df-v2)  

## ⚙️ Installation & Usage  

### 1️⃣ Clone Repository   
```bash
git clone https://github.com/srprajwl/Identification-of-Fake-Faces.git  
cd Identification-of-Fake-Faces
```
### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
### 3️⃣ Activate the Virtual Environment
```bash
source venv/bin/activate
```
### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 5️⃣ Run the Django Development Server
```bash
python manage.py runserver
```


