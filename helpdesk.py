import tkinter as tk
from tkinter import messagebox

class HelpDeskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Help Desk")
        self.root.geometry("500x400")
        self.root.configure(bg="#1e1e1e")

        # Title
        title_label = tk.Label(root, text="Help Desk", font=("Arial", 24, "bold"), bg="#1e1e1e", fg="red", pady=20)
        title_label.pack()

        # Instructions
        instruction_label = tk.Label(root, text="Please fill out the form below to submit your help request.", font=("Arial", 12), bg="#1e1e1e", fg="#ffffff", pady=10)
        instruction_label.pack()

        # Form Frame
        form_frame = tk.Frame(root, bg="#1e1e1e")
        form_frame.pack(pady=20)

        # Name Field
        name_label = tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#1e1e1e", fg="#ffffff")
        name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Email Field
        email_label = tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#1e1e1e", fg="#ffffff")
        email_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.email_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        # Issue Field
        issue_label = tk.Label(form_frame, text="Issue:", font=("Arial", 12), bg="#1e1e1e", fg="#ffffff")
        issue_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.issue_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.issue_entry.grid(row=2, column=1, padx=10, pady=10)

        # Description Field
        description_label = tk.Label(form_frame, text="Description:", font=("Arial", 12), bg="#1e1e1e", fg="#ffffff")
        description_label.grid(row=3, column=0, padx=10, pady=10, sticky="nw")
        self.description_text = tk.Text(form_frame, font=("Arial", 12), width=30, height=5)
        self.description_text.grid(row=3, column=1, padx=10, pady=10)

        # Submit Button
        submit_button = tk.Button(root, text="Submit", font=("Arial", 12, "bold"), bg="#4CAF50", fg="#ffffff", command=self.submit_request)
        submit_button.pack(pady=20)

    def submit_request(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        issue = self.issue_entry.get()
        description = self.description_text.get("1.0", tk.END).strip()

        if not name or not email or not issue or not description:
            messagebox.showwarning("Incomplete Form", "Please fill out all fields before submitting.")
            return
        
        # Here you would normally send this data to a server or save it to a file/database
        # For demonstration purposes, we'll just show a confirmation message
        messagebox.showinfo("Request Submitted", "Your help request has been submitted successfully!")
        self.clear_form()

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.issue_entry.delete(0, tk.END)
        self.description_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = HelpDeskApp(root)
    root.mainloop()