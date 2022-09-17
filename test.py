import main
import time
from tkinter import *


window = Tk()

l1 = Label(window, text="Slow")
l1.grid(row=0, column=0)

l2 = Label(window, text="Regular")
l2.grid(row=0, column=1)

l3 = Label(window, text="Fast")
l3.grid(row=0, column=2)

l4 = Label(window, text= main.slow )
l4.grid(row=1, column=0)

l5 = Label(window, text= main.regular )
l5.grid(row=1, column=1)

l6 = Label(window, text= main.fast )
l6.grid(row=1, column=2)

window.mainloop()