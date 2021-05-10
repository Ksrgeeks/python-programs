from tkinter import *
import time

def timing() :
    t= 1
    for t in range(1 , 10) :
        txt.delete(0,END)
        txt.insert(INSERT,t)
        t+=1
        time.sleep(1)
        
if __name__ == '__main__':
    root = Tk()
    root.title("TIMER")
    root.geometry("250x150")
    tx = StringVar()
    txt = Entry(root,textvariable=tx,width=10)
    txt.grid(row=0 , column=0)
    timing()
    root.mainloop()
