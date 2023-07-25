# GUI-calulator.py

from tkinter import *
from tkinter import ttk, messagebox # จะทำให้ UI ของเราสวยมากขึ้น

GUI = Tk() # สร้าง GUI
GUI.title('โปรแกรมคำนวณ เวลา Render') 
GUI.geometry('700x600')

bg = PhotoImage(file='Logo-Draft.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='จำนวน Frame ที่เวลา 8 ชั่วโมง',font=(None,20))
L.pack()

v_quantiry = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantiry, font=(None,20))
E1.pack()

def Cal():
    fixtime_per_minute = int(v_quantiry.get())
    calc = (8 * 60 * 5) // fixtime_per_minute 
    messagebox.showinfo('ผลลัพธ์','1 Frame เวลาเฉลี่ย Render ต้องไม่เกิน {} นาที'.format(calc))

'''
8 คือ Frame ที่เวลา 8 ชั่วโมง
ุ60 คือแปลงหน่วยจากชั่วโมงให้เป็นนาที
5 คือ จำนวนเครื่องที่เรนเดอร์
'''


B = ttk.Button(GUI, text='คำนวน', command=Cal)
B.pack(ipadx=30,ipady=20) #ipadx ขยายความกว้าง x/y


GUI.mainloop() # เพื่อให้โปรแกรมรันตลอดเวลา