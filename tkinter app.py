from new_rest import get_cur_read
from tkinter import *
from tkinter import font
from threading import Thread
from requests import put,post

def func():
    global curr_label,v1

    print("Thread function started!!")
    # post("http://balarubinan.pythonanywhere.com/lin",{"reading":"reset"})
    # print("After server reset")
    while(True):
    # curr
        current_val=get_cur_read()
        curr_label['text']=v1.get()
        post("http://balarubinan.pythonanywhere.com/lin",{"reading":v1.get()})
        curr_label.pack()

root=Tk()
root.geometry('500x500')
curr_label=Label(root,text="Null",font=font.Font(size=35))
curr_label.pack()
v1=DoubleVar()
s1 = Scale( root, variable = v1,
           from_ = 1, to = 100,
           orient = HORIZONTAL)
s1.pack()
t=Thread(target=func)
t.start()
root.mainloop()