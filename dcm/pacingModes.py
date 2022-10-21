from tkinter import *
from PIL import ImageTk, Image


background = 'white'
class AOO: 
    def __init__(self, frame):
        self.frame = frame
        self.frame.geometry('400x230')
        self.width = 350
        self.height = 180
        self.frame.minsize(self.width+30, self.height+30)
        self.frame.iconbitmap("images\logo.ico")
        self.frame.title("Pacemaker | AOO Pacing Mode")
        
        #AOO Frame
        self.aooFrame = Frame(self.frame, bg = background, width = self.width, height = self.height)
        self.aooFrame.place(anchor="c", relx=0.5, rely=0.5)
        self.aooFrame.grid_propagate(False)
        
        #Elements on the page
        self.aooLabel = Label(self.aooFrame, text = "AOO", font = ("Arial", 25), bg = background, padx = 10)
        self.instructionLabel = Label(self.aooFrame, text = "Please enter the values for the following parameters", bg = background, padx = 10)
        self.instructionLabel2 = Label(self.aooFrame, text  = "These values will be checked to ensure that they are valid entries", bg = background, padx = 10)
        self.lrlLabel = Label(self.aooFrame, text = "Lower Rate Limit:", bg = background, padx = 10)
        self.lrlEntry = Entry(self.aooFrame, bg = background)
        self.urlLabel = Label(self.aooFrame, text = "Upper Rate Limit:", bg = background, padx = 10)
        self.urlEntry = Entry(self.aooFrame, bg = background)
        self.apwLabel = Label(self.aooFrame, text = "Atrial Pulse Width:", bg = background, padx = 10)
        self.apwEntry = Entry(self.aooFrame, bg = background)
        self.aampLabel = Label(self.aooFrame, text = "Atrial Amplitude:", bg = background, padx = 10)
        self.aampEntry = Entry(self.aooFrame, bg = background)
        
        self.aooFrame.grid()
        self.aooLabel.grid(row = 1, column = 1, columnspan = 2)
        self.instructionLabel.grid(row = 2, column = 1, columnspan = 2)
        self.instructionLabel2.grid(row = 3, column = 1, columnspan = 2)
        self.lrlLabel.grid(row = 4, column = 1, sticky = W)
        self.lrlEntry.grid(row = 4, column = 2, sticky = W)
        self.urlLabel.grid(row = 5, column = 1, sticky = W)
        self.urlEntry.grid(row = 5, column = 2, sticky = W)
        self.apwLabel.grid(row = 6, column = 1, sticky = W)
        self.apwEntry.grid(row = 6, column = 2, sticky = W)
        self.aampLabel.grid(row = 7, column = 1, sticky = W)
        self.aampEntry.grid(row = 7, column = 2, sticky = W)

        
    
class VOO: 
    def __init__(self, frame):
        self.frame = frame
        self.frame.geometry('450x300')
        self.width = 400
        self.height = 250
        self.frame.minsize(self.width+30, self.height+30)
        self.frame.iconbitmap("images\logo.ico")
        self.frame.title("Pacemaker | VOO Pacing Mode")
        
        #VOO Frame
        self.vooFrame = Frame(self.frame, bg = background, width = self.width, height = self.height)
        self.vooFrame.place(anchor="c", relx=0.5, rely=0.5)
        self.vooFrame.grid_propagate(False)
        
        #Elements on the page
        self.vooLabel = Label(self.vooFrame, text = "VOO", font = ("Arial", 25), bg = background, padx = 10)
        self.instructionLabel = Label(self.vooFrame, text = "Please enter the values for the following parameters", bg = background, padx = 10)
        self.instructionLabel2 = Label(self.vooFrame, text  = "These values will be checked to ensure that they are valid entries", bg = background, padx = 10)
        self.lrlLabel = Label(self.vooFrame, text = "Lower Rate Limit:", bg = background, padx = 10)
        self.lrlEntry = Entry(self.vooFrame)
        self.urlLabel = Label(self.vooFrame, text = "Upper Rate Limit:", bg = background, padx = 10)
        self.urlEntry = Entry(self.vooFrame)
        self.vpwLabel = Label(self.vooFrame, text = "Ventrical Pulse Width:", bg = background, padx = 10)
        self.vpwEntry = Entry(self.vooFrame)
        self.vampLabel = Label(self.vooFrame, text = "Ventrical Amplitude:", bg = background, padx = 10)
        self.vampEntry = Entry(self.vooFrame)
        
        #Positioning all VOO Elements
        self.vooFrame.grid()
        self.vooLabel.grid(row = 1, column = 1, columnspan = 2)
        self.instructionLabel.grid(row = 2, column = 1, columnspan = 2)
        self.instructionLabel2.grid(row = 3, column = 1, columnspan = 2)
        self.lrlLabel.grid(row = 4, column = 1, sticky = W)
        self.lrlEntry.grid(row = 4, column = 2, sticky = W)
        self.urlLabel.grid(row = 5, column = 1, sticky = W)
        self.urlEntry.grid(row = 5, column = 2, sticky = W)
        self.vpwLabel.grid(row = 6, column = 1, sticky = W)
        self.vpwEntry.grid(row = 6, column = 2, sticky = W)
        self.vampLabel.grid(row = 7, column = 1, sticky = W)
        self.vampEntry.grid(row = 7, column = 2, sticky = W)



    
class AAI: 
    def __init__(self, frame):
        self.frame = frame
        self.frame.geometry('500x400')
        self.width = 450
        self.height = 350
        self.frame.minsize(self.width+30, self.height+30)
        self.frame.iconbitmap("images\logo.ico")
        self.frame.title("Pacemaker | AAI Pacing Mode")
        
        #AAI Frame
        self.aaiFrame = Frame(self.frame, bg = background, width = self.width, height = self.height)
        self.aaiFrame.place(anchor="c", relx=0.5, rely=0.5)
        self.aaiFrame.grid_propagate(False)
        
        #Creating all the elements for the AAI Page
        self.aaiLabel = Label(self.aaiFrame, text = "AAI", font = ("Arial", 25), bg = background, padx = 10)
        self.instructionLabel = Label(self.aaiFrame, text = "Please enter the values for the following parameters", bg = background, padx = 10)
        self.instructionLabel2 = Label(self.aaiFrame, text  = "These values will be checked to ensure that they are valid entries", bg = background, padx = 10)
        self.lrlLabel = Label(self.aaiFrame, text = "Lower Rate Limit:", bg = background, padx = 10)
        self.lrlEntry = Entry(self.aaiFrame)
        self.urlLabel = Label(self.aaiFrame, text = "Upper Rate Limit:", bg = background, padx = 10)
        self.urlEntry = Entry(self.aaiFrame)
        self.apwLabel = Label(self.aaiFrame, text = "Atrial Pulse Width:", bg = background, padx = 10)
        self.apwEntry = Entry(self.aaiFrame)
        self.aampLabel = Label(self.aaiFrame, text = "Atrial Amplitude:", bg = background, padx = 10)
        self.aampEntry = Entry(self.aaiFrame)
        self.asensLabel = Label(self.aaiFrame, text = "Atrial Sensitivity:", bg = background, padx = 10)
        self.asensEntry = Entry(self.aaiFrame)
        self.arpLabel = Label(self.aaiFrame, text = "ARP:", bg = background, padx = 10)
        self.arpEntry = Entry(self.aaiFrame)
        self.pvarpLabel = Label(self.aaiFrame, text = "PVARP:", bg = background, padx = 10)
        self.pvarpEntry = Entry(self.aaiFrame)
        self.hystLabel = Label(self.aaiFrame, text = "Hysteresis:", bg = background, padx = 10)
        self.hystEntry = Entry(self.aaiFrame)
        self.rsLabel = Label(self.aaiFrame, text = "Rate Smoothing:", bg = background, padx = 10)
        self.rsEntry = Entry(self.aaiFrame)
        
        self.aaiFrame.grid(padx = 50, pady = 50)
        self.aaiLabel.grid(row = 1, column = 1)
        self.instructionLabel.grid(row = 2, column = 1, columnspan = 2)
        self.instructionLabel2.grid(row = 3, column = 1, columnspan = 2)
        self.lrlLabel.grid(row = 4, column = 1, sticky = W)
        self.lrlEntry.grid(row = 4, column = 2, sticky = W)
        self.urlLabel.grid(row = 5, column = 1, sticky = W)
        self.urlEntry.grid(row = 5, column = 2, sticky = W)
        self.apwLabel.grid(row = 6, column = 1, sticky = W)
        self.apwEntry.grid(row = 6, column = 2, sticky = W)
        self.aampLabel.grid(row = 7, column = 1, sticky = W)
        self.aampEntry.grid(row = 7, column = 2, sticky = W)
        self.asensLabel.grid(row = 8, column = 1, sticky = W)
        self.asensEntry.grid(row = 8, column = 2, sticky = W)
        self.arpLabel.grid(row = 9, column = 1, sticky = W)
        self.arpEntry.grid(row = 9, column = 2, sticky = W)
        self.pvarpLabel.grid(row = 10, column = 1, sticky = W)
        self.pvarpEntry.grid(row = 10, column = 2, sticky = W)
        self.hystLabel.grid(row = 11, column = 1, sticky = W)
        self.hystEntry.grid(row = 11, column = 2, sticky = W)
        self.rsLabel.grid(row = 12, column = 1, sticky = W)
        self.rsEntry.grid(row = 12, column = 2, sticky = W)

    
class VVI: 
    def __init__(self, frame):
        self.frame = frame
        self.frame.geometry('425x350')
        self.width = 375
        self.height = 300
        self.frame.minsize(self.width+30, self.height+30)
        self.frame.iconbitmap("images\logo.ico")
        self.frame.title("Pacemaker | VVI Pacing Mode")
        
        #VVI Frame
        self.vviFrame = Frame(self.frame, bg = background, width = self.width, height = self.height)
        self.vviFrame.place(anchor="c", relx=0.5, rely=0.5)
        self.vviFrame.grid_propagate(False)
        
        #Creating the elements for the VVI Frame
        self.vviLabel = Label(self.vviFrame, text = "VVI", font = ("Arial", 25), bg = background, padx = 10)
        self.instructionLabel = Label(self.vviFrame, text = "Please enter the values for the following parameters", bg = background, padx = 10)
        self.instructionLabel2 = Label(self.vviFrame, text  = "These values will be checked to ensure that they are valid entries", bg = background, padx = 10)
        self.lrlLabel = Label(self.vviFrame, text = "Lower Rate Limit:", bg = background, padx = 10)
        self.lrlEntry = Entry(self.vviFrame)
        self.urlLabel = Label(self.vviFrame, text = "Upper Rate Limit:", bg = background, padx = 10)
        self.urlEntry = Entry(self.vviFrame)
        self.vpwLabel = Label(self.vviFrame, text = "Ventricular Pulse Width:", bg = background, padx = 10)
        self.vpwEntry = Entry(self.vviFrame)
        self.vampLabel = Label(self.vviFrame, text = "Ventricular Amplitude:", bg = background, padx = 10)
        self.vampEntry = Entry(self.vviFrame)
        self.vsensLabel = Label(self.vviFrame, text = "Ventricular Sensitivity:", bg = background, padx = 10)
        self.vsensEntry = Entry(self.vviFrame)
        self.hystLabel = Label(self.vviFrame, text = "Hysteresis:", bg = background, padx = 10)
        self.hystEntry = Entry(self.vviFrame)
        self.rsLabel = Label(self.vviFrame, text = "Rate Smoothing:", bg = background, padx = 10) 
        self.rsEntry = Entry(self.vviFrame)
        
        #Placing the element on the VOO Frame
        self.vviFrame.grid()
        self.vviLabel.grid(row = 1, column= 1)
        self.instructionLabel.grid(row = 2, column = 1, columnspan = 2)
        self.instructionLabel2.grid(row = 3, column = 1, columnspan = 2)
        self.lrlLabel.grid(row = 4, column = 1, sticky = W)
        self.lrlEntry.grid(row = 4, column = 2, sticky = W)
        self.urlLabel.grid(row = 5, column = 1, sticky = W)
        self.urlEntry.grid(row = 5, column = 2, sticky = W)
        self.vpwLabel.grid(row = 6, column = 1, sticky = W)
        self.vpwEntry.grid(row = 6, column = 2, sticky = W)
        self.vampLabel.grid(row = 7, column = 1, sticky = W)
        self.vampEntry.grid(row = 7, column = 2, sticky = W)
        self.vsensLabel.grid(row = 8, column = 1, sticky = W)
        self.vsensEntry.grid(row = 8, column = 2, sticky = W)
        self.hystLabel.grid(row = 9, column = 1, sticky = W)
        self.hystEntry.grid(row = 9, column = 2, sticky = W)
        self.rsLabel.grid(row = 10, column = 1, sticky = W)
        self.rsEntry.grid(row = 10, column = 2, sticky = W)

    
def launchAOO(window): 
    AOO(window)
    
def launchVOO(window): 
    VOO(window)

def launchAAI(window): 
    AAI(window)

def launchVVI(window): 
    VVI(window)
   
    