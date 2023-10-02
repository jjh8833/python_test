from tkinter import *

expr = ''

def press(num):
    global expr
    expr = expr + str(num)
    eqt.set(expr)

def clear():
	global expr
	expr = ""
	eqt.set("")
     
def equalpress():
     try :
          global expr
          total = str(eval(expr))
          eqt.set(total)
          expr = ""
     except : 
          eqt.set(" error ")
          expr = ""

if __name__ == "__main__":
    gui = Tk()
    gui.title("구구단계산기")
    gui.configure(background="#0066cc")
    gui.geometry("230x148")

    eqt = StringVar()
    expr_fld = Entry(gui, textvariable=eqt)
    expr_fld.grid(row = 1 , columnspan=4 ,  ipadx=10)

    btn1 = Button(gui, text=' 1 ', 
                     command=lambda: press(1), height=1, width=7)
    btn1.grid(row=2, column=0)
    
    btn2 = Button(gui, text=' 2 ', 
                     command=lambda: press(2), height=1, width=7)
    btn2.grid(row=2, column=1)

    btn3 = Button(gui, text=' 3 ', 
                     command=lambda: press(3), height=1, width=7)
    btn3.grid(row=2, column=2)

    btn4 = Button(gui, text=' 4 ', 
                     command=lambda: press(4), height=1, width=7)
    btn4.grid(row=3, column=0)

    btn5 = Button(gui, text=' 5 ', 
                     command=lambda: press(5), height=1, width=7)
    btn5.grid(row=3, column=1)

    btn6 = Button(gui, text=' 6 ', 
                     command=lambda: press(6), height=1, width=7)
    btn6.grid(row=3, column=2)

    btn7 = Button(gui, text=' 7 ', 
                     command=lambda: press(7), height=1, width=7)
    btn7.grid(row=4, column=0)

    btn8 = Button(gui, text=' 8 ', 
                     command=lambda: press(8), height=1, width=7)
    btn8.grid(row=4, column=1)

    btn9 = Button(gui, text=' 9 ', 
                     command=lambda: press(9), height=1, width=7)
    btn9.grid(row=4, column=2)

    btn0 = Button(gui, text=' 0 ', 
                     command=lambda: press(0), height=1, width=7)
    btn0.grid(row=5, column=0)

    equal = Button(gui, text=' = ', fg='black', bg='red',
				command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
				command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    plus = Button(gui, text=' + ', fg='black', bg='red',
				command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',
				command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',
					command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',
					command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    Decimal= Button(gui, text='.', fg='black', bg='red',
					command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)


    gui.mainloop()

