from tkinter import *
from tkinter import ttk
from backend import *



def view_am():
    list1.delete(0,END)
    for row in view_m():
        list1.insert(END,row)

def rech_s():
    list1.delete(0,END)
    for row in showdf():
        list1.insert(END,row)


def popup():
    popup = Toplevel()
    popup.title("details")
    popup.geometry("500x100")
    label11=Label(popup,text="testtesttesttest")
    label11.grid(row=2,column=2)

def clear():
    list1.delete(0,END)

window=Tk()
window.title("calendrier de maintenance")
#window.maxsize(400,400)    # to define later
l1=Label(window,text='date')
l1.grid(row=0,column=0)
l2=Label(window,text='service')
l2.grid(row=1,column=0)


date=StringVar()
e1=Entry(window,textvariable=date,bd=3)
e1.grid(row=0,column=1)

service=StringVar()
#e1=Entry(window,textvariable=service,bd =3)   //it's been replaced with a combobox

e1=ttk.Combobox(window, width = 27, textvariable = service)
e1['values']=("",'TRANS','DET')
e1.grid(row=1,column=1)



list1=Listbox(window,height=30,width=100)
list1.grid(row=2,column=0,rowspan=10,columnspan=3)
sb1=Scrollbar(window)
sb1.grid(row=3,column=3,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="rechercher par date",width=25)
b1.grid(row=0,column=2)
b4=Button(window,text="rechercher par service",width=25,command=rech_s)
b4.grid(row=1,column=2)
b2=Button(window,text="afficher tous",width=12,command=view_am)
b2.grid(row=3,column=4)
b3=Button(window,text="clear",width=12, command=clear)
b3.grid(row=5,column=4)
b3=Button(window,text="détails",width=12, command=popup)
b3.grid(row=4,column=4)








boudara=Label(window,text='Created by : EV1 BOUDARA')
boudara.grid(row=12,column=4)




 #needs the PIL module which work only in v_p<3
widget=Label(window)
widget.img = PhotoImage(file="ins.png")
widget.grid(row=10,column=4)
widget['text'] = "ins.png"
widget['image'] = widget.img

#img.grid(row=10,column=4)


window.mainloop()
