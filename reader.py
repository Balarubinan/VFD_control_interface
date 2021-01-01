# from new_rest import get_cur_read
from tkinter import *
from tkinter import font
from threading import Thread
from requests import put,get,post

curent_value=0
root=Tk()

def yielder():
    global curent_value
    return curent_value

def get_val():
    global seconds,cur,curent_value
    post("http://balarubinan.pythonanywhere.com/lin/0")
    while(True):
        val=get("http://balarubinan.pythonanywhere.com/lin/23")
        print(val.json())


        # cur['text']=val.json()['reading']
        curent_value=float(val.json()['reading'])
        # cur.pack()

# cur=Label(root)
# cur.pack()
# seconds=Label(root, text="None yet", font=font.Font(size=25))
# seconds.pack()
t=Thread(target=get_val)
t.start()
# root.mainloop()
