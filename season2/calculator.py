from tkinter import *
expr = ""  # Global expression string

window = Tk()
window.title("Calculator")
window.geometry("350x300")
window.config(bg="#e0e1e6") 

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")


display = StringVar()
entry = Entry(window, textvariable=display)
entry.grid(columnspan=4, ipadx=70)
entry = Entry(
    window,
    textvariable=display,
    font=('Arial', 20),
    justify='right',
    bd=10
)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons
# Number buttons
btn1 = Button(window, text='1', fg='black', bg='#F29974', command=lambda: press(1), height=3, width=8)
btn1.grid(row=2, column=0)
btn2 = Button(window, text='2', fg='black', bg='#F29974', command=lambda: press(2), height=3, width=8)
btn2.grid(row=2, column=1)
btn3 = Button(window, text='3', fg='black', bg='#F29974', command=lambda: press(3), height=3, width=8)
btn3.grid(row=2, column=2)
btn4 = Button(window, text='4', fg='black', bg='#F29974', command=lambda: press(4), height=3, width=8)
btn4.grid(row=3, column=0)
btn5 = Button(window, text='5', fg='black', bg='#F29974', command=lambda: press(5), height=3, width=8)
btn5.grid(row=3, column=1)
btn6 = Button(window, text='6', fg='black', bg='#F29974', command=lambda: press(6), height=3, width=8)
btn6.grid(row=3, column=2)
btn7 = Button(window, text='7', fg='black', bg='#F29974', command=lambda: press(7), height=3, width=8)
btn7.grid(row=4, column=0)
btn8 = Button(window, text='8', fg='black', bg='#F29974', command=lambda: press(8), height=3, width=8)
btn8.grid(row=4, column=1)
btn9 = Button(window, text='9', fg='black', bg='#F29974', command=lambda: press(9), height=3, width=8)
btn9.grid(row=4, column=2)
btn0 = Button(window, text='0', fg='black', bg='#F29974', command=lambda: press(0), height=3, width=8)
btn0.grid(row=5, column=1)

# Operator buttons
plus = Button(window, text='+', fg='black', bg='#B34A24', command=lambda: press('+'), height=3, width=8)
plus.grid(row=2, column=3)
minus = Button(window, text='-', fg='black', bg='#B34A24', command=lambda: press('-'), height=3, width=8)
minus.grid(row=3, column=3)
mult = Button(window, text='*', fg='black', bg='#B34A24', command=lambda: press('*'), height=3, width=8)
mult.grid(row=4, column=3)
div = Button(window, text='/', fg='black', bg='#B34A24', command=lambda: press('/'), height=3, width=8)
div.grid(row=5, column=3)

# Other buttons
eq = Button(window, text='=', fg='black', bg='#D64100', command=equal, height=3, width=8)
eq.grid(row=5, column=2)
clr = Button(window, text='Clear', fg='black', bg='#D64100', command=clear, height=3, width=8)
clr.grid(row=5, column=0)



#run the app
window.mainloop()