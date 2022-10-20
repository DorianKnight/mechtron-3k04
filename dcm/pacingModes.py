from tkinter import *

background = 'white'
class AOO: 
    def __init__(self, frame):
        self.frame = frame
        self.frame.geometry('450x500')
        self.width = 400
        self.height = 450
        self.mode = None
        self.frame.minsize(self.width+30, self.height+30)
        self.frame.iconbitmap("images\logo.ico")
        self.frame.title("Pacemaker | AOO Pacing Mode")
        
        self.aooLabel = Label(self.frame, text = "AOO", font = ("Arial", 25))
        self.instructionLabel = Label(self.frame, text = "Please enter the values for the following parameters")
        self.instructionLabel2 = Label(self.frame, text  = "These values will be checked to ensure that they are valid entries")
        self.lrlLabel = Label(self.frame, text = "Lower Rate Limit:")
        self.lrlEntry = Entry(self.frame, bg = background)
        self.urlLabel = Label(self.frame, text = "Upper Rate Limit:")
        self.urlEntry = Entry(self.frame, bg = background)
        self.apwLabel = Label(self.frame, text = "Atrial Pulse Width:")
        self.apwEntry = Entry(self.frame, bg = background)
        self.aampLabel = Label(self.frame, text = "Atrial Amplitude:")
        self.aampEntry = Entry(self.frame, bg = background)
        
        self.frame.grid(padx = 50, pady = 50)
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
        self.frame.geometry('450x500')
        self.width = 400
        self.height = 450
        self.mode = None
        self.frame.minsize(self.width+30, self.height+30)
        self.frame.iconbitmap("images\logo.ico")
        self.frame.title("Pacemaker | VOO Pacing Mode")
        
    
class AAI: 
    def __init__(self, frame):
        self.frame = frame
        self.frame.geometry('450x500')
        self.width = 400
        self.height = 450
        self.mode = None
        self.frame.minsize(self.width+30, self.height+30)
        self.frame.iconbitmap("images\logo.ico")
        self.frame.title("Pacemaker | AAI Pacing Mode")
        
    
class VVI: 
    def __init__(self, frame):
        self.frame = frame
        self.frame.geometry('450x500')
        self.width = 400
        self.height = 450
        self.mode = None
        self.frame.minsize(self.width+30, self.height+30)
        self.frame.iconbitmap("images\logo.ico")
        self.frame.title("Pacemaker | VVI Pacing Mode")
        
    
def launchAOO(window): 
    AOO(window)
    #window.mainloop() #????????????
    
def launchVOO(window): 
    pass 

def launchAAI(window): 
    pass

def launchVVI(window): 
    pass

if __name__ == '__main__':
    launchAOO()
   
    