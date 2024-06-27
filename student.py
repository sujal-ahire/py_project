from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")

        #--__variables__----
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


#bg image
        img_path = r"imgs\bg1.jpg"
        img = Image.open(img_path)
        img = img.resize((1600, 900))
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1600, height=900)

        tilte_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("new times roman",35,"bold"),bg="black",fg="silver")
        tilte_lbl.place(x=0,y=0,width=1600,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1560,height=780)

    # left lable frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RAISED,text="Student Details",font=("times new roman",12,"bold"))  
        left_frame.place(x=10,y=10,width=780,height=700)

        img_path = r"imgs\bg1.jpg"
        img_left = Image.open(img_path)
        img_left = img_left.resize((1600, 900))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        bg_img= Label(left_frame, image=self.photoimg_left)
        bg_img.place(x=5, y=0, width=770, height=130)
    
     #current course
        current_course=LabelFrame(left_frame,bd=2,bg="white",relief=RAISED,text="Current course information",font=("times new roman",12,"bold"))  
        current_course.place(x=5,y=135,width=770,height=150)

    #department
        dep_label=Label(current_course,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","B.voc Software Devlopment ","It","Bcs","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
    
    #course
        course_label=Label(current_course,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","First Year","Second Year","Third Year")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

    #Year
        year_label=Label(current_course,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

    #Semester
        semester_label=Label(current_course,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

     
    #Class Student information
        class_student=LabelFrame(left_frame,bd=2,bg="white",relief=RAISED,text="Class Student Information",font=("times new roman",12,"bold"))  
        class_student.place(x=5,y=295,width=770,height=380)

    # Student id
        studentId_label=Label(class_student,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_student,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    # Student Name
        studentName_label=Label(class_student,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

    # Class division
        class_div_label=Label(class_student,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="read only")
        div_combo["values"]=("","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        

    #Roll No
        Roll_no_label=Label(class_student,text="Roll No",font=("times new roman",12,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_no_entry=ttk.Entry(class_student,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    #Gender
        gender_label=Label(class_student,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

       
        gender_combo=ttk.Combobox(class_student,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="read only")
        gender_combo["values"]=("","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


    

    #DoB
        dob_label=Label(class_student,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


    #Email
        email_label=Label(class_student,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

    

    #Phone no
        phone_label=Label(class_student,text="Phone NO",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


    #Address
        address_label=Label(class_student,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

    

    #Teacher name
        teacher_label=Label(class_student,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)




    #redio butttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=6,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student,text="No Photo Sample",variable=self.var_radio1,value="no")
        radiobtn2.grid(row=6,column=1)

    
    #btn frame
        btn_frame=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=760,height=37)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=20,font=("times new roman",12,"bold"),bg="grey",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=20,font=("times new roman",12,"bold"),bg="grey",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=20,font=("times new roman",12,"bold"),bg="grey",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",12,"bold"),bg="grey",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_student,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=300,width=760,height=37)
    
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=41,font=("times new roman",12,"bold"),bg="grey",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",command=self.generate_dataset,width=41,font=("times new roman",12,"bold"),bg="grey",fg="white")
        update_photo_btn.grid(row=0,column=1)


     # right lable frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RAISED,text="Student Details",font=("times new roman",12,"bold"))  
        right_frame.place(x=800,y=10,width=740,height=700)


        img_path = r"imgs\mask.jpg"
        img_right = Image.open(img_path)
        img_right = img_right.resize((770, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        bg_img= Label(right_frame, image=self.photoimg_right)
        bg_img.place(x=5, y=0, width=770, height=130)
   
     #**********search system**********
        
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RAISED,text="Search System",font=("times new roman",12,"bold"))  
        search_frame.place(x=5,y=135,width=730,height=70)

        search_label=Label(search_frame,text="Search By :",font=("times new roman",15,"bold"),bg="skyblue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="read only")
        search_combo["values"]=("Select ","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=18,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=13,font=("times new roman",12,"bold"),bg="grey",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=13,font=("times new roman",12,"bold"),bg="grey",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

    #********table frame*********
        
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RAISED)
        table_frame.place(x=5,y=210,width=730,height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","add","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Deparment")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("add",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("add",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
   

    #***********function declaration******
    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are reuired",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database=" face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()
                                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Succes","Student Details Has Been Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :(str(es))",parent=self.root)



    #***************fetch data***********
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="root",database=" face_recogniser")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()

         if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i )
             conn.commit()
         conn.close()

    #***************get cursor*************
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        if data:  # Check if data is not empty
                # Make sure data has enough elements before setting variables
            if len(data) >= 15:
                self.var_dep.set(data[0])
                self.var_course.set(data[1])
                self.var_year.set(data[2])
                self.var_semester.set(data[3])
                self.var_std_id.set(data[4])
                self.var_std_name.set(data[5])
                self.var_div.set(data[6])
                self.var_roll.set(data[7])
                self.var_gender.set(data[8])
                self.var_dob.set(data[9])
                self.var_email.set(data[10])
                self.var_phone.set(data[11])
                self.var_address.set(data[12])
                self.var_teacher.set(data[13])
                self.var_radio1.set(data[14])
            else:
             # Handle case where data doesn't have enough elements
             messagebox.showerror("Error", "Insufficient data retrieved", parent=self.root)
        else:
             # Handle case where data is empty
            messagebox.showerror("Error", "No data retrieved", parent=self.root)

    
    #****************update function***********
    def update_data(self):
         if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are reuired",parent=self.root)

         else:
             try:
                 Update=messagebox.askyesno("Update","Do You Want To Upadate This Student Details ", parent=self.root)        
                 if Update>0:
                      conn=mysql.connector.connect(host="localhost",username="root",password="root",database=" face_recogniser")
                      my_cursor=conn.cursor()
                      my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                          
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.var_std_id.get()
        
                                                                                                                                                                                             ))
                      
                 else:
                     if not Update:
                        return
                 messagebox.showinfo("Success","Student Details Successfully Update Completed.",parent=self.root)
                 conn.commit()
                 self.fetch_data()
                 conn.close()

             except Exception as es:     
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)




    #*****Delet function**********
    def delete_data(self): 
        if self.var_std_id.get()=="":       
            messagebox.showerror("Error","student id must be required",parent=self.root)  
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do You Want To Delete Data Of The This Student ",parent=self.root)
                if delete>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="root",database=" face_recogniser")
                     my_cursor=conn.cursor()
                     sql="delete from student where Student_id=%s"
                     val=(self.var_std_id.get(),)
                     my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted student details",parent=self.root)   

            except Exception as es:     
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



    #********Reset data****************
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Sele Course ")
        self.var_year.set("Select Year")
        self.var_semester.set("Select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("") 
        self.var_radio1.set("")
                   


    #********Generate Data set or take photo samples****************
    def generate_dataset(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are reuired",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database=" face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("select * FROM student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                          
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                                                                                              ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #**********load predefiend data on face frontals from opencv**************

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!!!!!",parent=self.root)
            except Exception as es:     
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


              
                     



if __name__ == "__main__":
     root = Tk()
     obj = Student(root)
     root.mainloop()

        