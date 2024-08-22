from tkinter import *
from time import strftime
# from datetime import *
win=Tk()

def show():
    now=strftime('%Y/%m/%d  %H:%M:%S  %p')
    lbl.config(text=now)
    lbl.after(1000 , show)

lbl=Label(win,bg='darkred',fg='white',font=('tahoma',80))
lbl.pack(anchor='center')

show()
mainloop()






# import os
# os.system('cls')

# import datetime as dt
# time1=dt.datetime.now().year

# shamsi=time1-621
# print(shamsi)

# time2=dt.datetime.now().minute
# print(time2)


# time3=dt.datetime.now().second
# print(time3)

# time4=dt.datetime.now().day
# print(time4)

# time5=dt.datetime.now().month
# print(time5)


# time6=dt.datetime.now()
# print(time6)

# hour1=dt.datetime.now().hour
# minute1=dt.datetime.now().minute

# print(f'{hour1} : {minute1}')

# import time
# new_time=time.strftime('%Y/%m/%d  -( %W : %A )')
# print(new_time)