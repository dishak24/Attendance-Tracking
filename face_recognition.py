from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
# import warnings
# warnings.filterwarnings("ignore",category=DeprecationWarning)
#import warnings

#with warnings.catch_warnings():
    #warnings.filterwarnings("ignore",category=DeprecationWarning)



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance Tracking")
        
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
        bg1=Image.open(r"Attandence_images\bg2.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=100,width=1366,height=768)

        #title section
        title_lb1 = Label(bg_img,text="Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)


        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Attandence_images\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=550,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=550,y=350,width=180,height=45)
        #Attendance
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
                    
            if((i not in name_list))  and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
                
                
                
        
        
        #face recognition 
        
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
                
            coord=[]
                
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                    
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendance_tracking")
                my_cursor=conn.cursor()
                    
                my_cursor.execute("select Name from student where  Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                    
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                    
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                                    
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                    
                   
                    
                if confidence>80:
                    # cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                        
                coord=[x,y,w,h]
            return coord
    
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
            
            
        
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
            
        video_cap=cv2.VideoCapture(0)
            
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("WElcome To Face Recognition",img)
                
                
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                
                        
                        
              
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()