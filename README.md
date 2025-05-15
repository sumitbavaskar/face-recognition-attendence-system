
# Face Recognition Student Management System

A Python-based Face Recognition System for managing student attendance and information. Built with OpenCV, Tkinter, MySQL, and face recognition libraries, this project provides an efficient way to automate attendance tracking using facial biometrics.

## 📌 Features

- Face Detection and Recognition
- Real-time Attendance Logging
- Student Registration with Image Capture
- GUI Interface using Tkinter
- Data Stored in MySQL Database
- Image Dataset Generator

## 🛠️ Tech Stack

- Python
- OpenCV
- face_recognition
- Tkinter
- MySQL
- PIL (Python Imaging Library)

## 📥 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/face-recognition-system.git
   cd face-recognition-system
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Setup MySQL database:
   - Create a database named `face_recognition`.
   - Import the SQL script provided in the project (if available).
   - Update database credentials in the code (host, user, password).

4. Run the application:

   ```bash
   python main.py
   ```

## 📂 Project Structure

```
face-recognition-system/
│
├── dataset/                 # Stores captured face images
├── attendance/              # Stores attendance CSV logs
├── main.py                  # Main GUI application
├── train.py                 # Face training script
├── face_recognition.py      # Face recognition logic
├── student.py               # Student data registration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 🖼️ Screenshots

*Add screenshots of the UI here, if available.*

## ⚠️ Notes

- Make sure your webcam is functional.
- Train the model using captured face images before recognizing faces.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

*Developed by [Your Name].*
