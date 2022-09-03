from tkinter import *
import math
import tkinter.messagebox
root = Tk()
root.geometry("650x560+250+150")
root.title("Scientific Calculator")
switch = None


def btn_1():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn_2():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn_3():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn_4():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn_5():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn_6():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn_7():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn_8():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn_9():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn_0():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def btn_p():
    pos = len(disp.get())
    disp.insert(pos, '+')


def btn_s():
    pos = len(disp.get())
    disp.insert(pos, '-')


def btn_m():
    pos = len(disp.get())
    disp.insert(pos, 'x')


def btn_d():
    pos = len(disp.get())
    disp.insert(pos, '/')


def sin():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def cos():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.cos(math.radians(ans))
        else:
            ans = math.cos(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def tan():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.tan(math.radians(ans))
        else:
            ans = math.tan(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def asin():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.asin(math.radians(ans))
        else:
            ans = math.asin(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def acos():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.acos(math.radians(ans))
        else:
            ans = math.acos(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def atan():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.atan(math.radians(ans))
        else:
            ans = math.atan(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def pow():
    pos = len(disp.get())
    disp.insert(pos, '**')


def dot():
    pos = len(disp.get())
    disp.insert(pos, '.')


def br():
    pos = len(disp.get())
    disp.insert(pos, '(')


def bl():
    pos = len(disp.get())
    disp.insert(pos, ')')


def cl():
    pos = len(disp.get())
    disp.delete(0, END)
    disp.insert(0, '0')


def mo():
    pos = len(disp.get())
    disp.insert(pos, '%')


def eq():
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def log():
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def ln():
    try:
        ans = float(disp.get())
        ans = math.log(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def Round():
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def sqrt():
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


def btn_pi():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


def btn_ex():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.e))


def back():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def conv():
    try:
        ans = float(disp.get())
        ans = (ans)*(math.pi)/180
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error")


disp = Entry(root, font="Arial 20", fg="Black",
             bg="yellow", bd=10, justify=RIGHT)
disp.insert(0, '0')
disp.pack(expand=TRUE, fill=BOTH)
row1 = Frame(root, bg="red").pack(expand=TRUE, fill=BOTH)
btnrow1 = Frame(root)
btnrow1.pack(expand=TRUE, fill=BOTH)
btnc = Button(btnrow1, text="C", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=cl, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnbksp = Button(btnrow1, text="←", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                 command=back, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnbr1 = Button(btnrow1, text="(", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                command=br, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnbr2 = Button(btnrow1, text=")", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                command=bl, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)


sinbtn = Button(btnrow1, text="sin", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                command=sin, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
cosbtn = Button(btnrow1, text="cos", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                command=cos, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
tanbtn = Button(btnrow1, text="tan", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                command=tan, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)
btn7 = Button(btnrow2, text="7", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_7, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btn8 = Button(btnrow2, text="8", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_8, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btn9 = Button(btnrow2, text="9", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_9, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btns = Button(btnrow2, text="-", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_s, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)


btnasin = Button(btnrow2, text="sin-1", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                 command=asin, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnacos = Button(btnrow2, text="cos-1", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                 command=acos, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnatan = Button(btnrow2, text="tan-1", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                 command=atan, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)


btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)
btn4 = Button(btnrow3, text="4", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_4, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btn5 = Button(btnrow3, text="5", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_5, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btn6 = Button(btnrow3, text="6", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_6, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnp = Button(btnrow3, text="+", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_p, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnpw = Button(btnrow3, text="x^y", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
               command=pow, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnrt = Button(btnrow3, text="√", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
               command=sqrt, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btne = Button(btnrow3, text="e", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_ex, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)


btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)
btn1 = Button(btnrow4, text="1", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_1, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btn2 = Button(btnrow4, text="2", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_2, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btn3 = Button(btnrow4, text="3", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_3, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnd = Button(btnrow4, text="/", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_d, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
pibtn = Button(btnrow4, text="π", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
               command=btn_pi, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnrad = Button(btnrow4, text="Rad", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                command=conv, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnrnd = Button(btnrow4, text="Round", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                command=Round, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)


btnrow5 = Frame(root)
btnrow5.pack(expand=TRUE, fill=BOTH)
btn0 = Button(btnrow5, text="0", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_0, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnpt = Button(btnrow5, text=".", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
               command=dot, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnprc = Button(btnrow5, text="%", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                command=mo, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnm = Button(btnrow5, text="x", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
              command=btn_m, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btnln = Button(btnrow5, text="ln", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
               command=ln, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
logbtn = Button(btnrow5, text="log", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
                command=log, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)
btneq = Button(btnrow5, text="=", width=5, height=2, font="Arial 20", relief=GROOVE, bd=2,
               command=eq, fg="White", bg="#333333").pack(side=LEFT, expand=TRUE, fill=BOTH, pady=1)


root.mainloop()
