from tkinter import *

def plural():
    number1=int(num1.get())
    number2=int(num2.get())
    result=number1+number2
    lbl_result.config(text=result)

def minus():
    number1=int(num1.get())
    number2=int(num2.get()) 
    result=number1-number2
    lbl_result.config(text=result)

def multiplication():
    number1=int(num1.get())
    number2=int(num2.get())
    result=number1*number2
    lbl_result.config(text=result)

def division():
    number1=int(num1.get())
    number2=int(num2.get())
    result=number1/number2
    lbl_result.config(text=result)

def clear():
    lbl_result.configure(text='')
    num1.delete(0,END)
    num2.delete(0,END)
    num1.focus()



win=Tk()


win.title('Calculator')
win.geometry('300x400+500+200')
win.resizable(0,0)
win.config(bg='skyblue')

num1=Entry(justify='center')
num1.place(x=25,y=10,width=250,height=30)
num1.focus()

num2=Entry(justify='center')
num2.place(x=25,y=50,width=250,height=30)

btn_plural=Button(win, text="+",bg='yellow',fg='black',font=('title',20),command=plural)
btn_plural.place(x=25,y=90,width=40,height=40)

btn_minus=Button(win, text="–",bg='yellow',fg='black',font=('title',20),command=minus)
btn_minus.place(x=70,y=90,width=40,height=40)

btn_multiplication=Button(win, text="×",bg='yellow',fg='black',font=('title',20),command=multiplication)
btn_multiplication.place(x=115,y=90,width=40,height=40)

btn_division=Button(win, text="÷",bg='yellow',fg='black',font=('title',20),command=division)
btn_division.place(x=160,y=90,width=40,height=40)

btn_clear=Button(win, text="clear",bg='red',fg='white',font=('title',15),command=clear)
btn_clear.place(x=210,y=90,width=80,height=40)

lbl_result=Label(win,text='',bg='orange',font=('title',17))
lbl_result.place(x=25,y=250,width=249,height=40)


mainloop()