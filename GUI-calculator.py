# GUI-calulator.py

from tkinter import *
from tkinter import ttk, messagebox # จะทำให้ UI ของเราสวยมากขึ้น

GUI = Tk() # สร้าง GUI
GUI.title('โปรแกรมคำนวณ เวลา Render') 
GUI.geometry('500x800')

bg = PhotoImage(file='Logo-Draft.png')

BG = Label(GUI, image=bg)
BG.pack(pady=30)



L1 = Label(GUI,text='กำหนดเวลา Render(ชั่วโมง)',font=(None,20))
L1.pack(pady=20)

v_quantiry1 = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_quantiry1, font=(None,20))
E1.pack()



L2 = Label(GUI,text='จำนวนเครื่อง Render',font=(None,20))
L2.pack(pady=20)

v_quantiry2 = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E2 = ttk.Entry(GUI, textvariable=v_quantiry2, font=(None,20))
E2.pack()



L3 = Label(GUI,text='จำนวน Frame',font=(None,20))
L3.pack(pady=20)

v_quantiry3 = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E3 = ttk.Entry(GUI, textvariable=v_quantiry3, font=(None,20))
E3.pack()

L4 = Label(GUI,text='Test Render 1 Frame(นาที)',font=(None,20))
L4.pack(pady=20)

v_quantiry4 = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E4 = ttk.Entry(GUI, textvariable=v_quantiry4, font=(None,20))
E4.pack()


def Cal():
    try:
        fix_time = int(v_quantiry1.get())
        N_Render = int(v_quantiry2.get())
        frames = int(v_quantiry3.get())
        Render_1_Frame = int(v_quantiry4.get())

        calc1 = (fix_time * 60 * N_Render) // frames
        calc2_01 = ((frames * Render_1_Frame) / N_Render) // 60
        calc2_02 = ((frames * Render_1_Frame) / N_Render) % 60
        calc3 = '{} ชั่วโมง : {} นาที'.format(int(calc2_01),round(calc2_02))

        messagebox.showinfo('ผลลัพธ์','1 Frame เวลาเฉลี่ย Render ต้องไม่เกิน {} นาที \n\nเวลาที่ใช้ Render ทั้งหมด {} '.format(calc1,calc3))
        E1.focus()
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        E1.focus()


B = ttk.Button(GUI, text='คำนวน', command=Cal)
B.pack(ipadx=30,ipady=20,pady=20) #ipadx ขยายความกว้าง x/y



GUI.mainloop() # เพื่อให้โปรแกรมรันตลอดเวลา

'''
x = 3.55555555
print(f'{x:.2f}')
'''

