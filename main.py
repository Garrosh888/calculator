from tkinter import *

def get_rgb(rgb): #преоброзования цвeта rgb в 16 ричный вид
    return "#%02x%02x%02x" % rgb

def click_button(value,type):
    global indx,last_value
    if last_value is None and type =="operation":
        return
    etry1.insert(indx,value)#insert - вставка, 0 - на начальную позицию, value - значение для вставки
    indx = indx+1
    last_value = type

def clear_C(event):
    global indx,last_value
    last_value = None
    etry1.delete(0,END)
    indx = 0
def enter_button(button):
    button["bg"] = get_rgb((130,0,160))

def leave_button(button):
    button["bg"] = get_rgb((70, 0, 130))

last_value = None
window = Tk()
canv = Canvas(window,height=500,width = 350)
canv.pack()
window.resizable(0,0)
window.iconbitmap("iconka.ico")
window.title("ritka")
color0 = get_rgb((75,0,130))
indx = 0 #позиция в елементе etry1, 0 типо с самого лево

btn1 = Button(canv,text="0",font=(None,24),width=10, bg=color0)
btn1.place(x=0,y=445)
btn1.bind("<Button-1>",lambda event:click_button("0","number"))
btn1.bind("<Enter>",lambda event:enter_button(btn1))
btn1.bind("<Leave>",lambda event:leave_button(btn1))
btn2 = Button(canv, text=",", font=(None, 31), width=2,bg=color0)
btn2.bind("<Enter>",lambda event:enter_button(btn2))
btn2.bind("<Leave>",lambda event:leave_button(btn2))
btn2.place(x=295, y=443)
btn2.bind("<Button-1>", lambda event:click_button(",","zapeta"))
btn4 = Button(canv, text="1", font=(None, 24), width=3,bg= color0)
btn4.place(x=0, y=380)
btn4.bind("<Button-1>", lambda event:click_button("1","number"))
btn4.bind("<Enter>",lambda event:enter_button(btn4))
btn4.bind("<Leave>",lambda event:leave_button(btn4))
btn5 = Button(canv, text="2", font=(None, 24), width=3,bg=color0)
btn5.place(x=67, y=380)
btn5.bind("<Enter>",lambda event:enter_button(btn5))
btn5.bind("<Leave>",lambda event:leave_button(btn5))
btn5.bind("<Button-1>", lambda event:click_button("2","number"))
btn6 = Button(canv, text="3", font=(None, 24), width=3,bg=color0)
btn6.place(x=135, y=380)
btn6.bind("<Enter>",lambda event:enter_button(btn6))
btn6.bind("<Leave>",lambda event:leave_button(btn6))
btn6.bind("<Button-1>", lambda event:click_button("3","number"))
btn7 = Button(canv, text="4", font=(None, 24), width=3,bg=color0)
btn7.place(x=0, y=320)
btn7.bind("<Enter>",lambda event:enter_button(btn7))
btn7.bind("<Leave>",lambda event:leave_button(btn7))
btn7.bind("<Button-1>", lambda event:click_button("4","number"))
btn8 = Button(canv, text="5", font=(None, 24), width=3,bg=color0)
btn8.place(x=67, y=320)
btn8.bind("<Enter>",lambda event:enter_button(btn8))
btn8.bind("<Leave>",lambda event:leave_button(btn8))
btn8.bind("<Button-1>", lambda event:click_button("5","number"))
btn9 = Button(canv, text="6", font=(None, 24), width=3,bg=color0)
btn9.place(x=135, y=320)
btn9.bind("<Enter>",lambda event:enter_button(btn9))
btn9.bind("<Leave>",lambda event:leave_button(btn9))
btn9.bind("<Button-1>", lambda event:click_button("6","number"))
btn10 = Button(canv, text="7", font=(None, 24), width=3,bg=color0)
btn10.place(x=0, y=260)
btn10.bind("<Enter>",lambda event:enter_button(btn10))
btn10.bind("<Leave>",lambda event:leave_button(btn10))
btn10.bind("<Button-1>", lambda event:click_button("7","number"))
btn11 = Button(canv, text="8", font=(None, 24), width=3,bg=color0)
btn11.place(x=67, y=260)
btn11.bind("<Enter>",lambda event:enter_button(btn11))
btn11.bind("<Leave>",lambda event:leave_button(btn11))
btn11.bind("<Button-1>", lambda event:click_button("8","number"))
btn12 = Button(canv, text="9", font=(None, 24), width=3,bg=color0)
btn12.place(x=135, y=260)
btn12.bind("<Enter>",lambda event:enter_button(btn12))
btn12.bind("<Leave>",lambda event:leave_button(btn12))
btn12.bind("<Button-1>", lambda event:click_button("9","number"))
btn13 = Button(canv, text="+", font=(None, 24), width=3,bg=color0)
btn13.place(x=203, y=320)
btn13.bind("<Enter>",lambda event:enter_button(btn13))
btn13.bind("<Leave>",lambda event:leave_button(btn13))
btn13.bind("<Button-1>", lambda event:click_button("+","operation"))
btn14 = Button(canv, text="-", font=(None, 24), width=3,bg=color0)
btn14.place(x=203, y=381)
btn14.bind("<Enter>",lambda event:enter_button(btn14))
btn14.bind("<Leave>",lambda event:leave_button(btn14))
btn14.bind("<Button-1>", lambda event:click_button("-","minus"))
btn15 = Button(canv, text="÷", font=(None, 24), width=4,bg=color0)
btn15.place(x=270, y=381)
btn15.bind("<Enter>",lambda event:enter_button(btn15))
btn15.bind("<Leave>",lambda event:leave_button(btn15))
btn15.bind("<Button-1>", lambda event:click_button("÷","operation"))
btn16 = Button(canv, text="x", font=(None, 24), width=4,bg=color0)
btn16.place(x=270, y=320)
btn16.bind("<Enter>",lambda event:enter_button(btn16))
btn16.bind("<Leave>",lambda event:leave_button(btn16))
btn16.bind("<Button-1>", lambda event:click_button("x","operation"))
bnt17 = Button(canv,text="C",font=(None,24),width=8,bg=color0)
bnt17.place(x=202,y=260)
bnt17.bind("<Enter>",lambda event:enter_button(bnt17))
bnt17.bind("<Leave>",lambda event:leave_button(bnt17))
bnt17.bind("<Button-1>",clear_C)
btn18 = Button(canv, text="=", font=(None, 24), width=5, bg=color0)
btn18.place(x=200, y=445)
btn18.bind("<Button-1>", lambda event:click_button("=","equals"))
btn18.bind("<Enter>", lambda event:enter_button(btn18))
btn18.bind("<Leave>", lambda event:leave_button(btn18))

etry1 = Entry(canv,font= (None,27),width=15)
etry1.place(x=25,y=150)



window.mainloop()