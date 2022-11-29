from tkinter import *
from PIL import ImageTk, Image
import login
import registration
from data import createDB, indexExists
import connectionDisplay as CD
import SerialCommunications

background = 'white'
class WelcomePage:
    def __init__(self, window, Serobj):
        self.window = window
        self.window.geometry('450x600')
        self.width = 400
        self.height = 450
        self.window.minsize(self.width+30, self.height+40)
        self.window.iconbitmap("images\logo.ico")
        self.window.title("Pacemaker")
        self.Serobj = Serobj
        def Refresh():
            # try to connect
            global Serobj 
            SerialCommunications.checkHeartSer()
            if (SerialCommunications.getPortName() != '' and self.Serobj == None):
                print("Ive been created hahahah")
            oldUser=indexExists(2) # returns a bool stating whether the int passed exists as an index in the database (minimum index is 0)
            #call indexExists and pass in the "user identifier" int stored in the pacemaker

            #update newdevicechecker (connection checker is already updated in getPortName())
            if(oldUser): #old user, exists in db
                CD.newDeviceChecker=False
            else: #new user
                CD.newDeviceChecker=True
                

            # remove current status
            self.connectionBanner.destroy()
            self.deviceBanner.destroy()
            
            # display the status again
            self.connectionBanner=CD.displayConnection(self.window)
            self.deviceBanner=CD.displayNewDevice(self.window)


        # display whether the DCM is connected to the pacemaker
        self.connectionBanner=CD.displayConnection(self.window)
        # display whether the DCM is connected to a new pacemaker
        self.deviceBanner=CD.displayNewDevice(self.window)
        # refresh button
        refreshBtn=Button(window,text="Refresh", fg= 'black', font=("Helvetica",12), padx=10, command=Refresh)
        refreshBtn.grid(row=0,column=4)

        # refresh automatically when window is instantiated
        Refresh()

        def openLoginWin():
            self.welcome_frame.destroy()
            login.launchLogin(self.window, self.Serobj)


        def openRegisterWin():
            self.welcome_frame.destroy()
            registration.launchRegistration(self.window, self.Serobj)

        # ========= Welcome Frame =========
        self.welcome_frame = Frame(
            self.window,
            bg = background,
            width = self.width,
            height= self.height,
        )
        self.welcome_frame.place(anchor="c", relx=0.5, rely=0.5)
        self.welcome_frame.grid_propagate(False)

        # set weight of grid
        self.welcome_frame.columnconfigure(0,weight=1)
        self.welcome_frame.columnconfigure(1,weight=3)

        # ========= Welcome Text =========
        self.header_text = "Welcome"
        self.header = Label(self.welcome_frame, text = self.header_text, font=('Arial', 24, 'bold'), bg = background, fg='black')
        self.header.grid(row=0, column=0, columnspan=2, pady=(50,10))

        # ========= Welcome Logo =========
        self.logo_image = ImageTk.PhotoImage(Image.open("images/welcomeLogo.png"))
        self.logo = Label(self.welcome_frame, image = self.logo_image, bg=background)
        self.logo.image = self.logo_image
        self.logo.grid(row=1,column=0,columnspan=2,pady=10)

        # ========= Welcome Entry =========
        self.login_button = Button(self.welcome_frame, text="Login", width = 30, bg=background, command=openLoginWin)
        self.register_button = Button(self.welcome_frame, text="Register", width = 30, bg=background, command=openRegisterWin)

        # formatting entries
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.register_button.grid(row=3, column=0, columnspan=2)
        

def launchApp():
    createDB()
    serObj = SerialCommunications.SerialObject()
    window = Tk()
    WelcomePage(window, serObj)
    window.mainloop()


if __name__ == '__main__':
    launchApp()