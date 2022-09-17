from ast import While
from cProfile import label
from pathlib import WindowsPath
from tkinter import *
from turtle import up, update
from winotify import Notification, audio
from ethereum_gasprice import GaspriceController, GaspriceStrategy
from ethereum_gasprice.providers import EtherscanProvider
import time
import key


# Get gasprice by one of these strategies:
while(True):

    gasprice_slow = key.controller.get_gasprice_by_strategy(GaspriceStrategy.SLOW)
    gasprice_regular = key.controller.get_gasprice_by_strategy(GaspriceStrategy.REGULAR)
    gasprice_fast = key.controller.get_gasprice_by_strategy(GaspriceStrategy.FAST)

    slice_obj = slice(0,2)
    print(str(gasprice_slow)[slice_obj])  # output: 69
    print(str(gasprice_regular)[slice_obj])
    print(str(gasprice_fast)[slice_obj])

    slow = str(gasprice_slow)[slice_obj]
    regular = str(gasprice_regular)[slice_obj]
    fast = str(gasprice_fast)[slice_obj]

    if slow < str(10):
        toast = Notification(app_id= "GasTracker",
                        title="Gas Tracker",
                        msg= "Gas prices are lower than usual, Mint some shit!",
                        duration="short",
                        icon="D:\Python\Gas Tracker\png.png")

        toast.add_actions(label="Mint now", launch="https://knownorigin.io/pratiikjagdale")
        toast.set_audio(audio.SMS, loop = False)
        toast.show()
    time.sleep(2)
    
    

    window = Tk()

    l1 = Label(window, text="Slow")
    l1.grid(row=0, column=0)

    l2 = Label(window, text="Regular")
    l2.grid(row=0, column=1)

    l3 = Label(window, text="Fast")
    l3.grid(row=0, column=2)

    l4 = Label(window, text= slow )
    l4.grid(row=1, column=0)

    l5 = Label(window, text= regular )
    l5.grid(row=1, column=1)

    l6 = Label(window, text= fast )
    l6.grid(row=1, column=2)

    def update():
        l4 = Label(window, text= slow )
        l4.grid(row=1, column=0)

        l5 = Label(window, text= regular )
        l5.grid(row=1, column=1)

        l6 = Label(window, text= fast )
        l6.grid(row=1, column=2)
        window.after(10000, update)

    update()

    window.mainloop()