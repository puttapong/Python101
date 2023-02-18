from tkinter import *

root = Tk()

# สร้าง label บอกว่าเป็น input box
label = Label(root, text="กรอกข้อความ:")
label.pack()

# สร้าง input box
entry1 = Entry(root)
entry1.pack()

entry2 = Entry(root)
entry2.pack()

# ฟังก์ชั่นสำหรับเมื่อกดปุ่ม submit
def submit():
    text1 = entry1.get()  # รับค่าจาก input box
    text2 = entry2.get()  # รับค่าจาก input box
    print("ข้อความที่รับได้คือ:", text1,' ',text2)

# สร้างปุ่ม submit
button = Button(root, text="Submit", command=submit)
button.pack()

root.mainloop()
