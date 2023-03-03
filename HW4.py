from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
##############CSV###############
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']


def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
       # for row in fr:
        #    print(row)
        #csv_file.close()

    return data
#############################

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกเวลาเข้างาน') #นี่คือชื่อโปรแกรม
GUI.geometry('360x400') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='ลงเวลาเข้างาน',font=('Angsana New',30),fg='blue')
L1.place(x=100,y=20)


##########SECTION RIGHT##########
LF1 = ttk.LabelFrame(GUI,text='กรอกชื่อพนักงาน เพื่อลงเวลา')
LF1.place(x=80,y=110)

v_data = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',18))
E1.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y/%m/%d - %H:%M:%S  ')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

B4 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B4.pack(ipadx=20,ipady=20)

def Button3():
    text = readcsv()
    messagebox.showinfo('รายชื่อ',text)

FB2 = Frame(GUI) 
FB2.place(x=120,y=280)
B3 = ttk.Button(FB2,text='list รายชื่อ',command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()