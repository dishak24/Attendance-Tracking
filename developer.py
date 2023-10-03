from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
##import numpy as np
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Sytem")
        
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

        title_lbl=Label(bg_img,text="Developers", font=("tahoma",30,'bold'), bg="white",fg="navyblue")
        title_lbl.place(x=0, y=0, width=1280,height=45)
        
        
        #student button
        img4=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\d1 (1).jpg")
        img4=img4.resize((170,170),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=300, y=150, width=170,height=170)

        b1_1=Button(bg_img, text="Disha Kamble", cursor="hand2", font=("times new roman",14,'bold'), bg="#c8d8e4", fg="black")
        b1_1.place(x=300, y=300, width=170,height=30)


        #detect face
        #img5=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\d1 (5).jpg")
        #img5=img5.resize((170,170),Image.ANTIALIAS)
        #self.photoimg5=ImageTk.PhotoImage(img5)

        #b1=Button(bg_img, image=self.photoimg5, cursor="hand2")
        #b1.place(x=550, y=150, width=170,height=170)

        #b1_1=Button(bg_img, text="Priyanka Shinde", cursor="hand2", font=("times new roman",14,'bold'), bg="#c8d8e4", fg="black")
        #b1_1.place(x=550, y=300, width=170,height=30)

        #Attandence
        img6=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\d1 (4).jpg")
        img6=img6.resize((170,170),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=570, y=150, width=170,height=170)

        b1_1=Button(bg_img, text="Pallavi Talware", cursor="hand2", font=("times new roman",14,'bold'), bg="#c8d8e4", fg="black")
        b1_1.place(x=570, y=300, width=170,height=30)

        
        #help desk
        img7=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\d1 (3).jpg")
        img7=img7.resize((170,170),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=840, y=150, width=170,height=170)

        b1_1=Button(bg_img, text="Shubhangi kande", cursor="hand2", font=("times new roman",14,'bold'), bg="#c8d8e4", fg="black")
        b1_1.place(x=840, y=300, width=170,height=30)
        
        

        #2nd line icons
        #train face button
       # img8=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\d1 (2).jpg")
       # img8=img8.resize((170,170),Image.ANTIALIAS)
       # self.photoimg8=ImageTk.PhotoImage(img8)

       # b1=Button(bg_img, image=self.photoimg8, cursor="hand2")
        #b1.place(x=560, y=320, width=170,height=170)

        #b1_1=Button(bg_img, text="Mayuri Sable", cursor="hand2", font=("times new roman",14,'bold'), bg="#c8d8e4", fg="black")
       # b1_1.place(x=560, y=470, width=170,height=30)

        

        
         
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
