from tkinter import *  

def interest():
    label_p.grid(row=1 , column=1)
    p.grid(row=1 , column=2)
   
    label_r.grid(row=2 , column=1)
    r.grid(row=2 , column=2)
    
    label_t.grid(row=3 , column=1)
    t.grid(row=3 , column=2)

    find.grid(row=4 , column=1 , columnspan=2)

def check() :
    C.delete(0,END)
    S.delete(0,END)
    principle=p.get()
    principle=int(principle)
    rate=r.get()
    rate=int(rate)
    time=t.get()
    time=int(time)

    Label(top, text="Compound Interest", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic").grid(row=5 , column=1)
    Label(top, text="simple Interest", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic").grid(row=6 , column=1)

    Amount = principle * (pow((1 + rate / 100), time)) 
    CI = Amount - principle
    C.grid(row=5 , column=2)
    C.insert(INSERT,CI)

    si=(principle*rate*time)/100
    S.grid(row=6 , column=2)
    S.insert(INSERT , si)

def hcf_and_lcm() :

    label_num1.grid(row=1 , column=4)
    label_num2.grid(row=2 , column=4)

    num1.grid(row=1 , column=5)
    num2.grid(row=2 , column=5)

    find1.grid(row=4 , column=4 , columnspan=2)

def check1() :
    
    hcf.delete(0,END)
    lcm.delete(0,END)
    
    x=num1.get()
    x=int(x)
    y=num2.get()
    y=int(y)
    
    # for HCF
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            h = i 

    label_hcf.grid(row=6 , column=4)
    hcf.grid(row=6 , column=5)
    hcf.insert(INSERT,h)

    # for LCM
    if x > y:
       greater = x
    else:
       greater = y

    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           l = greater
           break
       greater += 1

    label_lcm.grid(row=5 , column=4)
    lcm.grid(row=5 , column=5)
    lcm.insert(INSERT,l)

    

def power() :
    label_x.grid(row=9 , column=1)
    label_y.grid(row=10 , column=1)

    entry_x.grid(row=9 , column=2)
    entry_y.grid(row=10 , column=2)

    find2.grid(row=11 , column=1, columnspan=2)

    
def check2() :
    power_result.delete(0,END)

    x=entry_x.get()
    x=int(x)
    y=entry_y.get()
    y=int(y)
    
    power_label.grid(row=12 , column=1)
    power_result.grid(row=12 , column=2)

    power=pow(x,y)
    power_result.insert(INSERT,power)
    
def root():
    label_root.grid(row=9 , column=4)
    label_power_root.grid(row=10 , column=4)

    entry_root.grid(row=9 , column=5)
    entry_power_root.grid(row=10 , column=5)

    find3.grid(row=11 , column=4, columnspan=2)
    

def check3() :
    root_power_result.delete(0,END)
    x=entry_root.get()
    x=int(x)
    y=entry_power_root.get()
    y=int(y)
    
    root=x**(1/y)
    root_power_label.grid(row=12 , column=4)
    root_power_result.grid(row=12 , column=5)
    root_power_result.insert(INSERT,root)

# Driver Code 
top = Tk()
top.title("CALCULATOR")
top.geometry("250x200")
#top.configure(bg="yellow")
top["background"]="#ffffff"
  
b1 = Button(top,text = "Simple and Compound Interest",command = lambda: interest(),activeforeground = "yellow",activebackground = "#5D6D7E",pady=10 , width=30, foreground="white", background="#5D6D7E")  
b2 = Button(top, text = "HCF and LCM",command = lambda: hcf_and_lcm(),activeforeground = "blue",activebackground = "#5D6D7E",pady=10 , width=30, foreground="white", background="#5D6D7E")   
#b3 = Button(top, text = "LCM",command = lambda: lcm(),activeforeground = "green",activebackground = "#5D6D7E",pady = 10 , width=30, foreground="white", background="#5D6D7E")    
b4 = Button(top, text = "Powers X^Y",command = lambda: power(),activeforeground = "yellow",activebackground = "#5D6D7E",pady = 10 , width=30, foreground="white", background="#5D6D7E")  
b5 = Button(top, text = "Roots Y√X",command = lambda: root(),activeforeground = "yellow",activebackground = "#5D6D7E",pady = 10 , width=30 , foreground="white" , background="#5D6D7E")  
find = Button(top, text= "CALCULATE INTEREST", command= lambda: check(), width=20, background="#5D6D7E",foreground="white")

# gui for Interest
b1.grid(row=0 , column=0)
b2.grid(row=1 , column=0)
#b3.grid(row=2 , column=0)
b4.grid(row=2 , column=0)
b5.grid(row=3 , column=0)

label_p=Label(top, text="Enter Principle", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")
label_r=Label(top, text="Enter rate", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")
label_t=Label(top, text="Enter Years", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")

p = Entry(top, width=20)
r = Entry(top, width=20)
t = Entry(top, width=20)

C = Entry(top, width=20)
S = Entry(top, width=20)

# gui for HCF and LCM
label_num1=Label(top, text="First Number", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")
label_num2=Label(top, text="Second Number", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")

num1 = Entry(top, width=20)
num2 = Entry(top, width=20)

find1 = Button(top, text= "CALCULATE LCM and HCF", command= lambda: check1(), width=22, background="#5D6D7E",foreground="white")

label_hcf=Label(top, text="HCF", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")
label_lcm=Label(top, text="LCM", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")

hcf = Entry(top, width=20)
lcm = Entry(top, width=20)

# gui for Power
label_x=Label(top, text="Enter X ", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")
label_y=Label(top, text="Enter Y ", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")

entry_x = Entry(top, width=20)
entry_y = Entry(top, width=20)

find2 = Button(top, text= "CALCULATE X^Y", command= lambda: check2(), width=20, background="#5D6D7E",foreground="white")

power_label=Label(top, text=" X^Y ", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")

power_result = Entry(top, width=20)

# gui for power roots
label_root=Label(top, text="Enter X ", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")
label_power_root=Label(top, text="Enter Y", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")

entry_root = Entry(top, width=20)
entry_power_root = Entry(top, width=20)

find3 = Button(top, text= "CALCULATE Y√X", command= lambda: check3(), width=20, background="#5D6D7E",foreground="white")

root_power_label=Label(top, text=" Y√X ", fg="#5D6D7E" , width=20,bg="white",font = "Helvetica 14 bold italic")

root_power_result = Entry(top, width=20)

horizontal_separate=Label(top, text="----------------------------------------------------------------------------", fg="red",bg="white", width=100)
horizontal_separate.grid(row= 8, column=1 , columnspan=5)


top.mainloop()

