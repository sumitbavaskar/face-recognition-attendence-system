import cv2
import face_recognition
import pickle
import os
import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import threading

class FaceDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Detector")
        self.root.geometry("800x600")
        
        # Title label
        title_label = tk.Label(root, text="Face Detector", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Start button
        start_button = tk.Button(root, text="Start Face Detection", font=("Arial", 14), command=self.start_recognition_thread)
        start_button.pack(pady=20)

        # Load trained data
        self.known_encodings, self.known_names = self.load_trained_data()

    def load_trained_data(self):
        if not os.path.exists("trained_data.pkl"):
            messagebox.showerror("Error", "trained_data.pkl not found. Train the model first.")
            return [], []  # Prevents crash if file is missing

        with open("trained_data.pkl", "rb") as file:
            try:
                known_encodings, known_names = pickle.load(file)
                return known_encodings, known_names
            except Exception as e:
                messagebox.showerror("Error", f"Error loading trained data: {e}")
                return [], []

    def start_recognition_thread(self):
        recognition_thread = threading.Thread(target=self.recognize_faces)
        recognition_thread.start()

    def recognize_faces(self):
        if not self.known_encodings:
            messagebox.showerror("Error", "No trained faces found. Please train your model first.")
            return

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            messagebox.showerror("Error", "Cannot access the webcam.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to capture image.")
                break

            # Resize frame for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding, face_location in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    matched_indexes = [i for i, match in enumerate(matches) if match]
                    best_match_index = matched_indexes[0]
                    name = self.known_names[best_match_index]

                top, right, bottom, left = [v * 4 for v in face_location]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                
                # Draw a label with the student ID above the face
                cv2.rectangle(frame, (left, top - 35), (right, top), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (left + 6, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

                # Check if 'P' key is pressed to mark attendance
                if cv2.waitKey(1) & 0xFF == ord('p'):
                    self.mark_attendance(name)

            cv2.imshow("Face Detector", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def mark_attendance(self, name):
        if name == "Unknown":
            return  # Do not record attendance for unknown faces

        with open("attendance.csv", "a", newline="") as file:
            writer = csv.writer(file)
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")
            writer.writerow([name, date, time])
            print(f"Attendance marked for {name} at {date} {time}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDetector(root)
    root.mainloop()