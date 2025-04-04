
# Face Recognition Attendance System

This is a Python-based attendance system that uses real-time face recognition to identify known individuals from a webcam and logs their attendance in a date-specific CSV file.

## 🚀 Features
- Real-time face detection using webcam
- Recognizes multiple known faces
- Automatically logs name and time to a CSV file
- Visual feedback with name overlay in OpenCV window
- One-time attendance per person per session

## 🛠️ Requirements
- Python 3.7+
- OpenCV
- face_recognition
- numpy

Install dependencies:
```bash
pip install opencv-python face_recognition numpy
```

## 📁 Folder Structure
```
FaceRecogSystem/
├── Faces/
│   ├── messi.png
│   └── ronaldo.png
├── facerecog.py
└── Attendance_XX-XX-XXXX.csv  # Generated automatically
```

## ▶️ How to Run
```bash
python facerecog.py
```

- Press `q` to quit the app.
- The attendance will be saved in a file named `Attendance_DD-MM-YYYY.csv`.

## 📌 Notes
- Make sure to add known face images in the `Faces/` folder and update the script accordingly.
- Ensure good lighting for better accuracy.

## ⭐ Rating
**Project Complexity:** ★★★☆☆  
**Usefulness:** ★★★★★  
**Learning Value:** ★★★★★

## 📸 Sample Output
- Frame with recognized faces
- CSV file with:
  ```
  Name, Time
  Messi, 09:01:14
  Ronaldo, 09:03:02
  ```

---

Built with ❤️ using Python and OpenCV.

