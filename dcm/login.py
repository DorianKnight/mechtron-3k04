from tkinter import *
#from Pillow import ImageTk, Image

window = Tk()
window.title("Login form")
window.geometry('340x440')
background = '#ebebeb'

login_fr = Frame(
    window,
    bg = background,
    padx = 10,
    pady = 10
)

login_fr.pack()

login_label = Label(login_fr, text="Login",bg=background)
username_label = Label(login_fr, text="Username", bg=background)
username_entry = Entry(login_fr)
password_label = Label(login_fr, text="Password", bg=background)
password_entry = Entry(login_fr, show="*")
login_button = Button(login_fr, text="Login")

login_label.grid(row=0, column=1, columnspan=2, sticky="news", pady=10)
username_label.grid(row=1, column=0, padx=5)
username_entry.grid(row=1, column=1, pady=10, padx=20)
password_label.grid(row=2, column=0, padx=5)
password_entry.grid(row=2, column=1, pady=10, padx=20)
login_button.grid(row=3, column=1, columnspan=2, pady=10)

window.mainloop()