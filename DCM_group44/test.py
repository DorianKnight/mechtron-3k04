'''
from tkinter import *
root = Tk()
sv = StringVar()
def callback():
    print("HELLO")
    return True
e = Entry(root, validate="key", validatecommand=callback)
e.grid()
e.insert(0,"test")
root.mainloop()
'''
# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry( "200x200" )

# Change the label text
def show():
	label.config( text = clicked.get() )

# Dropdown menu options
options = [
	"V-Low",
	"Low",
	"Med-Low",
	"Med",
	"Med-High",
	"High",
	"V-High"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Med" )

# Create Dropdown menu
actThrDrop = OptionMenu( root , clicked , *options )
actThrDrop.pack()

# Create button, it will change label text
button = Button(   text = "click Me" , command = show ).pack()

# Create Label
label = Label( root , text = " " )
label.pack()

# Execute tkinter
root.mainloop()
