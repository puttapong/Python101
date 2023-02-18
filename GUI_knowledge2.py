from tkinter import *
from tkinter import ttk #theme of tk

from tkinter import messagebox

import random

GUI = Tk()
GUI.title('คุณเหมือนตัวละครใดในการ์ตูน')
GUI.geometry('500x400')


L1 = Label(GUI,text='คุณเหมือนตัวละครใดในการ์ตูน',font=('Angsana New',30),fg='pink')
L1.place(x=110,y=20)

L2 = Label(GUI,text='โปรดกรอกชื่อ',font=('Angsana New',24),fg='green')
L2.place(x=30,y=70)

name = Entry(GUI)
name.place(x=200,y=90)

cartoon = ['นารูโตะ','โดราเอมอน','ซาสึเกะ','ไจแอนท์','ซึเนโอะ','ชิสุกะ','ชินจัง']
text2 = random.choice(cartoon)

######################
def submit():
    text1 = name.get()
    text2 = random.choice(cartoon)
    L3 = Label(GUI,text=("คุณ ",text1," เหมือน ",text2),font=('Angsana New',24),fg='green')
    L3.place(x=30,y=220)



FB1 = Frame(GUI)
FB1.place(x=200,y=150)

B2 = ttk.Button(FB1,text='ส่งข้อมูล',command=submit)
B2.pack(ipadx=20,ipady=20)

#########################



GUI.mainloop()
