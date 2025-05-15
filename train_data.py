import os
import face_recognition
import pickle
from tkinter import *
from tkinter import messagebox

class TrainData:
    def __init__(self, root):
        self.root = root
        self.root.title("Train Data")
        self.root.geometry("400x200")

        self.train_button = Button(root, text="Train Data", command=self.train_data, font=("Arial", 14))
        self.train_button.pack(pady=50)

    def train_data(self):
        print("Train data button clicked")  # Debugging statement
        known_faces = []
        known_names = []

        for student_id in os.listdir("data"):
            for image_name in os.listdir(f"data/{student_id}"):
                image_path = f"data/{student_id}/{image_name}"
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                if encodings:
                    encoding = encodings[0]
                    known_faces.append(encoding)
                    known_names.append(student_id)

        with open("trained_data.pkl", "wb") as f:
            pickle.dump((known_faces, known_names), f)

        messagebox.showinfo("Info", "Training completed and data saved")