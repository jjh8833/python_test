from tkinter import *

expr = ""

def press(num):
	global expr
	expr = expr + str(num)
	eqt.set(expr)

if __name__ == "__main__":

    gui = Tk()
    
    gui.title("계산기")
    # gui.configure(background="#A0A0A0")
    gui.geometry("300x300")

    lb1 = Label(gui, text="계산 : ")
    lb1.grid(row=0, column=0)

    eqt = StringVar()
    expr_fld = Entry(gui, textvariable=eqt)
    expr_fld.grid(row = 0, column=1, ipadx=50)

    lb2 = Label(gui, text="결과 : ")
    lb2.grid(row=1, rowspan=5, column=0)

    rslt = StringVar()
    rslt_fld = Entry(gui, textvariable=rslt)
    rslt_fld.grid(row = 1, rowspan=5, column=1, ipadx=50)


    

    button1 = Button(gui, text=' 1 ', fg='black', bg='red',	command=lambda: press(1), height=1, width=7)
    button1.grid(row=6, column=0)

    gui.mainloop()

