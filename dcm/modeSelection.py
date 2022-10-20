from tkinter import *
from PIL import ImageTk, Image
import pacingModes

  
background = 'white'
class ModeSelect: 
    def __init__(self, window): 
        self.window = window
        self.window.geometry('450x500')
        self.width = 400
        self.height = 450
        self.window.minsize(self.width+30, self.height+30)
        self.window.iconbitmap("images\logo.ico")
        self.window.title("Pacemaker | Mode Selection")
        self.mode = None #Will be used to keep track of the mode that is chosen by the user
                   
        def openMode(mode): 
            self.window.destroy()
            if(mode == 'AOO'): 
                pacingModes.AOO.launchAOO()
            elif(mode == 'VOO'):
                pacingModes.VOO.launchVOO()
            elif(mode == 'AAI'): 
                pacingModes.AAI.launchAAI()
            elif(mode == 'VVI'): 
                pacingModes.VVI.launchVVI()
            else: 
                print('This should not be possible. Something has gone wrong')
                
        #MS Frame
        self.msFrame = Frame(self.window, bg = background, width = self.width, height = self.height)
        self.msFrame.place(anchor="c", relx=0.5, rely=0.5)
        self.msFrame.grid_propagate(False)
        
        #Definition of elements on the page
        self.chooseLabel = Label(self.msFrame, text = "Please choose a pacing mode")
        self.aooRadio = Radiobutton(self.msFrame, text = "AOO", variable = self.modeVar, value = "AOO")
        self.vooRadio = Radiobutton(self.msFrame, text = "VOO", variable = self.modeVar, value = "VOO")
        self.aaiRadio = Radiobutton(self.msFrame, text = "AAI", variable = self.modeVar, value = "AAI")
        self.vviRadio = Radiobutton(self.msFrame, text = "VVI", variable = self.modeVar, value = "VVI")
        self.nextButton = Button(self.msFrame, text = "Next", command = openMode)
        
        #Formatting placement of elements on the page
        self.chooseLabel.grid(row = 1, column = 1, columnspan = 8)
        self.aooRadio.grid(row = 2, column = 1, sticky = W)
        self.vooRadio.grid(row = 3, column = 1, sticky = W)
        self.aaiRadio.grid(row = 4, column = 1, sticky = W)
        self.vviRadio.grid(row = 5, column = 1, sticky = W)
        self.nextButton.grid(row = 6, column = 2, sticky = W)
                
        
    
def launchModeSelect(): 
    window = Tk()
    ModeSelect(window)
    window.mainloop()
    
if __name__ == '__main__':
    launchModeSelect()

