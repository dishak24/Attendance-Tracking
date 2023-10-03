from tkinter import*
from tkinter import ttk
import webbrowser
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
##import numpy as np
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart attendance Tracking Sytem")
        
        
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
        
        # backgorund image 
        bg1=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\bg4.png")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)
        
        
        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)

        #title section
        title_lb1 = Label(bg_img,text="Help Support",font=("tahoma",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\link.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.website,image=self.std_img1,cursor="hand2")
        std_b1.place(x=200,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.website,text="LinkedIn",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=200,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\insta1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=430,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="Instagram",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=430,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\t.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=660,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.youtube,text="Telegram",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=660,y=380,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=890,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=890,y=380,width=180,height=45)


        # create function for button 
    
    
    def website(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/disha-kamble-22690b231/"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.instagram.com/"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://web.telegram.org/k/"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)




if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()