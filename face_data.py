import cv2
import os
from tkinter import *
from tkinter import messagebox

class FaceData:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Data Collection")
        self.root.geometry("400x200")

        self.label = Label(root, text="Enter Student ID: ", font=("Arial", 14))
        self.label.pack(pady=10)

        self.student_id = StringVar()
        self.entry = Entry(root, textvariable=self.student_id, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.capture_button = Button(root, text="Capture Images", command=self.capture_images, font=("Arial", 14))
        self.capture_button.pack(pady=10)

    def capture_images(self):
        student_id = self.student_id.get()
        if not student_id:
            messagebox.showerror("Error", "Please enter a Student ID")
            return

        # Create directory for the student's images if it doesn't exist
        os.makedirs(f"data/{student_id}", exist_ok=True)

        cap = cv2.VideoCapture(0)
        count = 0

        while count < 30:  # Capture 30 images
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                count += 1
                face_img = frame[y:y+h, x:x+w]
                cv2.imwrite(f"data/{student_id}/{student_id}_{count}.jpg", face_img)

            cv2.imshow("Capturing Images", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Info", f"Captured {count} images for Student ID: {student_id}")