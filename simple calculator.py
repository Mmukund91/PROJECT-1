from tkinter import *
root=Tk()
root.title("SIMPLE CALCULATOR")
e=Entry(root,width=50,borderwidth=10,bg="blue",fg="yellow")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10 )
e.get()
#e.insert(0,"Enter the Number")

def Add(number):
    c=e.get()
    e.delete(0,END)
    e.insert(0,str(c)+str(number))

def clear():
    e.delete(0,END)
    return
def ADDS():
    p=e.get()
    global fnum
    global math
    math="addition"

    fnum=int(p)
    e.delete(0,END)


def sub():
    p = e.get()
    global fnum
    global math
    math = "subtraction"

    fnum = int(p)
    e.delete(0, END)


def prod():
    p = e.get()
    global fnum
    global math
    math = "multiplication"

    fnum = int(p)
    e.delete(0, END)


def div():
    p = e.get()
    global fnum
    global math
    math = "division"

    fnum = int(p)
    e.delete(0, END)

def equal():
    q=e.get()
    sec_num=int(q)
    e.delete(0,END)
    if math=="addition":
        e.insert(0,fnum+sec_num)
    elif math=="subtraction":
        e.insert(0,fnum-sec_num)
    elif math=="multiplication":
        e.insert(0,fnum*sec_num)
    elif math=="division":
        e.insert(0,fnum/sec_num)




b1=Button(root,text="1",padx=40,pady=40,command=lambda: Add(1),bg="black",fg="red")
b2=Button(root,text="2",padx=40,pady=40,command=lambda: Add(2),bg="black",fg="red")
b3=Button(root,text="3",padx=40,pady=40,command=lambda: Add(3),bg="black",fg="red")
b4=Button(root,text="4",padx=40,pady=40,command=lambda: Add(4),bg="black",fg="red")
b5=Button(root,text="5",padx=40,pady=40,command=lambda: Add(5),bg="black",fg="red")
b6=Button(root,text="6",padx=40,pady=40,command=lambda: Add(6),bg="black",fg="red")
b7=Button(root,text="7",padx=40,pady=40,command=lambda: Add(7),bg="black",fg="red")
b8=Button(root,text="8",padx=40,pady=40,command=lambda: Add(8),bg="black",fg="red")
b9=Button(root,text="9",padx=40,pady=40,command=lambda: Add(9),bg="black",fg="red")
b0=Button(root,text="0",padx=40,pady=40,command=lambda: Add(0),bg="black",fg="red")
bplus=Button(root,text="+",padx=40,pady=40,command=ADDS,bg="black",fg="red")
bequal=Button(root,text="=",padx=40,pady=40,command=equal,bg="black",fg="red")
bclear=Button(root,text="CLEAR",padx=140,pady=40,command=lambda: clear(),bg="black",fg="red")
bsub=Button(root,text="-",padx=40,pady=40,command=sub,bg="black",fg="red")
bprod=Button(root,text="*",padx=40,pady=40,command=prod,bg="black",fg="red")
bdiv=Button(root,text="/",padx=40,pady=40,command=div,bg="black",fg="red")




b1.grid(row=3 ,column=0)
b2.grid(row=3 ,column=1)
b3.grid(row=3 ,column=2)

b4.grid(row=2 ,column=0)
b5.grid(row=2 ,column=1)
b6.grid(row=2 ,column=2)

b7.grid(row=1 ,column=0)
b8.grid(row=1 ,column=1)
b9.grid(row=1 ,column=2)

b0.grid(row=4 ,column=1)
bplus.grid(row=4 ,column=0)
bequal.grid(row=4 ,column=2)
bclear.grid(row=6 ,column=0,columnspan=9)
bsub.grid(row=5 ,column=0 )
bprod.grid(row=5 ,column=1)
bdiv.grid(row=5 ,column= 2)
root.mainloop()