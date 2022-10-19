from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Login form")
window.iconbitmap("logo.ico")
background = '#ebebeb'

#interface logo
img = ImageTk.PhotoImage(Image.open("dcm/Complogo.png"))

login_fr = Frame(
    window,
    bg = background,
    padx = 10,
    pady = 10
)

login_fr.pack()

img_label = Label(login_fr,image=img)
login_label = Label(login_fr, text="Login")
username_label = Label(login_fr, text="Username")
username_entry = Entry(login_fr)
password_label = Label(login_fr, text="Password")
password_entry = Entry(login_fr, show="*")
login_button = Button(login_fr, text="Login")

img_label.grid(row=0, column=0, padx=10)
login_label.grid(row=0, column=1, columnspan=2, sticky="news", pady=10)
username_label.grid(row=1, column=0, padx=5)
username_entry.grid(row=1, column=1, pady=10, padx=20)
password_label.grid(row=2, column=0, padx=5)
password_entry.grid(row=2, column=1, pady=10, padx=20)
login_button.grid(row=3, column=1, columnspan=2, pady=10)

window.mainloop()