from playsound import *
import datetime, time
from tkinter import *
import tkinter.messagebox


ip=time.strftime('%H:%M:%S')
setalarm = False

def tick():
    global setalarm
    now=time.strftime('%H:%M:%S')
    ip.set(now)
    c.after(10,tick)


    if setalarm:
        h=time.strftime('%H')
        m=time.strftime('%M')
        s=time.strftime('%S')
        t=datetime.time(int(h),int(m),int(s))

        if datetime.time(hour,minute,0) < t:
            setalarm = False
            tkinter.messagebox.showinfo('Something wrong!', 'Ooops! the alarm time is past already.. set a future time!!')

        if datetime.time(hour,minute,0) == t:
            for i in range(10):
                playsound('/Users/arunprakash/Downloads/beep-4.wav')
                time.sleep(0.2)
                setalarm = False


def getval():
    '''
    user can set the time for alarm by giving hour and minute input
    '''
    #get the params for hr and min from user and convert to time
    global setalarm
    global hour
    global minute
    hour = int(alh.get())
    minute = int(alm.get())
    setalarm=True

    #check if the time is past already and set the variable for controling the loop to check for starting alarm


ck = Tk()
ck.title('My Clock!')
ip = StringVar()
c = Entry(ck, font=('arial', 30, 'italic','bold'), textvariable = ip, bd=5,  bg = 'orange', justify = 'right')
c.grid(row=0, columnspan=2)
l1 = Label(ck, text="Hour")
l1.grid(row=1, column=0)
l2 = Label(ck, text="Minute")
l2.grid(row=2, column=0)
alh = Entry(ck, font=('arial', 15, 'bold', 'italic'), bd=5, bg='orange', justify = 'left')
alh.grid(row=1, column=1)
alm = Entry(ck, font=('arial', 15, 'bold', 'italic'), bd=5, bg='orange', justify = 'left')
alm.grid(row=2, column=1)
but1 = Button(ck, bd = 5, fg='red', bg = 'orange', font=('arial', 15, 'bold'), text='set', command = lambda:getval())
but1.grid(row=3, column=0)
but2 = Button(ck, bd = 5, fg='red', bg = 'orange', font=('arial', 15, 'bold'), text='Quit', command = ck.destroy)
but2.grid(row=3, column=1)
tick()

ck.mainloop()
