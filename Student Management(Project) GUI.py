from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as a
mydb=a.connect(host="localhost",user="root",password="tiger",database="student",auth_plugin="mysql_native_password")
print(mydb)
def search_entry():
      global q2
      global f2
      f2.forget()
      f2=Frame(root)
      f2.pack(side="top",anchor="nw")
      t=StringVar()
      l1=Label(f2,text="Select your column").grid(row=0,column=0)
      global combobox1
      combobox1=ttk.Combobox(f2,textvariable=t)
      combobox1['values']=["Admission number","Student's Name","Age","Class","Section","Contact","Gender","City","Pin code","Blood group","Nationality","Email id"]
      combobox1.current(0)
      combobox1.grid(row=0,column=1)
      q2=StringVar()
      e1=ttk.Entry(f2, textvariable=q2).grid(row=0,column=2)
      s1=Label(f2,text="").grid(row=1,column=0)
      b=ttk.Button(f2,text="search",command=search).grid(row=2,column=2)
def search():
      sql=""
      cur=mydb.cursor()
      if combobox1.get()=="Admission number":                                                                                                                                   
            sql="Select * from record where Admission_number='"+q2.get()+"'"
      if combobox1.get()=="Student's Name":                                                                                                                                           
            sql="Select * from record where Student_name='"+q2.get()+"'"
      if combobox1.get()=="Age":                                                                                                                                                           
            sql="Select * from record where Age='"+q2.get()+"'"
      if combobox1.get()=="Class":
            sql="Select * from record where class='"+q2.get()+"'"
      if combobox1.get()=="Section":                                                                                                                                                            
            sql="Select * from record where section='"+q2.get()+"'"
      if combobox1.get()=="DOB":                                                                                                                                                         
            sql="Select * from record where DOB='"+q2.get()+"'"
      if combobox1.get()=="Contact":                                                                                                                                                    
            sql="Select * from record where contact='"+q2.get()+"'"
      if combobox1.get()=="Gender":                                                                                                                                        
            sql="Select * from record where gender='"+q2.get()+"'"
      if combobox1.get()=="City":                                                                                                                                             
            sql="Select * from record where city='"+q2.get()+"'"
      if combobox1.get()=="Pin code":                                                                                                                                                
            sql="Select * from record where pin_code='"+q2.get()+"'"
      if combobox1.get()=="Nationality":                                                                                                                                         
            sql="Select * from record where nationality='"+q2.get()+"'"
      if combobox1.get()=="Blood group":
            sql="Select * from record where blood_group='"+q2.get()+"'"
      if combobox1.get()=="Email":                                                                                                                                                     
            sql="Select * from record where email='"+q2.get()+"'"
      if sql=="":
            messagebox.showinfo("","Please enter some value")
      if sql!="":
            cur.execute(sql)
            record=cur.fetchall()
            if len(record)==0:
                  messagebox.showinfo("No found","Record not found")
            if len(record)!=0:
                  for x in record:
                        print("Admission number:",x[0])
                        print("Name:",x[1])
                        print("Father name:",x[2])
                        print("Mother name:",x[3])
                        print("Age:",x[4])
                        print("Class:",x[5])
                        print("Section:",x[6])
                        print("Date of Birth:",x[7])
                        print("Contact:",x[8])
                        print("Gender:",x[10])
                        print("city:",x[11])
                        print("Pin code:",x[12])
                        print("Blood group:",x[9])
                        print("Address:",x[13])
                        print("Nationality:",x[14])
                        print("Email id:",x[15])
                        print('\n')
def update_entry():
      global f2
      f2.forget()
      f2=Frame(root)
      f2.pack(side="top",anchor="nw")
      t=StringVar()
      l1=ttk.Label(f2,text="Admission number").grid(row=0,column=0)
      global combobox
      combobox=ttk.Combobox(f2,textvariable=t)
      combobox['values']=["Admission number","Student's Name","Father's name","Mother's name,""Age","Class","Section","Contact","Gender","City","Pin code","Blood group","Nationality","Email id"]
      combobox.current(0)
      combobox.grid(row=2,column=1)
      e=Label(f2,text="Select your column").grid(row=2,column=0)
      global q1
      q1=StringVar()
      l2=Label(f2,text="Enter the new data").grid(row=4,column=0)
      global t2
      t2=StringVar()
      e2=ttk.Entry(f2, textvariable=t2).grid(row=4,column=1,ipadx=9)
      e1=ttk.Entry(f2, textvariable=q1).grid(row=0,column=1,ipadx=9)
      s1=Label(f2,text="").grid(row=5,column=0)
      b=ttk.Button(f2,text="update",command=update).grid(row=6,column=1)

def update():
      cur=mydb.cursor()
      if combobox.get()=="Admission number":                                                                                                                                 
            sql="update record set Admission_number='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Student's Name":                                                                                                                              
             sql="update record set Student_name='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Father's name":                                                                                                                                            
            sql="update record set Father_name='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Mother's name":                                                                                                                                            
           sql="update record set Mother_name='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Age":                                                                                                                                                           
            sql="update record set Age='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Class":
            sql="update record set Class='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Section":                                                                                                                                                            
            sql="update record set Section='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="DOB":                                                                                                                                                         
            sql="update record set DOB='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Contact":                                                                                                                                                    
            sql="update record set Contact='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Gender":                                                                                                                                        
            sql="update record set Gender='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="City":                                                                                                                                             
            sql="update record set City='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Pin code":                                                                                                                                                
           sql="update record set Pin_code='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Nationality":                                                                                                                                         
           sql="update record setNationality='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Blood group":
            sql="update record set Blood_group='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      if combobox.get()=="Email":                                                                                                                                                     
            sql="update record set Email='"+t2.get()+"'"" where Admission_number='"+q1.get()+"'"
      cur.execute(sql)
      mydb.commit()
def display():
      global f2
      f2.forget()
      f2=Frame(root)
      f2.pack(side="top",anchor="nw")
      cur=mydb.cursor()
      cur.execute("select * from record")
      record=cur.fetchall()
      for x in record:                                                                                                                                                    
                        print("Admission number:",x[0])
                        print("Name:",x[1])
                        print("Father name:",x[2])
                        print("Mother name:",x[3])
                        print("Age:",x[4])
                        print("Class:",x[5])
                        print("Section:",x[6])
                        print("Date of Birth:",x[7])
                        print("Contact:",x[8])
                        print("Gender:",x[10])
                        print("city:",x[11])
                        print("Pin code:",x[12])
                        print("Blood group:",x[9])
                        print("Address:",x[13])
                        print("Nationality:",x[14])
                        print("Email id:",x[15])
                        print('\n')
def Insert_submit():
      cur=mydb.cursor()
      sql="INSERT INTO record values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      val=(u1.get(),u2.get(),u3.get(),u4.get(),u5.get(),u6.get(),u7.get(),u8.get(),u9.get(),u10.get(),u11.get(),u12.get(),u13.get(),u14.get(),u15.get(),u16.get())
      cur.execute(sql,val)
      mydb.commit()
      my=cur.fetchall
      e1.delete(0,END)
      e2.delete(0,"end")
      e3.delete(0,"end")
      e4.delete(0,"end")
      e5.delete(0,"end")
      e6.delete(0,"end")
      e7.delete(0,"end")
      e8.delete(0,"end")
      e9.delete(0,"end")
      e10.delete(0,"end")
      e11.delete(0,"end")
      e12.delete(0,"end")
      e13.delete(0,"end")
      e14.delete(0,"end")
      e15.delete(0,"end")
      e16.delete(0,"end")
      
def Delete_entry():
      global q1
      global f2
      f2.forget()
      f2=Frame(root)
      f2.pack(side="top",anchor="nw")
      e=Label(f2,text="Admission number")
      s1=Label(f2,text="                                      ").grid(row=1,column=0)
      e.grid(row=0,column=0)
      q1=StringVar()
      e1=ttk.Entry(f2, textvariable=q1)
      e1.grid(row=0,column=1)
      b=ttk.Button(f2,text="submit",command=delete)
      b.grid(row=2,column=1)
def delete():
      cur=mydb.cursor()
      if q1.get()=='':
            messagebox.showinfo("","Please enter some value")
      if q1.get()!="":
            sql="Select * from record where Admission_number='"+q1.get()+"'"
            mydb.commit()
            a=messagebox.askquestion("","Do you want to delete")
            if a=="yes":
                  sql="Select * from record where Admission_number='"+q1.get()+"'"
                  mydb.commit()
            if a=="no":
                  pass
def insert():
      global q1
      global f2
      f2.forget()
      f2=Frame(root)
      f2.pack(side="top",anchor="nw")
      a1=Label(f2,text="Admission number")
      a1.grid(row=0,column=1)
      a2=Label(f2,text="Student's name")
      a2.grid(row=1,column=1)
      a3=Label(f2,text="Father's name")
      a3.grid(row=2,column=1)
      a4=Label(f2,text="Mother's name").grid(row=3,column=1)
      a5=Label(f2,text="Age").grid(row=4,column=1)
      a6=Label(f2,text="Class").grid(row=5,column=1)
      a7=Label(f2,text="Section").grid(row=6,column=1)
      a8=Label(f2,text="DOB(DD/MM/YYYY)").grid(row=7,column=1)
      a9=Label(f2,text="Contact number").grid(row=8,column=1)
      a10=Label(f2,text="Blood group").grid(row=9,column=1)
      a11=Label(f2,text="Gender(M/F)").grid(row=10,column=1)
      a12=Label(f2,text="City").grid(row=11,column=1)
      a13=Label(f2,text="Pin Code").grid(row=12,column=1)
      a14=Label(f2,text="Address").grid(row=13,column=1)
      a15=Label(f2,text="Nationality").grid(row=14,column=1)
      a16=Label(f2,text="Email").grid(row=15,column=1)
      global u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16
      u1=StringVar()
      u2=StringVar()
      u3=StringVar()
      u4=StringVar()
      u5=StringVar()
      u6=StringVar()
      u7=StringVar()
      u8=StringVar()
      u9=StringVar()
      u10=StringVar()
      u11=StringVar()
      u12=StringVar()
      u13=StringVar()
      u14=StringVar()
      u15=StringVar()
      u16=StringVar()
      global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16
      e1=ttk.Entry(f2, textvariable=u1)
      e1.grid(row=0,column=10,ipadx=8)
      e2=ttk.Entry(f2,textvariable=u2)
      e2.grid(row=1,column=10,ipadx=8)
      e3=ttk.Entry(f2,textvariable=u3)
      e3.grid(row=2,column=10,ipadx=8)
      e4=ttk.Entry(f2,textvariable=u4)
      e4.grid(row=3,column=10,ipadx=8)
      e5=ttk.Entry(f2,textvariable=u5)
      e5.grid(row=4,column=10,ipadx=8)
      e6=ttk.Combobox(f2,textvariable=u6)
      e6['value']=['1','2','3','4','5','6','7','8','9','10','11','12']
      e6.grid(row=5,column=10)
      e7=ttk.Combobox(f2,textvariable=u7)
      e7['value']=["A","B","C"]
      e7.grid(row=6,column=10)
      e8=ttk.Entry(f2,textvariable=u8)
      e8.grid(row=7,column=10,ipadx=8)
      e9=ttk.Entry(f2,textvariable=u9)
      e9.grid(row=8,column=10,ipadx=8.34)
      e10=ttk.Combobox(f2,textvariable=u10)
      e10['value']=["A+",'B+',"AB+","O+","A-","B-","AB-","o-"]
      e10.grid(row=9,column=10)
      e11=ttk.Combobox(f2,textvariable=u11)
      e11['value']=["M","F"]
      e11.grid(row=10,column=10)
      e12=ttk.Entry(f2,textvariable=u12)
      e12.grid(row=11,column=10,ipadx=8)
      e13=ttk.Entry(f2,textvariable=u13)
      e13.grid(row=12,column=10,ipadx=8)
      e14=ttk.Entry(f2,textvariable=u14)
      e14.grid(row=13,column=10,ipadx=8)
      e15=ttk.Entry(f2,textvariable=u15)
      e15.grid(row=14,column=10,ipadx=8)
      e16=ttk.Entry(f2,textvariable=u16)
      e16.grid(row=15,column=10,ipadx=8)
      s1=Label(f2,text="").grid(row=16,column=0)
      b6=ttk.Button(f2,text="Submit",command=Insert_submit).grid(row=17,column=10)
      

root=Tk()                                                       

root.title("Student information management")
root.geometry("640x480")
f1=Frame(root)
f1.pack(side="left",anchor='nw')
f2=Frame(root)
f2.pack(side="top",anchor="nw")
b1=Button(f1,text="Insert",command=insert,padx=34)
b1.grid(row=0,column=0)
b2=Button(f1,text="Delete",command=Delete_entry,padx=32)
b2.grid(row=1,column=0)
b3=Button(f1,text="Search",command=search_entry,padx=30.5)
b3.grid(row=2,column=0)
b4=Button(f1,text="Update",command=update_entry,padx=30.456)
b4.grid(row=3,column=0)
b5=Button(f1,text="Display all record ",command=display,padx=3)
b5.grid(row=4,column=0)

root.mainloop()
