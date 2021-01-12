from tkinter import *
from tkinter import font
from threading import Thread
from requests import post
from time import sleep

i=0
def func():
    global curr_label,v1

    print("Thread function started!!")
    # post("http://balarubinan.pythonanywhere.com/lin",{"reading":"reset"})
    # print("After server reset")
    while(True):
        global i
        curr_label['text']=v1.get()
        val=100
        # val=str(v1.get()/100)
        if i%2==0:
            val=post("http://127.0.0.1:5000/rot/reading")
            print("Resonse codde ",val)
        i+=1
        sleep(2)
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

# val=post("http://balarubinan.pythonanywhere.com/lin/"+"57")
# print(val)