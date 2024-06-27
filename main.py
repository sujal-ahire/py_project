import tkinter
import os
from time import strftime
from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer


class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")
        
        #bg image
        img_path = r"imgs\mask.jpg"
        img = Image.open(img_path)
        img = img.resize((1600, 900))
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1600, height=900)

        tilte_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("new times roman",35,"bold"),bg="black",fg="silver")
        tilte_lbl.place(x=0,y=0,width=1600,height=45)

#*************TIME*******
        def time():
            string= strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl= Label(tilte_lbl,font =("times new roman",15,"bold"),bg="black",fg="blue")
        lbl.place(x=2,y=0,width=110,height=50)
        time()


#sudent button
        img_path = r"imgs\sd.jpg"
        imgb1 = Image.open(img_path)
        imgb1 = imgb1.resize((220, 220))
        self.photoimgb1 = ImageTk.PhotoImage(imgb1)
        

        b1 = Button(bg_img, image=self.photoimgb1, command=self.student_details, cursor="hand2")
        b1.place(x=80,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details", command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="silver")
        b1_1.place(x=80,y=300,width=220,height=40)

  #Detect Face button
        img_path = r"imgs\fs.jpg"
        imgb2 = Image.open(img_path)
        imgb2 = imgb2.resize((220, 220))
        self.photoimgb2 = ImageTk.PhotoImage(imgb2)
        

        b2=Button(bg_img,image=self.photoimgb2,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="silver")
        b2_1.place(x=500,y=300,width=220,height=40)

 #Attendance button
        img_path = r"imgs\atten.png"
        imgb3 = Image.open(img_path)
        imgb3 = imgb3.resize((220, 220))
        self.photoimgb3 = ImageTk.PhotoImage(imgb3)
        

        b3=Button(bg_img,image=self.photoimgb3,cursor="hand2",command=self.attendance_data)
        b3.place(x=900,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="silver")
        b3_1.place(x=900,y=300,width=220,height=40)

#Help Desk button
        img_path = r"imgs\help.jpg"
        imgb4 = Image.open(img_path)
        imgb4 = imgb4.resize((220, 220))
        self.photoimgb4 = ImageTk.PhotoImage(imgb4)
        

        b4=Button(bg_img,image=self.photoimgb4,cursor="hand2")
        b4.place(x=1300,y=100,width=220,height=220)

        b4_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="silver")
        b4_1.place(x=1300,y=300,width=220,height=40)

#train button
        img_path = r"imgs\tr.png"
        imgb5 = Image.open(img_path)
        imgb5 = imgb5.resize((220, 220))
        self.photoimgb5 = ImageTk.PhotoImage(imgb5)
        

        b5=Button(bg_img,image=self.photoimgb5,cursor="hand2",command=self.train_data)
        b5.place(x=80,y=400,width=220,height=220)

        b5_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="silver")
        b5_1.place(x=80,y=600,width=220,height=40)

#photos button
        img_path = r"imgs\ph.png"
        imgb6 = Image.open(img_path)
        imgb6 = imgb6.resize((220, 220))
        self.photoimgb6 = ImageTk.PhotoImage(imgb6)
        
  
        b6=Button(bg_img,image=self.photoimgb6,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=400,width=220,height=220)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="silver")
        b6_1.place(x=500,y=600,width=220,height=40)

#Devloper button
        img_path = r"imgs\dev.jpg"
        imgb7 = Image.open(img_path)
        imgb7 = imgb7.resize((220, 220))
        self.photoimgb7 = ImageTk.PhotoImage(imgb7)
        

        b7=Button(bg_img,image=self.photoimgb7,cursor="hand2",command=self.developer_data)
        b7.place(x=900,y=400,width=220,height=220)

        b7_1=Button(bg_img,text="Devloper",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="black",fg="silver")
        b7_1.place(x=900,y=600,width=220,height=40)

#Exit button
        img_path = r"imgs\exit.jpg"
        imgb8 = Image.open(img_path)
        imgb8 = imgb8.resize((220, 220))
        self.photoimgb8 = ImageTk.PhotoImage(imgb8)
        
        b8=Button(bg_img,image=self.photoimgb8,cursor="hand2",command=self.iExit)
        b8.place(x=1300,y=400,width=220,height=220)

        b8_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="black",fg="silver")
        b8_1.place(x=1300,y=600,width=220,height=40)


#*****open photo********
    def open_img(self):
        os.startfile("data")


####Exit system$$
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure For Exit ",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


# function buttons student data page      
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

# function buttons  for train data page     
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

        
# function buttons  for face data   
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

# function buttons  for attendance data   
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)        

# function buttons  for developer data   
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()

