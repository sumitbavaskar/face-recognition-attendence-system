import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv

class AttendanceManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        self.root.geometry("800x600")

        # Set initial background image
        self.load_background_image(r"D:\face recognisation system\college_picture\Standard2.jpg")

        # Bind the resize event
        self.root.bind('<Configure>', self.resize_background)

        # Title label
        self.title_label = tk.Label(root, text="Attendance Management System", font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#333333")
        self.title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Frame for Treeview
        frame = tk.Frame(root, padx=20, pady=20, bg="#ffffff", relief=tk.RIDGE, bd=2)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9, relheight=0.65)

        # Treeview widget
        self.tree = ttk.Treeview(frame, columns=("sr_no", "name", "date", "time"), show="headings")
        self.tree.heading("sr_no", text="Sr. No")
        self.tree.heading("name", text="Name")
        self.tree.heading("date", text="Date")
        self.tree.heading("time", text="Time")
        self.tree.column("sr_no", anchor=tk.CENTER, width=50)
        self.tree.column("name", anchor=tk.W, width=200)
        self.tree.column("date", anchor=tk.W, width=150)
        self.tree.column("time", anchor=tk.W, width=150)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Add buttons with better styling and spacing
        button_frame = tk.Frame(root, bg="#ffffff")
        button_frame.place(relx=0.3, rely=0.88, anchor=tk.CENTER)

        self.show_button = tk.Button(button_frame, text="Show", command=self.show_data, font=("Helvetica", 15), bg="#4CAF50", fg="#ffffff", padx=20, pady=5)
        self.show_button.grid(row=0, column=0, )

        button_frame = tk.Frame(root, bg="#ffffff")
        button_frame.place(relx=0.7, rely=0.88, anchor=tk.CENTER)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_data, font=("Helvetica", 15), bg="#f44336", fg="#ffffff", padx=20, pady=5)
        self.reset_button.grid(row=0, column=1, )

        # Footer label
        self.footer_label = tk.Label(root, text="© 2025 Attendance Management System", font=("Helvetica", 10), bg="#ffffff", fg="#333333")
        self.footer_label.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    def load_background_image(self, image_path):
        try:
            self.background_image = Image.open(image_path)
            self.background_photo = ImageTk.PhotoImage(self.background_image.resize((800, 600)))
            self.background_label = tk.Label(self.root, image=self.background_photo)
            self.background_label.place(relwidth=1, relheight=1)
            self.background_label.lower()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load background image: {e}")
            self.background_label = tk.Label(self.root, bg="#ffffff")
            self.background_label.place(relwidth=1, relheight=1)
            self.background_label.lower()

    def resize_background(self, event):
        new_width = event.width
        new_height = event.height
        resized_image = self.background_image.resize((new_width, new_height))
        self.background_photo = ImageTk.PhotoImage(resized_image)
        self.background_label.config(image=self.background_photo)

    def show_data(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Read data from CSV file
        try:
            with open("attendance.csv", "r") as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader, start=1):
                    self.tree.insert("", tk.END, values=(i, *row))
        except FileNotFoundError:
            messagebox.showerror("Error", "Attendance file not found.")

    def reset_data(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        messagebox.showinfo("Info", "Data has been reset.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceManagement(root)
    root.mainloop()