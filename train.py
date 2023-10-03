from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import numpy as np
import cv2
import os


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x790+0+0")
        self.root.title("Attendance Tracking System")
        
        title_lbl=Label(self.root,text="Train Data",font=("times new roman",24,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1280,height=50)
        
        #Bg img
        img3=Image.open(r"Attandence_images\bg3.jpg")
        img3=img3.resize((1280,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=55,width=1280,height=590)

        #title_lbl=Label(bg_img,text="ATTANDENCE TRACKING SYSTEM", font=("times new roman",30,'bold'), bg="purple", fg="yellow")
        #title_lbl.place(x=0, y=0, width=1280,height=45)
        
        
        std_img_btn=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\t_btn1.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=550,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=550,y=350,width=180,height=45)
        
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  # gray scale image
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
                        
            
            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
        
        #train the classifier and save
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
