from tkinter import *
from PIL import ImageTk, Image
import pacingModes
import main
import Patient as P
import data
from connectionDisplay import displayConnection, displayNewDevice
import SerialCommunications

background = 'white'

# allow user to choose between the different pacing modes and then bring them to corresponding page
class ModeSelect: 
    def __init__(self, window): 
        self.window = window
        self.window.geometry('500x600')
        self.width = 350
        self.height = 250
        self.window.minsize(self.width+30, self.height+50)
        self.window.iconbitmap("images\logo.ico")
        self.window.title("Pacemaker | Mode Selection")
        self.mode = StringVar() #Will be used to keep track of the mode that is chosen by the user
        self.mode.set("None")
        self.patient=P.Patient()

        def Refresh():
            # try to connect
            SerialCommunications.SerialObject() # getPortName() updates the values in connectionDisplay
            
            # remove current status
            self.connectionBanner.destroy()
            self.deviceBanner.destroy()
            
            # display the status again
            self.connectionBanner=displayConnection(self.window)
            self.deviceBanner=displayNewDevice(self.window)


        # display whether the DCM is connected to the pacemaker
        self.connectionBanner=displayConnection(self.window)
        # display whether the DCM is connected to a new pacemaker
        self.deviceBanner=displayNewDevice(self.window)
        # refresh button
        refreshBtn=Button(window,text="Refresh", fg= 'black', font=("Helvetica",12), padx=10, command=Refresh)
        refreshBtn.grid(row=0,column=4)

        # moves from current frame to frame of selected pacing mode
        def openMode(): 
            self.msFrame.destroy()
            if(self.mode.get() == 'AOO'): 
                pacingModes.launchAOO(self.window,self.patient)
            elif(self.mode.get() == 'VOO'):
                pacingModes.launchVOO(self.window,self.patient)
            elif(self.mode.get() == 'AAI'): 
                pacingModes.launchAAI(self.window,self.patient)
            elif(self.mode.get() == 'VVI'): 
                pacingModes.launchVVI(self.window,self.patient)
            elif(self.mode.get() == 'AOOR'): 
                pacingModes.launchAOOR(self.window,self.patient)
            elif(self.mode.get() == 'VOOR'): 
                pacingModes.launchVOOR(self.window,self.patient)
            elif(self.mode.get() == 'AAIR'): 
                pacingModes.launchAAIR(self.window,self.patient)
            elif(self.mode.get() == 'VVIR'): 
                pacingModes.launchVVIR(self.window,self.patient)
            elif(self.mode.get() == 'DDD'): 
                pacingModes.launchDDD(self.window,self.patient)
            elif(self.mode.get() == 'DDDR'): 
                pacingModes.launchDDDR(self.window,self.patient)
            else: 
                print('This should not be possible. Something has gone wrong')
                print(self.mode.get())
        
        # back button to welcome page
        def backToWelcome(): 
            self.msFrame.destroy()
            main.WelcomePage(self.window)
                
        #MS Frame
        self.msFrame = Frame(self.window, bg = background, width = self.width, height = self.height)
        self.msFrame.place(anchor="c", relx=0.5, rely=0.5)
        self.msFrame.grid_propagate(False)
        
        #Definition of elements on the page
        self.chooseLabel = Label(self.msFrame, text = "Please choose a pacing mode", font = ("Arial",15), bg = background, padx = 10, pady = 20)
        self.aooRadio = Radiobutton(self.msFrame, text = "AOO", variable = self.mode, value = "AOO", bg=background,padx=10)
        self.vooRadio = Radiobutton(self.msFrame, text = "VOO", variable = self.mode, value = "VOO", bg=background,padx=10)
        self.aaiRadio = Radiobutton(self.msFrame, text = "AAI", variable = self.mode, value = "AAI", bg=background,padx=10)
        self.vviRadio = Radiobutton(self.msFrame, text = "VVI", variable = self.mode, value = "VVI", bg=background,padx=10)
        self.aoorRadio = Radiobutton(self.msFrame, text = "AOOR", variable = self.mode, value = "AOOR", bg = background, padx = 10)
        self.voorRadio = Radiobutton(self.msFrame, text = "VOOR", variable = self.mode, value = "VOOR", bg = background, padx = 10)
        self.aairRadio = Radiobutton(self.msFrame, text = "AAIR", variable = self.mode, value = "AAIR", bg = background, padx = 10)
        self.vvirRadio = Radiobutton(self.msFrame, text = "VVIR", variable = self.mode, value = "VVIR", bg = background, padx = 10)
        self.dddRadio = Radiobutton(self.msFrame, text = "DDD", variable = self.mode, value = "DDD", bg = background, padx = 10)
        self.dddrRadio = Radiobutton(self.msFrame, text = "DDDR", variable = self.mode, value = "DDDR", bg = background, padx = 10)
        self.backButton = Button(self.msFrame, text = "Back to Welcome Page", command = backToWelcome, bg = background)
        self.nextButton = Button(self.msFrame, text = "Next", command = openMode,bg=background, width=8)
        
        #Formatting placement of elements on the page
        self.chooseLabel.grid(row = 0, column = 0, columnspan = 2)
        self.aooRadio.grid(row = 1, column = 0, sticky = W, padx = 20)
        self.vooRadio.grid(row = 2, column = 0, sticky = W, padx = 20)
        self.aaiRadio.grid(row = 3, column = 0, sticky = W, padx = 20)
        self.vviRadio.grid(row = 4,column = 0, sticky = W, padx = 20)
        self.aoorRadio.grid(row = 1, column = 1, sticky = W, padx = 20)
        self.voorRadio.grid(row = 2, column = 1, sticky = W, padx = 20)
        self.aairRadio.grid(row = 3, column = 1, sticky = W, padx = 20) 
        self.vvirRadio.grid(row = 4, column = 1, sticky = W, padx = 20)
        self.dddRadio.grid(row = 5, column = 0, sticky = W, padx = 20)
        self.dddrRadio.grid(row = 5, column = 1, sticky = W, padx = 20)
        self.backButton.grid(row = 6,column = 0, sticky = W, padx = 20, pady = 20)
        self.nextButton.grid(row = 6, column = 1, columnspan=2, sticky = E, pady = 20)
                
        
# opens mode select page
def launchModeSelect(username): 
    window = Tk()
    MS=ModeSelect(window)
    MS.patient.username=username
    MS.patient.copyFromDB()
    
    # initially selects last-selected pacing mode by default
    if(MS.patient.pacingMode=="VOO"):
        MS.vooRadio.select()
    elif(MS.patient.pacingMode=="AOO"):
        MS.aooRadio.select()
    elif(MS.patient.pacingMode=="VVI"):
        MS.vviRadio.select()
    elif(MS.patient.pacingMode=="AAI"):
        MS.aaiRadio.select()
    elif(MS.patient.pacingMode=="AOOR"):
        MS.aoorRadio.select()
    elif(MS.patient.pacingMode=="VOOR"):
        MS.voorRadio.select()
    elif(MS.patient.pacingMode=="AAIR"):
        MS.aairRadio.select()
    elif(MS.patient.pacingMode=="VVIR"):
        MS.vvirRadio.select()
    elif(MS.patient.pacingMode=="DDDR"):
        MS.dddrRadio.select()
    else:
        MS.dddRadio.select() #nominal mode
    

    window.mainloop()