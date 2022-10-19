from tkinter import *
from PIL import ImageTk, Image

background = 'white'
class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1000x1000')
        self.width = 300
        self.height = 500
        self.window.minsize(self.width+30, self.height+30)

        # ========= Login Frame =========
        self.login_frame = Frame(
            self.window,
            bg = background,
            width = self.width,
            height= self.height,
        )
        self.login_frame.place(anchor="c", relx=0.5, rely=0.5)

        # ========= Login Text =========
        self.header_text = "Login"
        self.header = Label(self.login_frame, text = self.header_text, font=('Arial', 24, 'bold'), bg = background, fg='black')
        self.header.place(anchor="n", relx=0.5, y=50)

        # ========= Login Logo =========
        self.logo = Image.open()

def launchLogin():
    window = Tk()
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    launchLogin()