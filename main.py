from tkinter import *

def get_rgb(rgb): #преоброзования цвeта rgb в 16 ричный вид
    return "#%02x%02x%02x" % rgb
def click_button(value):
    global indx
    etry1.insert(indx,value)#insert - вставка, 0 - на начальную позицию, value - значение для вставки
    indx = indx+1
def click_0(event):
    click_button(0)
def click_1(event):
    click_button(1)
def clear_C(event):
    global indx
    etry1.delete(0,END)
    indx = 0

window = Tk()
canv = Canvas(window,height=500,width = 350)
canv.pack()
window.resizable(0,0)
color0 = get_rgb((75,0,130))
indx = 0
btn1 = Button(canv,text="0",font=(None,24),width=15, bg=color0)
btn1.place(x=0,y=445)
btn1.bind("<Button-1>",click_0)
bnt2 = Button(canv,text=",",font=(None,31),width=2)
bnt2.place(x=295,y=443)
bnt4 = Button(canv,text="1",font=(None,24),width=3)
bnt4.place(x=0,y=380)
bnt4.bind("<Button-1>",click_1)
bnt5 = Button(canv,text="2",font=(None,24),width=3)
bnt5.place(x=67 ,y=380)
bnt6 = Button(canv,text="3",font=(None,24),width=3)
bnt6.place(x=135,y=380)
bnt7 = Button(canv,text="4",font=(None,24),width=3)
bnt7.place(x=0,y=320)
bnt8 = Button(canv,text="5",font=(None,24),width=3)
bnt8.place(x=67,y=320)
bnt9 = Button(canv,text="6",font=(None,24),width=3)
bnt9.place(x=135,y=320)
bnt10 = Button(canv,text="7",font=(None,24),width=3)
bnt10.place(x=0,y=260)
bnt11 = Button(canv,text="8",font=(None,24),width=3)
bnt11.place(x=67,y=260)
bnt12 = Button(canv,text="9",font=(None,24),width=3)
bnt12.place(x=135,y=260)
bnt13 = Button(canv,text="+",font=(None,24),width=3)
bnt13.place(x=203,y=320)
bnt14 = Button(canv,text="-",font=(None,24),width=3)
bnt14.place(x=203,y=381)
bnt15 = Button(canv,text="÷",font=(None,24),width=4)
bnt15.place(x=270,y=381)
bnt16 = Button(canv,text="x",font=(None,24),width=4)
bnt16.place(x=270,y=320)
bnt17 = Button(canv,text="C",font=(None,24),width=8)
bnt17.place(x=202,y=260)
bnt17.bind("<Button-1>",clear_C)
etry1 = Entry(canv,font= (None,20))
etry1.place(x=25,y=150)



window.mainloop()