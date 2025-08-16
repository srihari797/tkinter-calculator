from tkinter import *
root=Tk()

e=Entry(root,width=50,border=4)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
  
def cal(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    
def clear():
    e.delete(0,END)

def operator(op):
    first_num=e.get()
    global first,symbol
    symbol=op
    first=int(first_num)
    e.delete(0,END)    

def equal():
    second_num=e.get()
    global second
    second=int(second_num)
    e.delete(0,END)
    if symbol=="+":
        e.insert(0,first+second)
    elif symbol=="-":
        e.insert(0,first-second)
    elif symbol=="*":
        e.insert(0,first*second)
    elif symbol=="/":
        if second !=0:
            e.insert(0,first//second)     
        else:
            e.insert(0,"Error")           
   
    
    

    
button1=Button(root,text="1",padx=40,pady=20,command=lambda: cal(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda: cal(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda: cal(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda: cal(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda: cal(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda: cal(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda: cal(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda: cal(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda: cal(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda: cal(0))
addbutton=Button(root,text="+",padx=40,pady=20,command=lambda: operator("+"))
subbutton=Button(root,text="-",padx=40,pady=20,command=lambda: operator("-"))
mulbutton=Button(root,text="*",padx=40,pady=20,command=lambda: operator("*"))
divisionbutton=Button(root,text="/",padx=40,pady=20,command=lambda: operator("/"))
equalsbutton=Button(root,text="=",padx=40,pady=20,command=lambda: equal())
clearsbutton=Button(root,text="Clear",padx=40,pady=20,command=lambda: clear())




button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
divisionbutton.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
mulbutton.grid(row=2,column=3)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
addbutton.grid(row=3,column=3)

button0.grid(row=4,column=0)
equalsbutton.grid(row=4,column=1)
clearsbutton.grid(row=4,column=2)
subbutton.grid(row=4,column=3)


mylabel=Label(root,text="").grid(row=5,column=2)



root.mainloop()