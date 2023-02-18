from tkinter import *
from tkinter import ttk #theme of tk

from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

#B1 = ttk.Button(GUI,text='เงินมีอยู่กี่่บาท')
#B1.pack(ipadx=20,ipady=20) 


L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

######################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
   # messagebox.showerror('เงินในบัญชี',text)

FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=100,y=80)

B2 = ttk.Button(FB1,text='เงินมีอยู่กี่่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
#B2.place(x=50,y=200)
#########################


entry1 = Entry(GUI)
entry1.pack()


def Button3():
    #text = 'Python 101, Math'
    text = entry1.get()
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)
   # messagebox.showerror('เงินในบัญชี',text)

FB2 = Frame(GUI)#คล้ายกระดาน
FB2.place(x=100,y=180)

B3 = ttk.Button(FB1,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)










GUI.mainloop()
