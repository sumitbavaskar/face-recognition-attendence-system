import tkinter as tk

class DeveloperInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Developer Information")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e1e")
        
        # Maximizing the window
        self.root.state('zoomed')

        # Title
        title_label = tk.Label(root, text="Developers", font=("Arial", 36, "bold"), bg="#1e1e1e", fg="red", pady=20)
        title_label.pack()

        # College Information
        college_label = tk.Label(root, text="Moolji Jetha College Jalgaon", font=("Arial", 28, "bold"), bg="#282c34", fg="#61dafb", pady=20)
        college_label.pack(fill="x")

        # Developer Information Frame
        dev_info_frame = tk.Frame(root, bg="#1e1e1e")
        dev_info_frame.pack(pady=50)

        dev1_label = tk.Label(dev_info_frame, text="Shivam Vinod Chaudhari", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="#ffffff")
        dev1_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        dev1_contact = tk.Label(dev_info_frame, text="Contact: 9764635302", font=("Arial", 18), bg="#1e1e1e", fg="#61dafb")
        dev1_contact.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        dev2_label = tk.Label(dev_info_frame, text="Sumit Nandkishor Bavaskar", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="#ffffff")
        dev2_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        dev2_contact = tk.Label(dev_info_frame, text="Contact: 7709623616", font=("Arial", 18), bg="#1e1e1e", fg="#61dafb")
        dev2_contact.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Separator
        separator = tk.Frame(root, height=2, bd=1, relief="sunken", bg="#61dafb")
        separator.pack(fill="x", padx=20, pady=20)

        # Class and Year Information
        class_year_label = tk.Label(root, text="Class: TYBCA   Year: 2025", font=("Arial", 20, "italic"), bg="#1e1e1e", fg="#ffffff", pady=10)
        class_year_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = DeveloperInfoApp(root)
    root.mainloop()