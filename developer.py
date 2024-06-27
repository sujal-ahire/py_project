from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")

        tilte_lbl=Label(self.root,text="DEVELOPER",font=("new times roman",35,"bold"),bg="black",fg="silver")
        tilte_lbl.place(x=0,y=0,width=1600,height=45)


        img_path = r"imgs\mask.jpg"
        img_top = Image.open(img_path)
        img_top = img_top.resize((1600, 900))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_img= Label(self.root, image=self.photoimg_top)
        bg_img.place(x=0, y=45, width=1600, height=790)

    #_______Frame____
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1082,y=0,width=500,height=600)

        
        img_path = r"imgs\me.png"
        img_frame = Image.open(img_path)
        img_frame = img_frame.resize((130, 120))
        self.photoimg_frame = ImageTk.PhotoImage(img_frame)

        bg_img= Label(main_frame, image=self.photoimg_frame)
        bg_img.place(x=370, y=0, width=130, height=120)

    #developer info
        dev_lbl=Label(main_frame,text="Hello, My Name Is Sujal",font=("new times roman",20,"bold"),fg="black")
        dev_lbl.place(x=0,y=5)

        dev1_lbl=Label(main_frame,text="I am B.voc Software Development",font=("new times roman",15,"bold"),fg="black")
        dev1_lbl.place(x=0,y=45)

        dev2_lbl=Label(main_frame,text="Student.",font=("new times roman",15,"bold"),fg="black")
        dev2_lbl.place(x=0,y=76)











if __name__ == "__main__":
     root = Tk()
     obj = Developer(root)
     root.mainloop()