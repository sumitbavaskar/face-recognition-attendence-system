import tkinter as tk
from tkinter import messagebox

class ExitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exit Application")
        self.root.geometry("300x150")
        self.root.resizable(False, False)

        # Label
        # label = tk.Label(root, text="Are you sure you want to exit?", font=("Arial", 12))
        # label.pack(pady=20)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        yes_button = tk.Button(button_frame, text="Yes", width=10, command=self.exit_app)
        yes_button.pack(side=tk.LEFT, padx=5)

        no_button = tk.Button(button_frame, text="No", width=10, command=self.root.destroy)
        no_button.pack(side=tk.LEFT, padx=5)

    def exit_app(self):
        if messagebox.askyesno("Confirm Exit", "Do you really want to exit?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExitApp(root)
    root.mainloop()