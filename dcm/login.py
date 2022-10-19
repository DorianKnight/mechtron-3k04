from tkinter import *
from PIL import ImageTk, Image

background = 'white'
class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('450x500')
        self.width = 400
        self.height = 350
        self.window.minsize(self.width+30, self.height+30)

        # ========= Login Frame =========
        self.login_frame = Frame(
            self.window,
            bg = background,
            width = self.width,
            height= self.height,
        )
        self.login_frame.place(anchor="c", relx=0.5, rely=0.5)
        self.login_frame.grid_propagate(False)

        # set weight of grid
        self.login_frame.columnconfigure(0,weight=1)
        self.login_frame.columnconfigure(1,weight=3)

        # ========= Login Text =========
        self.header_text = "Login"
        self.header = Label(self.login_frame, text = self.header_text, font=('Arial', 24, 'bold'), bg = background, fg='black')
        self.header.grid(row=0, column=0, columnspan=2, pady=(50,10))

        # ========= Login Logo =========
        self.logo_image = ImageTk.PhotoImage(Image.open("dcm/images/Complogo.png"))
        self.logo = Label(self.login_frame, image = self.logo_image, bg=background)
        self.logo.image = self.logo_image
        self.logo.grid(row=1,column=0,columnspan=2,pady=10)

        # ========= Login Entry =========
        self.username_label = Label(self.login_frame, text="Username", bg=background)
        self.username_entry = Entry(self.login_frame, bg=background)
        self.password_label = Label(self.login_frame, text="Password", bg=background)
        self.password_entry = Entry(self.login_frame, show="*", bg=background)
        self.login_button = Button(self.login_frame, text="Login", bg=background)

        # formatting entries
        self.username_label.grid(row=2, column=0, pady=5)
        self.username_entry.grid(row=2, column=1)
        self.password_label.grid(row=3, column=0, pady=5)
        self.password_entry.grid(row=3, column=1)
        self.login_button.grid(row=4, column=1, columnspan=2, pady=10)

def launchLogin():
    window = Tk()
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    launchLogin()