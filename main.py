from tkinter import*
from tkinter import ttk
import tkinter
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import attendance
from developer import Developer
from help import Help



class face_recognition_sytem:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attandence Sytem*")

        #first img
        img=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\Stanford.jpg")
        img=img.resize((450,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=100)

        #2nd img
        img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\facialrecognition.png")
        img1=img1.resize((450,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=100)

        #3rd img
        img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\u.jpg")
        img2=img2.resize((450,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=850,y=0,width=450,height=100)
        
        #Bg img
        img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\bg3.jpg")
        img3=img3.resize((1280,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1280,height=590)

        title_lbl=Label(bg_img,text="Smart Attendance System", font=("tahoma",28,'bold'), bg="white",fg="navyblue")
        title_lbl.place(x=0, y=0, width=1280,height=45)
        
        
        #time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl,font=("tahoma",11,"bold"),background = "white",foreground = "black")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #student button
        img4=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\std1.jpg")
        img4=img4.resize((170,170),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=150, y=70, width=170,height=170)

        b1_1=Button(bg_img,command=self.student_details, text="Student Pannel", cursor="hand2", font=("tahoma",14,'bold'), bg="#c8d8e4", fg="black")
        b1_1.place(x=150, y=220, width=170,height=30)


        #detect face
        img5=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\det1.jpg")
        img5=img5.resize((170,170),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=430, y=70, width=170,height=170)

        b1_1=Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("tahoma",14,'bold'), bg="#c8d8e4", fg="black")
        b1_1.place(x=430, y=220, width=170,height=30)

        #Attandence
        img6=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\att.jpg")
        img6=img6.resize((170,170),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b1.place(x=680, y=70, width=170,height=170)

        b1_1=Button(bg_img, text="Attandence", cursor="hand2",command=self.attendance_data, font=("tahoma",14,'bold'), bg="#c8d8e4", fg="black")
        b1_1.place(x=680, y=220, width=170,height=30)

        #help desk
        img7=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\hlp.jpg")
        img7=img7.resize((170,170),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place(x=950, y=70, width=170,height=170)

        b1_1=Button(bg_img, text="Help Support", cursor="hand2",command=self.help_data, font=("tahoma",14,'bold'), bg="#c8d8e4", fg="black")
        b1_1.place(x=950, y=220, width=170,height=30)

        #2nd line icons
        #train face button
        img8=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\tra1.jpg")
        img8=img8.resize((170,170),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=150, y=300, width=170,height=170)

        b1_1=Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data,font=("tahoma",14,'bold'), bg="#c8d8e4", fg="black")
        b1_1.place(x=150, y=450, width=170,height=30)

        #photos button
        img9=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\dataset.jpg")
        img9=img9.resize((170,170),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=430, y=300, width=170,height=170)

        b1_1=Button(bg_img, text="Dataset", cursor="hand2",command=self.open_img, font=("tahoma",14,'bold'), bg="#c8d8e4", fg="black")
        b1_1.place(x=430, y=450, width=170,height=30)

        #developer button
        img10=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\dev.jpg")
        img10=img10.resize((170,170),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data)
        b1.place(x=680, y=300, width=170,height=170)

        b1_1=Button(bg_img, text="Developers", cursor="hand2",command=self.developer_data, font=("tahoma",14,'bold'), bg="#c8d8e4", fg="black")
        b1_1.place(x=680, y=450, width=170,height=30)


        #exit button
        img11=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\exi.jpg")
        img11=img11.resize((170,170),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.exit)
        b1.place(x=950, y=300, width=170,height=170)

        b1_1=Button(bg_img, text="EXIT", cursor="hand2",command=self.exit, font=("tahoma",14,'bold'), bg="#c8d8e4", fg="black")
        b1_1.place(x=950, y=450, width=170,height=30)


    def open_img(self):
        os.startfile("data")

#exit button
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Attendance Tracking System:","Are you sure exit this project",parent=self.root)
        if self.exit >0:
                self.root.destroy()
        else:
            return

    #functions buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=face_recognition_sytem(root)
    root.mainloop()