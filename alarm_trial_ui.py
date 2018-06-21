from playsound import *
import datetime, time
from tkinter import *


ip=time.strftime('%H:%M:%S')

def tick():
    now=time.strftime('%H:%M:%S')
    ip.set(now)
    c.after(10,tick)


def getval():
    '''
    user can set the time for alarm by giving hour and minute input
    '''
    #get the params for hr and min from user and convert to time
    hour = int(alh.get())
    minute = int(alm.get())

    #check if the time is past already and set the variable for controling the loop to check for starting alarm
    if datetime.time(hour,minute) < datetime.datetime.now().time():
        checkforalarm = False
        print('Hey the time is already past the alarm time :(')
    else:
        checkforalarm = True

    #main alarm func
    while checkforalarm:
        if datetime.time(hour,minute) == datetime.datetime.now().time():
            for i in range(10):
                playsound('/Users/arunprakash/Downloads/beep-4.wav')
                time.sleep(0.5)
            checkforalarm = False

ck = Tk()
ck.title('My Clock!')
ip = StringVar()
c = Entry(ck, font=('arial', 30, 'italic','bold'), textvariable = ip, bd=5,  bg = 'lightgreen', justify = 'right')
c.grid(row=0, columnspan=2)
l1 = Label(ck, text="Hour")
l1.grid(row=1, column=0)
l2 = Label(ck, text="Minute")
l2.grid(row=2, column=0)
alh = Entry(ck, font=('arial', 15, 'bold', 'italic'), bg='lightgreen')
alh.grid(row=1, column=1)
alm = Entry(ck, font=('arial', 15, 'bold', 'italic'), bg='lightgreen')
alm.grid(row=2, column=1)
but1 = Button(ck, bd = 5, fg='red', bg = 'lightgreen', font=('arial', 15, 'bold'), text='set', command = lambda:getval())
but1.grid(row=3)
tick()

ck.mainloop()
