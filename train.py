from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")



        tilte_lbl=Label(self.root,text="TRAIN  DATA SET",font=("new times roman",35,"bold"),bg="black",fg="silver")
        tilte_lbl.place(x=0,y=0,width=1600,height=45)

        img_path = r"imgs\tr1.jpg"
        img_top = Image.open(img_path)
        img_top = img_top.resize((1600, 900))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_img= Label(self.root, image=self.photoimg_top)
        bg_img.place(x=0, y=45, width=1600, height=320)

       #*********button**********
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="silver")
        b1_1.place(x=0,y=340,width=1600,height=80)
 

        img_path = r"imgs\tr2.png"
        img_bottom = Image.open(img_path)
        img_bottom = img_bottom.resize((1600, 900))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        bg_img= Label(self.root, image=self.photoimg_bottom)
        bg_img.place(x=0, y=420, width=1600, height=410)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")  # gray scale image
            imageNp=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #########tain the classifier and save

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training datasets completed!!",parent=self.root)










if __name__ == "__main__":
     root = Tk()
     obj = Train(root)
     root.mainloop()