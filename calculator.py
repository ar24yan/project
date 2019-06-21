from tkinter import *
import math
import tkinter.messagebox
import logging
import datetime


def get_filename_datetime():
    # for getting file name of log file
    now = datetime.datetime.now()
    return "file-" + now.strftime("%Y-%m-%d %H:%M:%S") + ".log"


name = get_filename_datetime()
# basic configuration for logging
logging.basicConfig(filename=name, level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p', filemode="w+")

# using Tk we are creating main window
root = Tk()
logging.warning("THis is start")

# assigning title to window
root.title("Scientific calculator")

# assigning background color as powder blue to window
root.configure(background="powder blue")

# creating a window which can not be resized
root.resizable(width=False, height=False)
root.geometry("500x568+0+0")

# creating a frame from parent root and placing the frame
calc = Frame(root)
calc.grid()


# creating a Calc() class which will have methods to perform all mathematical operation and creating variable

class Calc:
    def __init__(self):
        self.total = 0
        self.current = " "
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        # for getting the number
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum

        self.display(self.current)

    def sum_of_total(self):
        # for displaying number if more than one number is entered
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        # for deleteing the entry value

        txtDisplay.delete(0, END)
        # nserts string value before the character at the given index.
        txtDisplay.insert(0, value)

    def valid_function(self):

        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            try:
                self.total /= self.current
            except:
                logging.info("An Exception has occured")
                self.total = "Math Error"

        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def pi(self):
        # for displaying the value of pi=3.14
        self.result = False
        self.current = math.pi
        self.display(self.current)
        logging.info("Printing the value of Pi")

    def tau(self):
        # for displaying the value of 2*pi
        self.result = False
        self.current = math.tau
        self.display(self.current)
        logging.info("Printing the value of 2pi")

    def e(self):
        # for displaying the value of e
        self.result = False
        self.current = math.e
        self.display(self.current)
        logging.info("Printing the value of e")

    def Clear_Entry(self):
        # for clearing the entry
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True
        logging.info("Performing clear opeartion")

    def all_Clear_Entry(self):
        # for clearning the entry
        self.Clear_Entry()
        self.total = 0
        logging.info("Performing AllClear Opeartion")

    def squared(self):
        # for displaying the squareroot of the number
        self.result = False
        m = txtDisplay.get()
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
        logging.info(f"performing squareroot operation of {m} is  {self.current}")

    def mathPM(self):
        # for converting positive number to negative and vice-versa.
        self.result = False
        m = txtDisplay.get()
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
        logging.info(f"performing plusminus operation of {m} is  {self.current}")

    def cos(self):
        # for displaying cos of value entered in degree
        self.result = False
        m = txtDisplay.get()
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        logging.info(f"performing cos operation of {m} is  {self.current}")

    def cosh(self):
        # for dispalying cosine hyperbolic value of entered data
        self.result = False
        m = txtDisplay.get()
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        logging.info(f"performing cosh operation of {m} is  {self.current}")

    def sin(self):
        # for displaying sine of value entered in degree
        self.result = False
        m = txtDisplay.get()
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        logging.info(f"performing sin operation of {m} is  {self.current}")

    def sinh(self):
        # for displaying sine hyperbolic value
        self.result = False
        m = txtDisplay.get()
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        logging.info(f"performing sinh operation of {m} is  {self.current}")

    def tan(self):
        # for displaying tan of value entered in degree
        self.result = False
        m = txtDisplay.get()
        a = float(m)
        print(type(int((a / 90) % 2)))
        if int((a / 90) % 2) == 1:
            self.current = "Maths Error"
            self.display(self.current)
        elif int((a / 90) % 2) == 0:
            self.current = "0"
            self.display(self.current)
        else:
            self.current = math.tan(math.radians(float(txtDisplay.get())))
            self.display(self.current)
        logging.info(f"performing tan operation of {m} is  {self.current}")

    def tanh(self):
        # for displaying tangent hyperbolic of value entered in degree
        self.result = False
        m = txtDisplay.get()
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        logging.info(f"performing tanh operation of {m} is  {self.current}")

    def log(self):
        # for displaying natural log of entered value
        self.result = False
        m = txtDisplay.get()
        try:
            self.current = math.log(float(txtDisplay.get()))
        except:
            self.current = "Maths error"
            self.display(self.current)

        self.display(self.current)

        logging.info(f"performing log operation of {m} is  {self.current}")

    def lgamma(self):
        # for displaying natural log(number-1)
        self.current = False
        m = txtDisplay.get()
        try:
            self.current = math.lgamma(float(txtDisplay.get()))
        except:
            self.current = "Maths Error"
            self.display(self.current)
        self.display(self.current)
        logging.info(f"performing 1gamma operation of {m} is  {self.current}")

    def degrees(self):
        # for converting given value to degrees
        self.current = False
        m = txtDisplay.get()
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
        logging.info(f"performing degree operation of {m} is  {self.current}")

    def log2(self):
        # for displaying log to the base 2 of entered value
        self.current = False
        m = txtDisplay.get()
        try:
            self.current = math.log2(float(txtDisplay.get()))
        except:
            self.current = "Maths Error"
            self.display(self.current)

        self.display(self.current)
        logging.info(f"performing log2 operation of {m} is  {self.current}")

    def log10(self):
        # for displaying log to the base 10 of entered value
        self.current = False
        m = txtDisplay.get()
        try:
            self.current = math.log10(float(txtDisplay.get()))
        except:
            self.current = "Maths Error"
            self.display(self.current)

        self.display(self.current)
        logging.info(f"performing log10 operation of {m} is  {self.current}")

    def log1p(self):
        # for displaying natural log of number+1 of entered value
        self.current = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)
        logging.info(f"performing log1p operation of {m} is  {self.current}")

    def a_cosh(self):
        # for displaying inverse cos hyperbolic function
        self.current = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)
        logging.info(f"performing inverse Hyperbolic function operation of {m} is  {self.current}")

    def expm1(self):
        # for displaying exp(number)-1
        self.current = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)
        logging.info(f"performing expm1 operation of {m} is  {self.current}")

    def exp(self):
        # for displaying exponential of given value
        self.current = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)
        logging.info(f"performing exp operation of {m} is  {self.current}")

    def fact(self):
        # for dispalying the factorial of number
        self.current = False
        m = int(float(txtDisplay.get()))

        self.current = math.factorial(m)

        self.display(self.current)
        logging.info(f"performing Adding operation of {m} is  {self.current}")

    def a_sinh(self):
        # for displaying inverse hyperbolic of sine of entered numbered
        self.current = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)
        logging.info(f"performing inverse sine hyperbolic operation of {m} is  {self.current}")


# creating object of Calc class
added_value = Calc()

# creating a text display
txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg="powder blue", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

# ========================CREATING STANDARD CALCULATOR BUTTONS=====================================================================
btnClear = Button(calc, text=chr(67), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                  command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)

btnAllClear = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg='powder blue', command=added_value.all_Clear_Entry).grid(row=1, column=1, pady=1)

btnSq = Button(calc, text="√", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
               command=added_value.squared).grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)

btnSub = Button(calc, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)

btnMul = Button(calc, text="*", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)

btnDiv = Button(calc, text="/", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)

btnZero = Button(calc, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                 command=lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)
# command=lambda:added_value.numberEnter(0)

btnDot = Button(calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)

btnPM = Button(calc, text=chr(177), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
               command=added_value.mathPM).grid(row=5, column=2, pady=1)

btnEquals = Button(calc, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                   command=added_value.sum_of_total).grid(row=5, column=3, pady=1)

# =========================CREATING SCIENTIFIC CALCULATOR BUTTON===============================================================================

btnPi = Button(calc, text="π", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
               command=added_value.pi).grid(row=1, column=4, pady=1)

btncos = Button(calc, text="cos", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=added_value.cos).grid(row=1,
                                              column=5,
                                              pady=1)

btntan = Button(calc, text="tan", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=added_value.tan).grid(row=1,
                                              column=6,
                                              pady=1)

btnsin = Button(calc, text="sin", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=added_value.sin).grid(row=1,
                                              column=7,
                                              pady=1)

btn2Pi = Button(calc, text="2π", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=added_value.tau).grid(row=2, column=4, pady=1)

btncosh = Button(calc, text="cosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                 command=added_value.cosh).grid(row=2,
                                                column=5,
                                                pady=1)

btntanh = Button(calc, text="tanh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                 command=added_value.tanh).grid(row=2,
                                                column=6,
                                                pady=1)

btnsinh = Button(calc, text="sinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                 command=added_value.sinh).grid(row=2,
                                                column=7,
                                                pady=1)

btnlog = Button(calc, text="log", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg='powder blue', command=added_value.log).grid(row=3, column=4, pady=1)

btnExp = Button(calc, text="Exp", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=added_value.exp).grid(row=3, column=5, pady=1)

btnfact = Button(calc, text="!", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                 command=added_value.fact).grid(row=3, column=6, pady=1)

btnE = Button(calc, text="e", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
              command=added_value.e).grid(row=3, column=7, pady=1)

btnlog2 = Button(calc, text="log2", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                 command=added_value.log2).grid(row=4, column=4, pady=1)

btndeg = Button(calc, text="deg", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=added_value.degrees).grid(row=4, column=5, pady=1)

btnacosh = Button(calc, text="acosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                  command=added_value.a_cosh).grid(row=4,
                                                   column=6,
                                                   pady=1)

btnasinh = Button(calc, text="asinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                  command=added_value.a_sinh).grid(row=4,
                                                   column=7,
                                                   pady=1)

btnlog10 = Button(calc, text="log10", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                  command=added_value.log10).grid(row=5,
                                                  column=4,
                                                  pady=1)

btnlog1p = Button(calc, text="log1p", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                  command=added_value.log1p).grid(row=5,
                                                  column=5,
                                                  pady=1)

btnexpm1 = Button(calc, text="expm1", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                  command=added_value.expm1).grid(row=5,
                                                  column=6,
                                                  pady=1)

btn1gamma = Button(calc, text="1gamma", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                   command=added_value.lgamma).grid(
    row=5, column=7, pady=1)

lblDisplay = Label(calc, text="Scientific Calculator", font=('arial', 30, 'bold'), justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)

numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1


# *********************************Menu*****************************************************

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific calculator", "Confirm if you want to exit")
    if iExit > 0:
        logging.info("End of the code")
        root.destroy()

        return


def scientific():
    root.resizable(width=False, height=False)
    root.geometry("1000x568+0+0")


def standard():
    root.resizable(width=False, height=False)
    root.geometry("500x568+0+0")


def message_about():
    return tkinter.messagebox.showinfo("About", "This is standard and Scientific calculator.")


menubar = Menu(calc)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=standard)
filemenu.add_command(label="Scientific", command=scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=aboutmenu)
aboutmenu.add_command(label="About", command=message_about)

root.configure(menu=menubar)

root.mainloop()