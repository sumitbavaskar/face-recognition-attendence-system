from tkinter import *
from tkinter import Button
from tkinter import ttk 
from PIL import Image,ImageTk 
from student import student

 



class face_recognisation_system:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        #FIRST IMAGE

        img=Image.open(r"D:\face recognisation system\college_picture\Standard2.jpg")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)                                           

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #SECOND IMAGE 

        img1=Image.open(r"D:\face recognisation system\college_picture\Standard3.jpg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)                                          

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #THIRD IMAGE

        img2=Image.open(r"D:\face recognisation system\college_picture\face4.jpg")
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)                                           #(Built in function )

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


        # BACKGROUND IMAGE 

        bg_img=Image.open(r"D:\face recognisation system\college_picture\bg.jfif")
        bg_img=bg_img.resize((1370,710))
        self.photoimg3=ImageTk.PhotoImage(bg_img)                                           #(Built in function )

        bg_imglbl=Label(self.root,image=self.photoimg3)
        bg_imglbl.place(x=0,y=130,width=1370,height=710)


        l1=Label(text="FACE RECOGNITION ATTENDANCE SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        l1.place(x=0,y=140,width=1350,height=45)

        # STUDENT button
        img3=Image.open(r"D:\face recognisation system\college_picture\employee.jfif")
        img3=img3.resize((150,150))
        self.photoimg4=ImageTk.PhotoImage(img3) 

        b1=Button(bg_imglbl,image=self.photoimg4,cursor="hand2",)
        b1.place(x=100,y=100,width=150,height=150)

        b1_lbl=Button(bg_imglbl,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="black")
        b1_lbl.place(x=100,y=250,width=150,height=35)

#------FACE DETECTOR ---------
        img4=Image.open(r"D:\face recognisation system\college_picture\face1.jpg")
        img4=img4.resize((150,150))
        self.photoimg5=ImageTk.PhotoImage(img4) 

        b2=Button(bg_imglbl,image=self.photoimg5,cursor="hand2")
        b2.place(x=400,y=100,width=150,height=150)

        b2_lbl=Button(bg_imglbl,text="FACE DETECTOR",cursor="hand2",font=("times new roman",13,"bold"),bg="yellow",fg="black")
        b2_lbl.place(x=400,y=250,width=150,height=35)


#---------ATTENDENCE--------------------

        img5=Image.open(r"D:\face recognisation system\college_picture\attend.jfif")
        img5=img5.resize((150,150))
        self.photoimg6=ImageTk.PhotoImage(img5) 

        b3=Button(bg_imglbl,image=self.photoimg6,cursor="hand2")
        b3.place(x=700,y=100,width=150,height=150)

        b3_lbl=Button(bg_imglbl,text="ATTENDENCE",cursor="hand2",font=("times new roman",13,"bold"),bg="yellow",fg="black")
        b3_lbl.place(x=700,y=250,width=150,height=35)

#-----------HELP DESK ------------------

        img6=Image.open(r"D:\face recognisation system\college_picture\help.jpg")
        img6=img6.resize((150,150))
        self.photoimg7=ImageTk.PhotoImage(img6) 

        b4=Button(bg_imglbl,image=self.photoimg7,cursor="hand2",)
        b4.place(x=1000,y=100,width=150,height=150)

        b4_lbl=Button(bg_imglbl,text="HELP",cursor="hand2",font=("times new roman",13,"bold"),bg="yellow",fg="black")
        b4_lbl.place(x=1000,y=250,width=150,height=35)

#------------MANIPULATION----------------------

        img7=Image.open(r"D:\face recognisation system\college_picture\manipulation.jpg")
        img7=img7.resize((150,150))
        self.photoimg8=ImageTk.PhotoImage(img7) 

        b5=Button(bg_imglbl,image=self.photoimg8,cursor="hand2")
        b5.place(x=100,y=350,width=150,height=150)

        b5_lbl=Button(bg_imglbl,text="Train data",cursor="hand2",font=("times new roman",13,"bold"),bg="yellow",fg="black")
        b5_lbl.place(x=100,y=500,width=150,height=35)
    
 #-----------FACE DATA-----------------------------

        img8=Image.open(r"D:\face recognisation system\college_picture\face_data.jfif")
        img8=img8.resize((150,150))
        self.photoimg9=ImageTk.PhotoImage(img8) 

        b6=Button(bg_imglbl,image=self.photoimg9,cursor="hand2")
        b6.place(x=400,y=350,width=150,height=150)

        b6_lbl=Button(bg_imglbl,text="FACE DATA",cursor="hand2",font=("times new roman",13,"bold"),bg="yellow",fg="black")
        b6_lbl.place(x=400,y=500,width=150,height=35)


#-------------ABOUT-----------------------

        img9=Image.open(r"D:\face recognisation system\college_picture\dev.jfif")
        img9=img9.resize((150,150))
        self.photoimg10=ImageTk.PhotoImage(img9) 

        b7=Button(bg_imglbl,image=self.photoimg10,cursor="hand2")
        b7.place(x=700,y=350,width=150,height=150)

        b7_lbl=Button(bg_imglbl,text="ABOUT US",cursor="hand2",font=("times new roman",13,"bold"),bg="yellow",fg="black")
        b7_lbl.place(x=700,y=500,width=150,height=35)


#-----------EXIT---------------------


        img10=Image.open(r"D:\face recognisation system\college_picture\EXIT.jfif")
        img10=img10.resize((150,150))
        self.photoimg11=ImageTk.PhotoImage(img10) 

        b8=Button(bg_imglbl,image=self.photoimg11,cursor="hand2")
        b8.place(x=1000,y=350,width=150,height=150)

        b8_lbl=Button(bg_imglbl,text="EXIT",cursor="hand2",font=("times new roman",13,"bold"),bg="red",fg="black")
        b8_lbl.place(x=1000,y=500,width=150,height=35)

#----============================= FUNCTION BUTTON ----================
        def student_details(self):
             self.new_window=Toplevel(self.root)
             self.app=student(self.new_window)


        







if __name__ == "__main__":
    root=Tk()
    obj=face_recognisation_system(root)
    root.mainloop()
