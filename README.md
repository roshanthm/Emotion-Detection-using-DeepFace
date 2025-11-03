# 🎯 Face Recognition & Emotion Detection System  

An intelligent computer vision project that combines **face recognition** and **emotion analysis** using the power of AI and deep learning.  
Built with **Python**, **OpenCV**, and **DeepFace**, this system identifies faces and detects emotions in real-time through your webcam.  

---

## 🚀 Features  

✅ **Face Recognition** — Matches real-time faces with reference images.  
✅ **Emotion Detection** — Detects emotions such as *happy, sad, angry, surprise, neutral, fear,* and *disgust.*  
✅ **Live Camera Feed** — Uses your webcam to analyze frames continuously.  
✅ **Deep Learning Models** — Uses pre-trained models from `DeepFace`.  
✅ **Automatic Model Caching** — Downloads models once and reuses them (no repeated downloads).  

---

## 🧠 How It Works  

1. The webcam captures video frames in real time.  
2. The system compares each detected face with reference images stored locally.  
3. It uses DeepFace’s emotion model to analyze the detected face and label emotions.  
4. Results are displayed live on the video feed.  

---

## 🧩 Technologies Used  

| Component | Description |
|------------|-------------|
| **Python** | Core programming language |
| **OpenCV** | Captures and processes video frames |
| **DeepFace** | Handles face recognition and emotion detection |
| **TensorFlow / Keras** | Backend deep learning framework |
| **NumPy & Pandas** | Data handling and numerical operations |

---

## 🛠️ Installation  

Clone the repository:  
```bash
git clone https://github.com/roshanthm/Face_Recognition_Emotion.git
cd Face_Recognition_Emotion
