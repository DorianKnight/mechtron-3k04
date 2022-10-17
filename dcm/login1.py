from tkinter import *
#from Pillow import ImageTk, Image

background = 'black'
class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1000x1000')
        self.window.background
        # ======= Login Frame =========
        self.login_fr = Frame(
            self.window,
            bg = background,
            padx = 10,
            pady = 10
        )
        self.login_fr.pack()
        self.header_text = "Pacemaker"
        self.header = Label(self.login_fr, text = self.header_text, font=('Arial', 24, 'bold'), bg = background, fg='white')
        self.header.place(x=90, y=30,width=300, height=30)

        # ======= Login Frame =========

def main():
    window = Tk()
    LoginPage(window)
    window.mainloop()

main()