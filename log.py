from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from main import FaceRecognitionSystem

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("800x600")

        # Background Image
        background_image = Image.open(r"D:\face recognisation system\college_picture\log.jpg")
        background_image = background_image.resize((1380, 800))
        self.bg_image = ImageTk.PhotoImage(background_image)

        bg_label = tk.Label(self.root, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        # Login Frame
        frame = tk.Frame(self.root, bg="#34495e", padx=20, pady=20, highlightbackground="white", highlightthickness=2)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Username:", font=("Arial", 14), bg="#34495e", fg="white").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(frame, font=("Arial", 14))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame, text="Password:", font=("Arial", 14), bg="#34495e", fg="white").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(frame, font=("Arial", 14), show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = tk.Button(frame, text="Login", font=("Arial", 14), bg="#1abc9c", fg="white", command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
           # messagebox.showinfo("Login Successful", "Welcome!")

            # Close login window
            self.root.destroy()

            # Open the main application
            main_root = tk.Tk()
            FaceRecognitionSystem(main_root)
            main_root.mainloop()

        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

# Running the login window
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
