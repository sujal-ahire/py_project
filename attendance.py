from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")

      ##############variables ##########

        self.var_atten_id=StringVar() 
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar() 
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        tilte_lbl=Label(self.root,text="ATTENDANCE MANGMENT SYSTEM",font=("new times roman",35,"bold"),bg="black",fg="silver")
        tilte_lbl.place(x=0,y=0,width=1600,height=45)

        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1560,height=780)
        
    # left lable frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RAISED,text="Student Attendance Details",font=("times new roman",12,"bold"))  
        left_frame.place(x=10,y=10,width=780,height=700)

        img_path = r"imgs\bg1.jpg"
        img_left = Image.open(img_path)
        img_left = img_left.resize((1600, 900))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        bg_img= Label(left_frame, image=self.photoimg_left)
        bg_img.place(x=5, y=0, width=770, height=130)

        left_inside=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside.place(x=0,y=135,width=770,height=400)

      #  label and entry
        # attendance id
        attendanceId_label=Label(left_inside,text="Attendance ID :",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # roll
        roll_label=Label(left_inside,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)

         # Name
        name_label=Label(left_inside,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,pady=8)

          # Department
        deplabel=Label(left_inside,text="Department:",font=("times new roman",12,"bold"),bg="white")
        deplabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)

          # Time
        timelabel=Label(left_inside,text="Time:",font=("times new roman",12,"bold"),bg="white")
        timelabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,pady=8)

          # Date
        datelabel=Label(left_inside,text="Date:",font=("times new roman",12,"bold"),bg="white")
        datelabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,pady=8)

          # Attendamce
        attendancelabel=Label(left_inside,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendancelabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside,width=20,textvariable=self.var_atten_attendance,font="comicsansans 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #btn frame
        btn_frame=Frame(left_inside,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=350,width=760,height=37)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=20,font=("times new roman",12,"bold"),bg="grey",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=20,font=("times new roman",12,"bold"),bg="grey",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=20,font=("times new roman",12,"bold"),bg="grey",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=20,command=self.reset_data,font=("times new roman",12,"bold"),bg="grey",fg="white")
        reset_btn.grid(row=0,column=3)


    # right lable frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RAISED,text="Attendance Details",font=("times new roman",12,"bold"))  
        right_frame.place(x=800,y=10,width=740,height=700)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=720,height=520)

        #*********scrollbar table****

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #############fetch data#######\\
        
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    ######import csv

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("csv File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #######Export
    def exportCsv(self):
      try:
        if len(mydata)<1:
         messagebox.showerror("No Data","No Data Found to export",parent=self.root)
         return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("csv File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
           exp_write=csv.writer(myfile,delimiter=",")
           for i in mydata:
              exp_write.writerow(i)
              messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"Successfly")
           
      except Exception as es:     
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


        
        
        
        
          



if __name__ == "__main__":
     root = Tk()
     obj = Attendance(root)
     root.mainloop()
