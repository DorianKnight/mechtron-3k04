from tkinter import *
from tkinter import messagebox
import sqlite3
import pathlib
from data import createDB
from PIL import ImageTk, Image
import main
import modeSelection
# from connectionDisplay import displayConnection, displayNewDevice


createDB()
background = 'white'

class RegistrationPage:
    def __init__(self, window, max_accounts):
        self.window = window
        self.window.geometry('450x500')
        self.width = 400
        self.height = 400
        self.window.minsize(self.width+30, self.height+30)
        self.max_accounts = max_accounts
        self.window.title("Pacemaker Register")

        '''
        # display whether the DCM is connected to the pacemaker
        displayConnection(self.window)
        # display whether the DCM is connected to a new pacemaker
        displayNewDevice(self.window)
        '''

        def goBack(): 
            self.frame.destroy()
            main.WelcomePage(self.window)

        # ========= Registration Frame =========
        self.frame = Frame(
            self.window,
            bg = background,
            width = self.width,
            height= self.height,
        )
        self.frame.place(anchor="c", relx=0.5, rely=0.5)
        self.frame.grid_propagate(False)

        # set weight of grid
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1,weight=3)

        # ========= Registration Text =========
        self.header_text = "Register"
        self.header = Label(self.frame, text = self.header_text, font=('Arial', 24, 'bold'), bg = background, fg='black')
        self.header.grid(row=0, column=0, columnspan=2, pady=(50,10))

        # ========= Logo =========
        self.logo_image = ImageTk.PhotoImage(Image.open("images/Complogo.png"))
        self.logo = Label(self.frame, image = self.logo_image, bg=background)
        self.logo.image = self.logo_image
        self.logo.grid(row=1,column=0,columnspan=2,pady=10)

        # ========= Registration Entry =========
        self.username_label = Label(self.frame, text="Username", bg=background)
        self.username_entry = Entry(self.frame, bg=background)
        self.password_label = Label(self.frame, text="Password", bg=background)
        self.password_entry = Entry(self.frame, show="*", bg=background)
        self.password2_label = Label(self.frame, text="Re-enter password", bg=background)
        self.password2_entry = Entry(self.frame, show="*", bg=background)
        self.register_button = Button(self.frame, text="Register", bg=background,command= self.registerUser)
        self.back_button = Button(self.frame, text = "Back", bg = background, command = goBack)

        # formatting entries
        self.username_label.grid(row=2, column=0, sticky='w',pady=5, padx=(25,0))
        self.username_entry.grid(row=2, column=1)
        self.password_label.grid(row=3, column=0, pady=5, sticky='w', padx=(25,0))
        self.password_entry.grid(row=3, column=1)
        self.password2_label.grid(row=4, column=0, pady=5, sticky='w', padx=(25,0))
        self.password2_entry.grid(row=4, column=1)
        self.register_button.grid(row=5, column=1, pady=10, sticky = E, padx = 25)
        self.back_button.grid(row = 5, column = 0, pady = 10, sticky = W, padx = 25)

    def registerUser(self):
        error_msg = self.checkEntryErrors() # check for entry validity errors

        # if there is no error, check to see if the username is not already being used and then register account
        if (error_msg == ""):   
            try:
                connection = sqlite3.connect('userdata.db')
                cursor = connection.cursor()
                
                # check number of users
                cursor.execute("SELECT COUNT(username) FROM accounts")
                num_accounts = cursor.fetchone()[0]

                if (num_accounts == None or num_accounts >= self.max_accounts):
                    raise Exception("There are already 10 accounts. You have reached the maximum.")
                
                # ensure username does not yet exist
                cursor.execute("SELECT COUNT (username) FROM accounts WHERE username = (:username)", {
                                'username': self.username_entry.get()
                })
                new_user = cursor.fetchone()[0] == 0
                
                if (not(new_user)):
                    raise Exception("This username is already in use")

                # make new user with nominal values
                cursor.execute("INSERT INTO accounts VALUES (:username, :password, :pacingMode,:lrl,:url,:apw,:vpw,:aamp,:vamp,:asens,:vsens,:arp,:vrp,:pvarp,:actThr,:reactTime,:respFactor,:recoveryTime,:maxSensRate,:fixedAVdelay)", {
                                'username': self.username_entry.get(),
                                'password': self.password_entry.get(),
                                'lrl': 60,
                                'url': 120,
                                'pacingMode': "DDD",
                                'apw': 1,
                                'vpw': 1,
                                'aamp': 5,
                                'vamp': 5,
                                'asens': 2.5,
                                'vsens': 2.5,
                                'arp': 250,
                                'vrp': 320,
                                'pvarp': 250,
                                'actThr': "Med",
                                'reactTime': 30,
                                'respFactor': 8,
                                'recoveryTime': 5,
                                'maxSensRate': 120,
                                'fixedAVdelay': 150
                })
                connection.commit()
                self.goToModeSelect()
                #messagebox.showinfo('confirmation', 'User Saved')

            except Exception as ep:
                messagebox.showerror('', ep) 
        else:
            messagebox.showerror('Error', error_msg)
            
    def checkEntryErrors(self):
        if (self.username_entry.get() == ''):
            return "Username cannot be empty."
        if (self.password_entry.get() == ''):
            return "Password cannot be empty."
        if (self.password_entry.get() != self.password2_entry.get()):
            return "Passwords do not match."
        
        # disallow usernames with spaces
        if (" " in self.username_entry.get()):
            return "Username cannot have a space."

        # edge case where password cannot be " "
        if (self.password_entry.get() == " "):
            return "Password cannot be just a space."

        # if no errors, return empty string
        return ""
    
    def goToModeSelect(self): 
        usernameEntry=self.username_entry.get()
        self.frame.destroy()
        modeSelection.launchModeSelect(usernameEntry, self.window)

def launchRegistration(window):
    RegistrationPage(window,10)

if __name__ == '__main__':
    window = Tk()
    RegistrationPage(window,10)
    window.iconbitmap("images\logo.ico")
    launchRegistration(window)
    window.mainloop()