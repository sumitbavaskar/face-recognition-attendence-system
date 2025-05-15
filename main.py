from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from student import student
from attendence import AttendanceManagement
from face_detector import FaceDetector
from face_data import FaceData
from train_data import TrainData
from exit import ExitApp
from about import DeveloperInfoApp
from helpdesk import HelpDeskApp

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Face Recognition System")
        
        # Configure root window
        self.root.configure(bg="#f0f2f6")  # Light blue-gray background
        
        self.image_references = []

        # Modern style configuration
        style = ttk.Style()
        style.configure("Modern.TButton",
                    padding=10,
                    font=("Helvetica", 12),
                    background="#2196f3",
                    foreground="white")

        def load_image(path, size):
            try:
                img = Image.open(path)
                img = img.resize(size, Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.image_references.append(photo)
                return photo
            except Exception as e:
                print(f"Error loading image {path}: {e}")
                return None

        # Create main container
        main_container = Frame(self.root, bg="#f0f2f6")
        main_container.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Header Frame with gradient effect
        header_frame = Frame(main_container, bg="#1976d2", height=100)
        header_frame.pack(fill=X, pady=(0, 20))

        # Title with modern font and shadow effect
        title_frame = Frame(header_frame, bg="#1976d2")
        title_frame.pack(pady=20)
        
        title_label = Label(
            title_frame,
            text="SMART FACE RECOGNITION SYSTEM",
            font=("Helvetica", 36, "bold"),
            bg="#1976d2",
            fg="white"
        )
        title_label.pack()

        # Create card container
        card_container = Frame(main_container, bg="#f0f2f6")
        card_container.pack(fill=BOTH, expand=True)

        # Configure grid
        card_container.grid_columnconfigure((0,1,2,3), weight=1, pad=20)
        card_container.grid_rowconfigure((0,1), weight=1, pad=20)

        def create_card(image_path, text, command, row, column):
            # Card frame with shadow effect
            card_frame = Frame(
                card_container,
                bg="white",
                highlightbackground="#e0e0e0",
                highlightthickness=1,
            )
            card_frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

            # Add hover effect
            def on_enter(e):
                card_frame.configure(bg="#f5f5f5")
                card_button.configure(bg="#f5f5f5")
                
            def on_leave(e):
                card_frame.configure(bg="white")
                card_button.configure(bg="white")

            card_frame.bind("<Enter>", on_enter)
            card_frame.bind("<Leave>", on_leave)

            # Image
            photo = load_image(image_path, (120, 120))
            if photo:
                image_label = Label(
                    card_frame,
                    image=photo,
                    bg="white",
                    cursor="hand2"
                )
                image_label.pack(pady=(20,10))
                image_label.bind("<Button-1>", lambda e: command())

            # Button with modern design
            card_button = Button(
                card_frame,
                text=text,
                font=("Helvetica", 12, "bold"),
                bg="white",
                fg="#1976d2",
                bd=0,
                cursor="hand2",
                command=command,
                activebackground="#f5f5f5",
                activeforeground="#1976d2",
                width=20,
                height=2
            )
            card_button.pack(pady=(0,20))

        # Create cards for each function
        cards_data = [
            (r"D:\face recognisation system\college_picture\employee.jfif", "Student Management", self.student_details, 0, 0),
            (r"D:\face recognisation system\college_picture\face1.jpg", "Face Detection", self.face_detector, 0, 1),
            (r"D:\face recognisation system\college_picture\attend.jfif", "Attendance", self.Attendence, 0, 2),
            (r"D:\face recognisation system\college_picture\help.jpg", "Help Desk", self.helpdesk, 0, 3),
            (r"D:\face recognisation system\college_picture\manipulation.jpg", "Train Model", self.train_data, 1, 0),
            (r"D:\face recognisation system\college_picture\face_data.jfif", "Face Data", self.face_data, 1, 1),
            (r"D:\face recognisation system\college_picture\dev.jfif", "About Us", self.about, 1, 2),
            (r"D:\face recognisation system\college_picture\EXIT.jfif", "Exit", self.exit, 1, 3)
        ]

        for img_path, text, cmd, row, col in cards_data:
            create_card(img_path, text, cmd, row, col)

        # Status bar at bottom
        status_frame = Frame(main_container, bg="#1976d2", height=30)
        status_frame.pack(fill=X, side=BOTTOM, pady=(20,0))
        
        status_label = Label(
            status_frame,
            text="Ready",
            font=("Helvetica", 10),
            bg="#1976d2",
            fg="white"
        )
        status_label.pack(side=LEFT, padx=10)

    # Student Details Function
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    # Attendence Function
    def Attendence(self):
        self.new_window = Toplevel(self.root)
        self.app = AttendanceManagement(self.new_window)


    # Face Detection Function
    def face_detector(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceDetector(self.new_window)

    # Face Data Function
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceData(self.new_window)

    # Train Data Function
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = TrainData(self.new_window)

    # Exit  Function
    def exit(self):
        self.new_window = Toplevel(self.root)
        self.app = ExitApp(self.new_window)

    # About  Function
    def about(self):
        self.new_window = Toplevel(self.root)
        self.app = DeveloperInfoApp(self.new_window)
    
    # help Desk Function
    def helpdesk(self):
        self.new_window = Toplevel(self.root)
        self.app = HelpDeskApp(self.new_window)
    



if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
