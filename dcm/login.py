import tkinter as tk

background = '#333333'

window = tk.Tk()
window.title("Login form")
window.geometry('320x190')
window.minsize(320, 190)
window.maxsize(320, 190)
#window.configure(bg=background)

login_label = tk.Label(window, text="Login")
username_label = tk.Label(window, text="Username")
username_entry = tk.Entry(window)
password_label = tk.Label(window, text="Password")
password_entry = tk.Entry(window, show="*")
login_button = tk.Button(window, text="Login")


# Placing widgets on the screen
login_label.grid(row=0, column=1, columnspan=2, sticky="news", pady=10)
username_label.grid(row=1, column=0, padx=10)
username_entry.grid(row=1, column=1, pady=10, padx=10)
password_label.grid(row=2, column=0, padx=10)
password_entry.grid(row=2, column=1, pady=10, padx=10)
login_button.grid(row=3, column=1, columnspan=2, pady=10)

window.mainloop()