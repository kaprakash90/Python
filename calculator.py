from tkinter import *

calc = Tk()
calc.title('My calc!')
txtip = ''

def clk(num):
    global txtip
    txtip = txtip + str(num)
    ip.set(txtip)

def rset():
    global txtip
    txtip = ''
    ip.set(txtip)

def opequal():
    global txtip
    res = str(eval(txtip))
    ip.set(res)

ip = StringVar()
displayarea = Entry(calc, font=('arial', 15, 'italic','bold'), textvariable = ip, bd=5, insertwidth = 2, bg = 'lightgreen', justify = 'right').grid(columnspan=3)
but1 = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='1', command = lambda:clk('1')).grid(row=1, column=0)
but2 = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='2', command = lambda:clk('2')).grid(row=1, column=1)
but3 = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='3', command = lambda:clk('3')).grid(row=1, column=2)

but4 = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='4', command = lambda:clk('4')).grid(row=2, column=0)
but5 = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='5', command = lambda:clk('5')).grid(row=2, column=1)
but6 = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='6', command = lambda:clk('6')).grid(row=2, column=2)

but7 = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='7', command = lambda:clk('7')).grid(row=3, column=0)
but8 = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='8', command = lambda:clk('8')).grid(row=3, column=1)
but9 = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='9', command = lambda:clk('9')).grid(row=3, column=2)

butrs = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='C', command = lambda:rset()).grid(row=4, column=2)

butad = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='+', command = lambda:clk('+')).grid(row=4, column=1)
butmi = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='-', command = lambda:clk('-')).grid(row=4, column=0)

butmi = Button(calc, padx = 16, bd = 5, fg='red', bg = 'lightblue', font=('arial', 15, 'bold'), text='=', command = opequal).grid(row=5, column=1)


mainloop()
