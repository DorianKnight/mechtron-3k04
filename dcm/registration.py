import tkinter as tk
from tkinter import messagebox
import sqlite3
import pathlib
from data import createDB

createDB()
def checkEntries():
    print("test")
    error_msg = ""
    register_error = False
    if (username_entry_reg.get() == ''):
        error_msg = "Username cannot be empty"
        register_error = True
    if (password_entry_reg.get() != password2_entry_reg.get()):
        error_msg = "test"
        register_error = True

    if (register_error == False):        
        try:
            connection = sqlite3.connect('userdata.db')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO accounts VALUES (:username, :password)", {
                            'username': username_entry_reg.get(),
                            'password': password_entry_reg.get()
            })
            connection.commit()
            tk.messagebox.showinfo('confirmation', 'Record Saved')

        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', error_msg)

window = tk.Tk()
window.title("Pacemaker | Registration")
window.iconbitmap(str(pathlib.Path(__file__).parent.resolve())+ "\logo.ico")
#window.geometry('340x440')
f = ('Trebuchet', 14)

background = '#ebebeb'
register_fr = tk.Frame(
    window,
    bd = 2,
    bg = background,
    relief = tk.SOLID,
    padx = 10,
    pady = 10
)

register_fr.pack()

tk.Label(
    register_fr,
    text = "Username",
    bg = background,
    font = f
).grid(row = 0, column = 0, sticky = tk.W, pady = 10)

tk.Label(
    register_fr,
    text = "Password",
    bg = background,
    font = f
).grid(row = 1, column = 0, sticky = tk.W, pady = 10)

tk.Label(
    register_fr,
    text = "Re-enter password",
    bg = background,
    font = f
).grid(row = 2, column = 0, sticky = tk.W, pady = 10)

username_entry_reg = tk.Entry(
    register_fr,
    font = f
)

password_entry_reg = tk.Entry(
    register_fr,
    font = f,
    show='*'
)

password2_entry_reg = tk.Entry(
    register_fr,
    font = f,
    show='*'
)


register_button = tk.Button(
    register_fr, 
    width=15, 
    text='Register', 
    font=f, 
    relief=tk.SOLID,
    command=lambda: checkEntries()
)

username_entry_reg.grid(row = 0, column = 1,pady=10, padx=20)
password_entry_reg.grid(row = 1, column = 1,pady=10, padx=20)
password2_entry_reg.grid(row = 2, column = 1,pady=10, padx=20)
register_button.grid(row = 3, column = 0, columnspan=2)
window.mainloop()

