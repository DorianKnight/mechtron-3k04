from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import main
import modeSelection
from connectionDisplay import displayNewDevice, displayConnection

background = 'white'
class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('450x600')
        self.width = 400
        self.height = 350
        self.window.minsize(self.width+30, self.height+40)
        self.window.iconbitmap("images\logo.ico")
        self.window.title("Pacemaker Login")

        # display whether the DCM is connected to the pacemaker
        displayConnection(self.window)
        # display whether the DCM is connected to a new pacemaker
        displayNewDevice(self.window)
        
        # function to go back to previous page (ie the welcome page)
        def goBack(): 
            self.login_frame.destroy()
            main.WelcomePage(self.window)

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

        # ========= Login =========
        self.logo_image = ImageTk.PhotoImage(Image.open("images/Complogo.png"))
        self.logo = Label(self.login_frame, image = self.logo_image, bg=background)
        self.logo.image = self.logo_image
        self.logo.grid(row=1,column=0,columnspan=2,pady=10)

        # ========= Login Entry =========
        self.username_label = Label(self.login_frame, text="Username", bg=background)
        self.username_entry = Entry(self.login_frame, bg=background)
        self.password_label = Label(self.login_frame, text="Password", bg=background)
        self.password_entry = Entry(self.login_frame, show="*", bg=background)
        self.login_button = Button(self.login_frame, text="Login", bg=background, command= self.loginUser)
        self.back_button = Button(self.login_frame, text = "Back", bg = background, command = goBack)

        # formatting entries
        self.username_label.grid(row=2, column=0, pady=5)
        self.username_entry.grid(row=2, column=1)
        self.password_label.grid(row=3, column=0, pady=5)
        self.password_entry.grid(row=3, column=1)
        self.login_button.grid(row=4, column=1, pady=10, sticky=E, padx = 25)
        self.back_button.grid(row = 4, column = 0, pady = 10, sticky = W, padx = 25)

    def loginUser(self):
        if(self.entriesCorrect()):
            usernameEntry = self.username_entry.get()
            self.login_frame.destroy()
            modeSelection.launchModeSelect(usernameEntry, self.window, main.Serobj)

    # check whether username/password entries are valid, and match a pair in the database
    def entriesCorrect(self):
        error_msg = ""
        # check validity of username/password
        no_error = True
        if (self.username_entry.get() == ''):
            error_msg = "Username cannot be empty"
            no_error = False
        elif (self.password_entry.get() == ''):
            error_msg = "Password cannot be empty"
            no_error = False

        # if entries are valid, check if they match a pair in database
        if (no_error):        
            try:
                connection = sqlite3.connect('userdata.db')
                cursor = connection.cursor()
                
                # check if username and password are in database
                cursor.execute("SELECT COUNT (username) FROM accounts WHERE username = (:username) AND password = (:password)", {
                                'username': self.username_entry.get(),
                                'password': self.password_entry.get()
                })
                account_exists = cursor.fetchone()[0] == 1
                
                if (not(account_exists)):
                    raise Exception("The login details you entered are incorrect. Please try again.")

            except Exception as ep:
                messagebox.showerror('', ep) 
                no_error = False
        else:
            messagebox.showerror('Error', error_msg)

        return no_error


def launchLogin(window):
    LoginPage(window)

if __name__ == '__main__':
    window = Tk()
    launchLogin(window)
    window.mainloop()