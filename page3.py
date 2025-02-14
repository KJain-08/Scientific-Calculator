from tkinter import *
from tkinter import ttk
import math
import tkinter
import subprocess

root = Tk()
root.title("Scientific Calculator")
root.configure(background="#121212", padx=10.0, pady=20.0)
root.resizable(width=False, height=False)
root.geometry("500x600")

color = "black"
btnColor = "#232323"
btnColorCont = "#ff680c"
btnTextColor = "white"
# Text box
ip = Frame(root, background=btnColor, bd=0, pady=15, padx=18)
ip.pack(ipady=10)


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.user_input = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberInput(self, num):
        self.result = False
        numInput1 = txtDisplay.get()
        numInput2 = str(num)
        if self.user_input:
            self.current = numInput2
            self.user_input = False
        else:
            if numInput2 == '.':
                if numInput2 in numInput1:
                    return
            self.current = numInput1 + numInput2
        self.display(self.current)

    def totalSum(self):
        self.result = True
        self.current = float(self.current)
        self.current = float(self.current)
        if self.check_sum == True:
            self.mainFunction()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def mainFunction(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        if self.op == "raise":
            self.total = self.total ** self.current
        if self.op == "nthroot":
            self.total = self.total ** (1 / self.current)
        if self.op == "log":
            self.total = round(math.log(self.total, self.current), 2)
        self.user_input = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.mainFunction()
        elif not self.result:
            self.total = self.current
            self.user_input = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clearAllEntry(self):
        self.result = False
        self.current = 0
        self.display(self.current)
        self.user_input = True

    def clearEntry(self):
        self.result=False
        pos = len(txtDisplay.get())
        display = str(txtDisplay.get())
        if display == '':
            txtDisplay.insert(0, '0')
        elif display == ' ':
            txtDisplay.insert(0, '0')
        elif display == '0':
            pass
        else:
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, display[0:pos-1])
            self.current= txtDisplay.get()
            self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(txtDisplay.get())
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(int(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = round(math.cos(math.radians(int(txtDisplay.get()))), 2)
        self.display(self.current)

    def sqr(self):
        self.result = False
        self.current = int(txtDisplay.get()) ** 2
        self.display(self.current)

    def xinv(self):
        self.result = False
        self.current = 1 / int(txtDisplay.get())
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = round(math.tan(math.radians(int(txtDisplay.get()))), 2)
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = round(math.sin(math.radians(int(txtDisplay.get()))), 2)
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(int(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(int(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(int(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(int(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(int(txtDisplay.get()))
        self.display(self.current)

    def fact(self):
        self.result = False
        self.current = math.factorial(int(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(int(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(int(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(int(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(int(txtDisplay.get()))
        self.display(self.current)


added_value = Calc()

txtDisplay = Entry(ip, font=('Georgia', 24, 'bold'), bg='#454545', fg='#CDCDCD', width=19, bd=1, justify="right",
                   border=6)
txtDisplay.insert(0, "0")
txtDisplay.pack()

# Buttons

btn = Frame(root, background=color)
btn.pack()
numberpad = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
i = 0
btns = []
for j in range(2, 5):
    for k in range(3):
        btns.append(Button(btn, padx=0, pady=0, borderwidth=2, text=numberpad[i], height=1, width=7, bg=btnColor,
                           fg=btnTextColor, font=('Georgia', 18, 'bold'), bd=0, ))
        btns[i].grid(row=j, column=k)
        btns[i]["command"] = lambda x=numberpad[i]: added_value.numberInput(x)
        i += 1

    # --------------------------------------------------------

    # --------------------------------------------------------

btnClear = Button(btn, padx=0, pady=0, borderwidth=2, text="<--", height=1, width=7, bg=btnColorCont, fg=btnTextColor,
                  font=('Georgia', 18, 'bold'), bd=0, command=added_value.clearEntry).grid(row=1, column=0)

btnAllClear = Button(btn, padx=0, pady=0, borderwidth=2, text="C", height=1, width=7, bg=btnColorCont, fg=btnTextColor,
                     font=('Georgia', 18, 'bold'), bd=0, command=added_value.clearAllEntry).grid(row=1, column=1)

btnMod = Button(btn, padx=0, pady=0, borderwidth=2, text="%", height=1, bg=btnColorCont, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, width=7, command=lambda: added_value.operation("mod")).grid(row=1,
                                                                                                                column=2)

btnAdd = Button(btn, padx=0, pady=0, borderwidth=2, text="+", height=1, width=7, bg=btnColorCont, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, command=lambda: added_value.operation("add")).grid(row=1, column=3)

btnSub = Button(btn, padx=0, pady=0, borderwidth=2, text="-", height=1, width=7, bg=btnColorCont, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, command=lambda: added_value.operation("sub")).grid(row=2, column=3)

btnMul = Button(btn, padx=0, pady=0, borderwidth=2, text="x", height=1, width=7, bg=btnColorCont, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, command=lambda: added_value.operation("multi")).grid(row=3,
                                                                                                         column=3)

btnDiv = Button(btn, padx=0, pady=0, borderwidth=2, text="/", height=1, width=7, bg=btnColorCont, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, command=lambda: added_value.operation("divide")).grid(row=4,
                                                                                                          column=3)

btnZero = Button(btn, padx=0, pady=0, borderwidth=2, text="0", height=1, width=7, bg=btnColor, fg=btnTextColor,
                 font=('Georgia', 18, 'bold'), bd=0, command=lambda: added_value.numberInput(0)).grid(row=5, column=0)

btnDot = Button(btn, padx=0, pady=0, borderwidth=2, text=".", height=1, width=7, bg=btnColor, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, command=lambda: added_value.numberInput(".")).grid(row=5, column=1)

btnPM = Button(btn, padx=0, pady=0, borderwidth=2, text=chr(177), height=1, width=7, bg=btnColorCont, fg=btnTextColor,
               font=('Georgia', 18, 'bold'), bd=0, command=added_value.mathPM).grid(row=5, column=2)

btnEquals = Button(btn, padx=0, pady=0, borderwidth=2, text="=", height=1, width=7, bg=btnColorCont, fg=btnTextColor,
                   font=('Georgia', 18, 'bold'), bd=0, command=added_value.totalSum).grid(row=5, column=3)

# SCI
btnPi = Button(btn, padx=0, pady=0, borderwidth=2, text="pi", height=1, bg=btnColor, fg=btnTextColor,
               font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.pi).grid(row=6, column=0)

btnCos = Button(btn, padx=0, pady=0, borderwidth=2, text="Cos", height=1, bg=btnColor, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.cos).grid(row=6, column=1)

btntan = Button(btn, padx=0, pady=0, borderwidth=2, text="tan", height=1, bg=btnColor, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.tan).grid(row=6, column=2)

btnsin = Button(btn, padx=0, pady=0, borderwidth=2, text="sin", height=1, bg=btnColor, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.sin).grid(row=6, column=3)

# ROW 2 :
btn2Pi = Button(btn, padx=0, pady=0, borderwidth=2, text="2pi", height=1, bg=btnColor, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.tau).grid(row=7, column=0)

btnsqr = Button(btn, padx=0, pady=0, borderwidth=2, text="x**2", height=1, bg=btnColor, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.sqr).grid(row=7, column=1)

btnxinv = Button(btn, padx=0, pady=0, borderwidth=2, text="1/x", height=1, bg=btnColor, fg=btnTextColor,
                 font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.xinv).grid(row=7, column=2)

btnrasie = Button(btn, padx=0, pady=0, borderwidth=2, text="x**y", height=1, bg=btnColor, fg=btnTextColor,
                  font=('Georgia', 18, 'bold'), bd=0, width=7, command=lambda: added_value.operation("raise")).grid(
    row=7, column=3)

# ROW 3 :
btnlog = Button(btn, padx=0, pady=0, borderwidth=2, text="log", height=1, bg=btnColor, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, width=7,
                command=lambda: added_value.operation("log")).grid(row=8, column=0)

btnExp = Button(btn, padx=0, pady=0, borderwidth=2, text="exp", height=1, bg=btnColor, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.exp).grid(row=8, column=1)

btnsqrt = Button(btn, padx=0, pady=0, borderwidth=2, text="\u221A", height=1, width=7, bg=btnColor, fg=btnTextColor,
                 font=('Georgia', 18, 'bold'), bd=0, command=added_value.squared).grid(row=8, column=2)

btnE = Button(btn, padx=0, pady=0, borderwidth=2, text="e", height=1, bg=btnColor, fg=btnTextColor,
              font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.e).grid(row=8, column=3)

# ROW 4 :
btnlog10 = Button(btn, padx=0, pady=0, borderwidth=2, text="log10", height=1, bg=btnColor, fg=btnTextColor,
                  font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.log10).grid(row=10, column=0)

btncos = Button(btn, padx=0, pady=0, borderwidth=2, text="log1p", height=1, bg=btnColor, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.cos).grid(row=10, column=1)

nthroot = Button(btn, padx=0, pady=0, borderwidth=2, text="nth root", height=1, bg=btnColor, fg=btnTextColor,
                 font=('Georgia', 18, 'bold'), bd=0, width=7, command=lambda: added_value.operation("nthroot")).grid(
    row=10, column=2)

fact = Button(btn, padx=0, pady=0, borderwidth=2, text="x!", height=1, bg=btnColor, fg=btnTextColor,
              font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.fact).grid(row=10, column=3)
# ROW 5 :
btnlog2 = Button(btn, padx=0, pady=0, borderwidth=2, text="log2", height=1, bg=btnColor, fg=btnTextColor,
                 font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.log2).grid(row=11, column=0)

btndeg = Button(btn, padx=0, pady=0, borderwidth=2, text="deg", height=1, bg=btnColor, fg=btnTextColor,
                font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.degrees).grid(row=11, column=1)

btnacosh = Button(btn, padx=0, pady=0, borderwidth=2, text="acosh", height=1, bg=btnColor, fg=btnTextColor,
                  font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.acosh).grid(row=11, column=2)

btnasinh = Button(btn, padx=0, pady=0, borderwidth=2, text="asinh", height=1, bg=btnColor, fg=btnTextColor,
                  font=('Georgia', 18, 'bold'), bd=0, width=7, command=added_value.asinh).grid(row=11, column=3)

# Menu
menubar = Menu(root)



def open_sci_calculator():
    try:
        subprocess.run(["python", "currency.py"])
    except Exception as e:
        print(f"Error running Scientific Calculator: {e}")




def isExit():
    isExit = tkinter.messagebox.askyesno("Scientific Calculator", "Do you want to exit?")
    if isExit > 0:
        root.destroy()
        return


# MenuBar1 :
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="Unit Covertor", command=open_sci_calculator)
filemenu.add_command(label="Scientific")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=isExit)

# MenuBar2 :
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")
editmenu.add_separator()
editmenu.add_command(label="Dark Mode")

root.config(menu=menubar)
root.mainloop()