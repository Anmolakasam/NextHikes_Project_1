from tkinter import *
import math as M

window = Tk()
window.geometry("361x570+470+20")
window.title("Python Calculator")
window.config(bg="gray11")
window.resizable(False, False)

#window.overrideredirect(1)


def close():
    window.destroy()

def clear():
    entry.delete(0, "end")

def back():
    last_number=len(entry.get())-1
    entry.delete(last_number)

def press(input):
    length = len(entry.get())
    entry.insert(length, input)

def add(a,b):
    return float(a)+float(b)

def subtract(a,b):
    return float(a)-float(b)

def divide(a,b):
    return float(a) / float(b)

def multiply(a,b):
    return float(a) * float(b)

def expression_break(sign, expression):
    values = expression.split(sign,1)
    return values

def scientific(expression):
    data = expression_break("(",expression)
    if data[0] =="tan":       
        result = M.tan(float(data[1]))

    elif data[0] =="coSs":
        result = M.cos(float(data[1]))

    elif data[0] =="sin":
        result = M.sin(float(data[1]))

    elif data[0] =="sqrt":
        result = M.sqrt(float(data[1]))

    elif data[0] =="log":
        result = M.log10(float(data[1]))

    elif data[0] =="ln":
        result = M.log(float(data[1]))

    elif data[0] =="deg":
        result = M.degrees(float(data[1]))

    elif data[0] =="rad":
        result = M.radians(float(data[1]))

    elif data[0] =="fac":
        result = M.factorial(int(float(data[1])))
    return result


def equal(event = None):
    expression = entry.get()
    clear()
    try:

        if expression.find("(") > 0:
             result = scientific(expression)

        elif "pow" in expression:
             data = expression_break("pow", expression)
             result = M.pow(float(data[0]), float(data[1]))

        elif expression.find("rem") > 0:
            data = expression_break("rem",expression)
            result = M.remainder(float(data[0]), float(data[1]))

        elif expression.find("×") != -1:
            data = expression_break("×", expression)
            result = multiply(data[0], data[1])

        elif expression.find("*") != -1:
            data = expression_break("*", expression)
            result = multiply(data[0], data[1])

        elif expression.find("÷") != -1:
            data = expression_break("÷", expression)
            result = divide(data[0], data[1])

        elif expression.find("/") != -1:
            data = expression_break("/", expression)
            result = divide(data[0], data[1])

        elif expression.find("+") > 0:
            first = expression.find("+")
            second = expression.find("+",(first+1),(first+5))
            if first > second:
                data = expression_break("+",expression)
                result = add(data[0], data[1])
            else:
                result = add(expression[0:second], expression[second+1:])

        elif expression.rindex("-") > 0:
            sign = expression.rindex("-")
            result = subtract(expression[0:sign],expression[sign+1:])

        entry.insert(0, result)

    except:
        entry.insert(0, "Error")

def key_filter(event):
    allowed = "0123456789.+-*/"
    if event.keysym in ("BackSpace", "Delete", "Left", "Right", "Tab", "Return", "KP_Enter"):
        return
    if event.char in allowed:
        return
    if event.char == "":
        return
    return "break"

entry_string = StringVar()
entry = Entry(window, textvariable = entry_string,
              fg = "white", bg = "gray20",
              border = 0, font = ("Bohnschrift SemiBold",25))
entry.grid(columnspan=4, ipady=15)
entry.bind("<Return>", equal)
entry.bind("<KP_Enter>", equal)
entry.bind("<KeyPress>", key_filter)

font_value = ("Calibari", 17)

#Buttons Grids
#buttons values are = Tan, cos, sin, sqrt

btn_tan= Button(window, text="tan", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("tan("))
btn_tan.grid(row=1, column=0, sticky=E+W, ipady=5)

btn_cos= Button(window, text="cos", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("cos("))
btn_cos.grid(row=1, column=1, sticky=E+W, ipady=5)

btn_sin= Button(window, text="sin", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("sin("))
btn_sin.grid(row=1, column=2, sticky=E+W, ipady=5)

btn_sqrt= Button(window, text="sqrt", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("sqrt("))
btn_sqrt.grid(row=1, column=3, sticky=E+W, ipady=5)

#buttons values are = log, ln, deg, rad

btn_log= Button(window, text="log", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("log("))
btn_log.grid(row=2, column=0, sticky=E+W, ipady=5)

btn_ln= Button(window, text="ln", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("ln("))
btn_ln.grid(row=2, column=1, sticky=E+W, ipady=5)

btn_deg= Button(window, text="deg", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("deg("))
btn_deg.grid(row=2, column=2, sticky=E+W, ipady=5)

btn_rad= Button(window, text="rad", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("rad("))
btn_rad.grid(row=2, column=3, sticky=E+W, ipady=5)

#buttons values are = factorial, power, rem, pi

btn_fac= Button(window, text="fac", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("fac("))
btn_fac.grid(row=3, column=0, sticky=E+W, ipady=5)

btn_pow= Button(window, text="pow", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("pow"))
btn_pow.grid(row=3, column=1, sticky=E+W, ipady=5)

btn_rem= Button(window, text="rem", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("rem"))
btn_rem.grid(row=3, column=2, sticky=E+W, ipady=5)

btn_π= Button(window, text="π", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(3.141592))
btn_π.grid(row=3, column=3, sticky=E+W, ipady=5)

#buttons values are = CLear, Delete

btn_CLEAR= Button(window, text="C", bg= "grey5",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = clear)
btn_CLEAR.grid(row=4, columnspan=2, column=0, sticky=E+W, ipady=5)

btn_BACKSPACE= Button(window, text="Delete", bg= "grey5",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command=back)
btn_BACKSPACE.grid(row=4, columnspan=2, column=2, sticky=E+W, ipady=5)

#number Buttons values
#buttons = 7, 8,9 and division

btn_7= Button(window, text="7", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(7))
btn_7.grid(row=5, column=0, sticky=E+W, ipady=5)

btn_8= Button(window, text="8", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(8))
btn_8.grid(row=5, column=1, sticky=E+W, ipady=5)

btn_9= Button(window, text="9", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(9))
btn_9.grid(row=5, column=2, sticky=E+W, ipady=5)

btn_div= Button(window, text="/ ", bg= "grey5",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("/"))
btn_div.grid(row=5, column=3, sticky=E+W, ipady=5)

#buttons = 4, 5,6 and multiply

btn_4= Button(window, text="4", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(4))
btn_4.grid(row=6, column=0, sticky=E+W, ipady=5)

btn_5= Button(window, text="5", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(5))
btn_5.grid(row=6, column=1, sticky=E+W, ipady=5)

btn_6= Button(window, text="6", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(6))
btn_6.grid(row=6, column=2, sticky=E+W, ipady=5)

btn_multiply= Button(window, text="*", bg= "grey5",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("*"))
btn_multiply.grid(row=6, column=3, sticky=E+W, ipady=5)

#buttons = 1, 2, 3 and subtraction

btn_1= Button(window, text="1", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(1))
btn_1.grid(row=7, column=0, sticky=E+W, ipady=5)

btn_2= Button(window, text="2", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(2))
btn_2.grid(row=7, column=1, sticky=E+W, ipady=5)

btn_3= Button(window, text="3", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(3))
btn_3.grid(row=7, column=2, sticky=E+W, ipady=5)

btn_sub= Button(window, text= "-", bg= "grey5",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("-"))
btn_sub.grid(row=7, column=3, sticky=E+W, ipady=5)

#buttons = Decimal, 0, e, and Addition

btn_decimal= Button(window, text= ".", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("."))
btn_decimal.grid(row=8, column=0, sticky=E+W, ipady=5)

btn_0= Button(window, text= "0", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(0))
btn_0.grid(row=8, column=1, sticky=E+W, ipady=5)

btn_e= Button(window, text= "e", bg= "grey11",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press(2.71828))
btn_e.grid(row=8, column=2, sticky=E+W, ipady=5)

btn_addition= Button(window, text= "+", bg= "grey5",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = lambda:press("+"))
btn_addition.grid(row=8, column=3, sticky=E+W, ipady=5)

#Buttons = Equal and Close

btn_equal= Button(window, text="=", bg= "DarkOrange1",
                 fg="Black", font=font_value,
                 borderwidth=1, relief= SOLID, command = equal)
btn_equal.grid(row=9, columnspan=3, column=0, sticky=E+W, ipady=5)

btn_close= Button(window, text="close", bg= "grey5",
                 fg="DarkOrange1", font=font_value,
                 borderwidth=1, relief= SOLID, command = close)
btn_close.grid(row=9,column=3, sticky=E+W, ipady=5)


mainloop()