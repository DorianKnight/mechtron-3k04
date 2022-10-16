import tkinter as tk

background = '#333333'

window = tk.Tk()
window.title("Login form")
window.geometry('340x440')
#window.configure(bg=background)

login_label = tk.Label(window, text="Login")
username_label = tk.Label(window, text="Username")
username_entry = tk.Entry(window)
password_label = tk.Label(window, text="Password")
password_entry = tk.Entry(window, show="*")
login_button = tk.Button(window, text="Login")

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

window.mainloop()