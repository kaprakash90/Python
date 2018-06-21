from tkinter import *
import time

def tick():
    cur_time = time.strftime('%H:%M')
    c.config(text=cur_time)
    c.after(10,tick)

ck = Tk()
c = Label(ck, font=('arial', 100, 'bold', 'italic'), bg='lightblue')
c.pack()
tick()
ck.mainloop()
