from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
from time import time
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")


        tilte_lbl=Label(self.root,text="FACE RECOGNITION",font=("new times roman",35,"bold"),bg="black",fg="silver")
        tilte_lbl.place(x=0,y=0,width=1600,height=45)


        img_path = r"imgs\mask.jpg"
        img_left = Image.open(img_path)
        img_left = img_left.resize((830, 700))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        bg_img= Label(self.root, image=self.photoimg_left)
        bg_img.place(x=0, y=45, width=830, height=700)
 
        
        img_path = r"imgs\fs.jpg"
        img_right = Image.open(img_path)
        img_right= img_right.resize((810, 700))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        bg_img= Label(self.root, image=self.photoimg_right)
        bg_img.place(x=830, y=45, width=810, height=700)

        b1_1=Button(bg_img,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="black",fg="silver")
        b1_1.place(x=260,y=515,width=300,height=55)

     # Dictionary to store last entry timestamps for each person
        self.last_entry_timestamps = {}

     #*************Attendance ********************
    def mark_attendance(self,i,r,n,d,c):

        # Get the current timestamp
        current_time = time()

        # Calculate the key for the person entry
        person_key = (i, r, n, d, c)

        # Check if the person has an existing entry and if enough time has passed since the last entry
        if person_key in self.last_entry_timestamps:
            last_entry_time = self.last_entry_timestamps[person_key]
            if current_time - last_entry_time < 59:
                print("Skipping entry for", person_key, "as 59 seconds have not passed since the last entry.")
                return False
            




        # Add the new entry to the file
        with open("Attendance.csv", "a", newline="\n") as f:
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S %p")
            f.write(f"{i},{r},{n},{d},{c},{dtString},{d1},present\n")

        # Update the last entry timestamp for the person
        self.last_entry_timestamps[person_key] = current_time
        print("Entry added successfully for", person_key)
        return True




   ###########     face recognition  *************
        
    def face_recog(self):
        def draw_boundray(img, classifier, scalefactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            features = classifier.detectMultiScale(gray_image, scalefactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recogniser")
                my_cursor = conn.cursor()

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Course from student where Student_id=" + str(id))
                c = my_cursor.fetchone()
                c = "+".join(c)

                if confidence > 75:
                    cv2.putText(img, f"Id: {i}", (x, y - 120), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255,255), 2)
                    cv2.putText(img, f"Roll No: {r}", (x, y - 90), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 65), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Year: {c}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(i, r, n, d, c)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 2)

                coord = [x, y, w, h]

            return coord

        def recognise(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognise(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            key = cv2.waitKey(1)
            if key == 27:  # Esc key to exit
                break

    # Release video capture device and close all windows
        video_cap.release()
        cv2.destroyAllWindows()

 

if __name__ == "__main__":
     root = Tk()
     obj = Face_Recognition(root)
     root.mainloop()