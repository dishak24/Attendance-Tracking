from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import time
import datetime
import random
from register import Register
from main import face_recognition_sytem

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        
        img_top=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\loginBG.jpg")
        img_top=img_top.resize((1280,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=505,y=120,width=340,height=400)
        
        img1=Image.open(r"Attandence_images\LoginIconAppl.png")
        img1=img1.resize((70,70),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=630,y=120,width=100,height=100)
        
        
        get_started=Label(frame,text="Get Started",font=("times new roman",18,"bold"),fg="white",bg="black")
        get_started.place(x=110,y=95)
        
        
        username=Label(frame,text="Username",font=("times new roman",18,"bold"),fg="white",bg="black")
        username.place(x=70,y=145)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        
        
        password=Label(frame,text="Password",font=("times new roman",18,"bold"),fg="white",bg="black")
        password.place(x=70,y=215)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        #icon imgs
        img2=Image.open(r"Attandence_images\LoginIconAppl.png")
        img2=img1.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=545,y=270,width=25,height=25)
        
        
        img3=Image.open(r"Attandence_images\lock-512.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg1.place(x=545,y=340,width=25,height=25)
        
        
        #button
        loginbutton=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbutton.place(x=110,y=300,width=120,height=35)
        
        #registerbtn
        registerbutton=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbutton.place(x=15,y=350,width=160)
        
        forgetpasswordbutton=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpasswordbutton.place(x=10,y=370,width=160)
        
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="dbatu":
            messagebox.showinfo("Success","Welcome to the Attendance Tracking System")
        else:
            messagebox.showerror("welcome")

        
            
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reseet password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendance_tracking")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            
            if row==None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                
                l=Label(self.root,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                
                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)
        

        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
        
        
                security_A=Label(self.root2,text="Securty Answwer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)
        
                self.txt_security=ttk.Entry(self.root2,font=("times new roamn",15))
                self.txt_security.place(x=50,y=180,width=250)
                
                
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
        
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roamn",15))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
                
                
            
                
            


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        
        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\wp2551980.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\wp2551980.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        
        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=20,y=20)
        
        #label and entry
        # fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        # fname.place(x=50,y=100)
        
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100)
        
        # fname_entry=ttk.Entry(fname,font=("times new roman",15,"bold"))
        # fname_entry.place(x=50,y=130,width=250)
        
        fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname.place(x=50,y=130,width=250)
        
        
        
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #row2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        #row3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        

        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        
        security_A=Label(frame,text="Securty Answwer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roamn",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        #row4
        pswd=Label(frame,text="password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        
        
        #check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #buttons
        img=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\wp2551980.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)
        
        img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\Attandence_Project\Attandence_images\wp2551980.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)
        
        
        
        #function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="attendance_tracking")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

        
        
    
if __name__ == "__main__":
    main()
    