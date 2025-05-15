
from tkinter import *
from tkinter import Button
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")

        # =================== variables =================
        self.var_dep= StringVar()
        self.var_course= StringVar()
        self.var_year= StringVar()
        self.var_semester= StringVar()
        self.var_studentID= StringVar()
        self.var_DOB= StringVar()
        self.var_name= StringVar()
        self.var_rollnumber= StringVar()
        self.var_mobilenumber= StringVar()
        self.var_address= StringVar()

        # FIRST IMAGE
        img = Image.open(r"D:\face recognisation system\college_picture\Standard2.jpg").resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # SECOND IMAGE
        img1 = Image.open(r"D:\face recognisation system\college_picture\Standard3.jpg").resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # THIRD IMAGE
        img2 = Image.open(r"D:\face recognisation system\college_picture\face4.jpg").resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # BACKGROUND IMAGE 
        bg_img=Image.open(r"D:\face recognisation system\college_picture\bg.jfif")
        bg_img=bg_img.resize((1370,710))
        self.photoimg3=ImageTk.PhotoImage(bg_img)

        bg_imglbl=Label(self.root,image=self.photoimg3)
        bg_imglbl.place(x=0,y=130,width=1370,height=710)

        # l1=Label(text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        # l1.place(x=15,y= 130,width=1370,height=45)

        # MAIN FRAME
        main_frame = Frame(bg_imglbl, bd=2,bg="white")
        main_frame.place(x=20, y=55, width=1320, height=500)

        # LEFT LABEL FRAME
        left_frame = LabelFrame(main_frame, bg="white", bd=2, font=("times new roman", 15, "bold"), relief=RIDGE, text="STUDENT MANAGEMENT")
        left_frame.place(x=10, y=3, width=660, height=490)

        # LEFT FRAME IMG
        img_left = Image.open(r"D:\face recognisation system\college_picture\face4.jpg").resize((600, 130))
        img_left=img_left.resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left , bg="white")
        f_lbl.place(x=5, y=0, width=720, height=130)

        # CURRENT COURSE
        left_frame=LabelFrame(left_frame, bd=2,bg="white",relief=RIDGE,text=" COURSE INFORMATION", font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=130,width=660,height=120 )

        

        
        # Adding Department Label
        department_label = Label(left_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        department_label.grid(row=0 , column=0 , padx=10,sticky=W)

        # Adding Department Combo Box
        department_combo = ttk.Combobox(left_frame, textvariable=self.var_dep,font=("times new roman", 12, "bold"), state="readonly")
        department_combo['values'] =("Select Department", "Computer Science", "Electrical Engineering", "Mechanical Engineering", ) # Example options
        department_combo.current(0)
        department_combo.grid(row=0 , column=1 , padx=2,pady=10,sticky=W)

        # Adding course Label
        course_label = Label(left_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0 , column=2 , padx=10 , sticky=W)

        # Adding course Combo Box
        course_combo = ttk.Combobox(left_frame, textvariable=self.var_course,font=("times new roman", 12, "bold"), state="readonly")
        course_combo['values'] = ("Select Department", "BCA", "B.tech", "BE")  # Example options
        course_combo.current(0)
        course_combo.grid(row=0 , column=3 , padx=2,pady=10,sticky=W)

        # Adding year Label
        year_label = Label(left_frame, text="year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1 , column=0 , padx=10,sticky=W)

        # Adding year Combo Box
        year_combo = ttk.Combobox(left_frame, textvariable=self.var_year,font=("times new roman", 12, "bold"), state="readonly")
        year_combo['values'] =("Select year", "F.Y", "S.Y", "T.Y","Final Year" , )  # Example options
        year_combo.current(0)
        year_combo.grid(row=1 , column=1 , padx=2,pady=10,sticky=W)

        # Adding semester Label
        semeseter_label = Label(left_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semeseter_label.grid(row=1 , column=2, padx=10,sticky=W)

        # Adding semester Combo Box
        semeseter_combo = ttk.Combobox(left_frame,textvariable=self.var_semester ,font=("times new roman", 12, "bold"), state="readonly")
        semeseter_combo['values'] = ("Select Department", "semester 1", "semester 2", "semester 3" )  # Example options
        semeseter_combo.current(0)
        semeseter_combo.grid(row=1 , column=3 , padx=2,pady=10,sticky=W)

    
        # Adding Student Information Label Frame
        student_info_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="STUDENT INFORMATION", font=("times new roman", 13, "bold"))
        student_info_frame.place(x=15, y=280, width=650, height=210)

        # Adding Labels and Entry for Student Information
        studentID_label = Label(student_info_frame, text="StudentID", font=("times new roman", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, pady=8, sticky=W)

        studentID_entry = Entry(student_info_frame,textvariable=self.var_studentID ,font=("times new roman", 12, "bold"), bd=2, relief=RIDGE)
        studentID_entry.grid(row=0, column=1, padx=10, pady=8, sticky=W)

        DOB_label = Label(student_info_frame, text="DOB", font=("times new roman", 12, "bold"), bg="white")
        DOB_label.grid(row=0, column=2, padx=10, pady=8, sticky=W)

        DOB_entry = Entry(student_info_frame,textvariable=self.var_DOB ,font=("times new roman", 12, "bold"), bd=2, relief=RIDGE)
        DOB_entry.grid(row=0, column=3, padx=10, pady=8, sticky=W)

        name_label = Label(student_info_frame, text="Name", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=8, sticky=W)

        name_entry = Entry(student_info_frame,textvariable=self.var_name ,font=("times new roman", 12, "bold"), bd=2, relief=RIDGE)
        name_entry.grid(row=1, column=1, padx=10, pady=8, sticky=W)

        roll_label = Label(student_info_frame, text="Roll Number", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=1, column=2, padx=10, pady=8, sticky=W)

        roll_entry = Entry(student_info_frame,textvariable=self.var_rollnumber ,font=("times new roman", 12, "bold"), bd=2, relief=RIDGE)
        roll_entry.grid(row=1, column=3, padx=10, pady=8, sticky=W)

        mobile_label = Label(student_info_frame, text="Mobile Number", font=("times new roman", 12, "bold"), bg="white")
        mobile_label.grid(row=2, column=0, padx=10, pady=8, sticky=W)

        mobile_entry = Entry(student_info_frame,textvariable=self.var_mobilenumber, font=("times new roman", 12, "bold"), bd=2, relief=RIDGE)
        mobile_entry.grid(row=2, column=1, padx=10, pady=8, sticky=W)

        address_label = Label(student_info_frame, text="address", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=2, column=2, padx=10, pady=8, sticky=W)

        address_entry = Entry(student_info_frame,textvariable=self.var_address ,font=("times new roman", 12, "bold"), bd=2, relief=RIDGE)
        address_entry.grid(row=2, column=3, padx=10, pady=8, sticky=W)

    #     # Adding Radio Button 
    #     self.var_radiobtn1=StringVar()
    #     radiobtn1 = ttk.Radiobutton(student_info_frame,textvariable=self.var_radiobtn1, text="take photo sample",value="yes")
    #     radiobtn1.grid(row=3, column=0, padx=10, pady=10, sticky=W)

    #     self.var_radiobtn2=StringVar()
    #     radiobtn2 =ttk. Radiobutton(student_info_frame, textvariable=self.var_radiobtn2,text="no photo sample",  value="no")
    #     radiobtn2.grid(row=3, column=1, padx=10, pady=10, sticky=W)


      # Adding button frame 
        button_frame = Frame(student_info_frame, bg="white", bd=2, relief=RIDGE)
        button_frame.place(x=0, y=120, width=645, height=65)

        # SAVE Button
        save_btn = Button(button_frame, text="SAVE", command=self.add_data, width=17, font=("times new roman", 12, "bold"), bg="green", fg="white",)
        save_btn.grid(row=0, column=0)
        # update Button
        update_btn = Button(button_frame, text="update", width=17, font=("times new roman", 12, "bold"), bg="green", fg="white",)
        update_btn.grid(row=0, column=1)
        # delete Button
        delete_btn = Button(button_frame, text="delete", width=17, font=("times new roman", 12, "bold"), bg="green", fg="white",)
        delete_btn.grid(row=0, column=2)
        # reset Button
        reset_btn = Button(button_frame, text="reset", width=17, font=("times new roman", 12, "bold"), bg="green", fg="white",)
        reset_btn.grid(row=0, column=3)

        button_frame1 = Frame(student_info_frame, bg="white", bd=2, relief=RIDGE)
        button_frame1.place(x=0, y=150, width=645, height=35)

         # take photo Button
        take_photo_btn = Button(button_frame1, text="take a photo", width=35, font=("times new roman", 12, "bold"), bg="green", fg="white",)
        take_photo_btn.grid(row=0, column=0)
         # update photo Button
        update_photo_btn = Button(button_frame1, text="update a photo", width=35, font=("times new roman", 12, "bold"), bg="green", fg="white",)
        update_photo_btn.grid(row=0, column=1)
         

        # right frame 
        right_frame =LabelFrame(main_frame,bg="white", bd=2, font=("times new roman",15,"bold"),relief=RIDGE,text="STUDENT MANAGEMENT",)
        right_frame.place(x=680,y=3,width=620,height=490 )

      
        # RIGHT FRAME IMG
        img_right = Image.open(r"D:\face recognisation system\college_picture\face4.jpg").resize((600, 130))
        img_right=img_right.resize((720, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right , bg="white")
        f_lbl.place(x=5, y=0, width=720, height=130)

        # ================  SEARCHING SYSTEM ======================

        # Adding Searching system Frame
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="SEARCH SYSTEM", font=("times new roman", 13, "bold"))
        search_frame.place(x=5, y=135, width=610, height=70)

        # Adding Search Label
        search_label = Label(search_frame, text="Search:-", font=("times new roman", 12, "bold"), bg="Red", fg="white")
        search_label.grid(row=0 , column=0 , padx=10,sticky=W)

        # Adding Search Combo Box
        search_combo = ttk.Combobox(search_frame, width=10,font=("times new roman", 12, "bold"), state="readonly")
        search_combo['values'] = ("Select ", "Roll NO", "Phone No")  # Example options
        search_combo.current(0)
        search_combo.grid(row=0 , column=1 , padx=2,pady=10,sticky=W)

        search_entry = Entry(search_frame, width=15,font=("times new roman", 12, "bold"), bd=2, relief=RIDGE)
        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

         # search Button
        search_btn = Button(search_frame, text="Search",command=self.search_data ,width=12, font=("times new roman", 12, "bold"), bg="green", fg="white",)
        search_btn.grid(row=0, column=3,padx=2,pady=10)
        # show All Button
        show_btn = Button(search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="green", fg="white",)
        show_btn.grid(row=0, column=4,padx=2,pady=10)

        # Adding a table frame
        table_frame = Frame(right_frame, bd=2,bg="white" ,relief=RIDGE)
        table_frame.place(x=8,y=210, width=600, height=250)
        # Creating a scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("dep","course","year","semester","name","roll number","mobile number","address","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="dep")
        self.student_table.heading("course", text="course")
        self.student_table.heading("year", text="year")
        self.student_table.heading("semester", text="semester")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll number", text="Roll No")
        self.student_table.heading("mobile number", text="Mobile No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("Photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.pack( fill=BOTH , expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()




        # Database Connection
    def connect_db():
        return mysql.connector.connect(host="localhost", user="root", password="Sumit@2304", database="student")
                                           


        # ========================== FUNCTIONS DECLARATION =========================

    def add_data(self):
        if self.var_dep.get()=="select department"or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are required")   
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sumit@2304", database="face_recognisation_system")
                my_cursor = conn.cursor()

                query = "INSERT INTO student (department, course, semester, year, studentID, DOB, name, roll, mobile, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                
                values = (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_semester.get(),
                    self.var_year.get(),
                    self.var_studentID.get(),
                    self.var_DOB.get(),
                    self.var_name.get(),
                    self.var_rollnumber.get(),
                    self.var_mobilenumber.get(),
                    self.var_address.get()
                )

                # Execute the SQL query
                my_cursor.execute(query, values)

                # Commit the transaction
                conn.commit()
                
                self.fetch_data() 
                # Close the connection
                conn.close()
                
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


#==================== FETCH DATA ==========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Sumit@2304", database="face_recognisation_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.close() 



     #======================= GET CURSOR ======================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])         
        self.var_course.set(data[1])         
        self.var_semester.set(data[2])         
        self.var_year.set(data[3])         
        self.var_studentID.set(data[4])         
        self.var_DOB.set(data[5])         
        self.var_name.set(data[6])         
        self.var_rollnumber.set(data[7])         
        self.var_mobilenumber.set(data[8])         
        self.var_address.set(data[9])  
         
         #========================= UPDATE DATA ==========================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_studentID.get():
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do you want to update student details",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Sumit@2304", database="face_recognisation_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,year=%s,semester=%s,name=%s,Dob=%s,roll=%s,mobile=%s,address=%s, where studentID=%s" ,(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_semester.get(),
                    self.var_year.get(),
                    self.var_DOB.get(),
                    self.var_name.get(),
                    self.var_rollnumber.get(),
                    self.var_mobilenumber.get(),
                    self.var_address.get(),
                    self.var_studentID.get()

                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "student details successfully updated")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                conn.commit
                self.fetch_data()
                conn.close             
                

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_studentID.get():
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
            
                conn = mysql.connector.connect(host="localhost", username="root", password="Sumit@2304", database="face_recognisation_system")
                my_cursor = conn.cursor()
            
            except:
                pass

    def search_data(self):
        # messagebox.showerror("hhhh")
        # print("Search function triggered")
        # print("Search By:", self.var_search_by.get())
        # print("Search Text:", self.var_search_txt.get())

        if self.var_search_by.get() == "Select" or self.var_search_txt.get() == "":
            messagebox.showerror("Error", "Please select a search criteria and enter search text.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sumit@2304", database="face_recognisation_system")
                my_cursor = conn.cursor()

                query = ""
                if self.var_search_by.get() == "Roll":
                    query = "SELECT department, course, year, semester, name, roll, mobile, address, studentID FROM student WHERE roll LIKE %s"
                elif self.var_search_by.get() == "Phone":
                    query = "SELECT department, course, year, semester, name, roll, mobile, address, studentID FROM student WHERE mobile LIKE %s"
                elif self.var_search_by.get() == "Name":
                    query = "SELECT department, course, year, semester, name, roll, mobile, address, studentID FROM student WHERE name LIKE %s"

                print("Running Query:", query)

                my_cursor.execute(query, (f"%{self.var_search_txt.get()}%",))
                rows = my_cursor.fetchall()

                if len(rows) == 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", END, values=row)
                else:
                    messagebox.showinfo("Result", "No matching record found.", parent=self.root)

                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)
































if __name__ == "__main__":
    root=Tk()
    obj=FaceRecognitionSystem(root)
    root.mainloop()
