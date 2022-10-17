from tkinter import *

window = Tk()



checker = False


if(checker == False):
    lbl = Label(window, text = "Not connected", fg = 'red', font = ("Helvetica", 16))
    lbl.grid(column = 3)

else:
    lbl  = Label(window, text = "Connected" , fg = 'green' , font = ("Helvetica" , 16))
    lbl.grid(column = 3)

window.mainloop()



