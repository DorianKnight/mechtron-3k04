from tkinter import *
from PIL import ImageTk, Image
import pacingModes

  
background = 'white'
class ModeSelect: 
    def __init__(self, window): 
        self.window = window
        self.window.geometry('350x280')
        self.width = 300
        self.height = 220
        self.window.minsize(self.width+30, self.height+30)
        self.window.iconbitmap("images\logo.ico")
        self.window.title("Pacemaker | Mode Selection")
        self.mode = StringVar() #Will be used to keep track of the mode that is chosen by the user
        self.mode.set("None")

        def test(myStr):
            print("you selected "+myStr)  

        def openMode(): 
            self.msFrame.destroy()
            if(self.mode.get() == 'AOO'): 
                pacingModes.launchAOO(self.window)
            elif(self.mode.get() == 'VOO'):
                pacingModes.launchVOO(self.window)
            elif(self.mode.get() == 'AAI'): 
                pacingModes.launchAAI(self.window)
            elif(self.mode.get() == 'VVI'): 
                pacingModes.launchVVI(self.window)
            else: 
                print('This should not be possible. Something has gone wrong')
                print(self.mode.get())
                
        #MS Frame
        self.msFrame = Frame(self.window, bg = background, width = self.width, height = self.height)
        self.msFrame.place(anchor="c", relx=0.5, rely=0.5)
        self.msFrame.grid_propagate(False)
        
        #Definition of elements on the page
        self.chooseLabel = Label(self.msFrame, text = "Please choose a pacing mode", bg=background,padx=10,pady=20)
        self.aooRadio = Radiobutton(self.msFrame, text = "AOO", variable = self.mode, value = "AOO", bg=background,padx=10, command=test("AOO"))
        self.vooRadio = Radiobutton(self.msFrame, text = "VOO", variable = self.mode, value = "VOO", bg=background,padx=10, command=test("vOO"))
        self.aaiRadio = Radiobutton(self.msFrame, text = "AAI", variable = self.mode, value = "AAI", bg=background,padx=10, command=test("AAI"))
        self.vviRadio = Radiobutton(self.msFrame, text = "VVI", variable = self.mode, value = "VVI", bg=background,padx=10, command=test("VVI"))
        self.nextButton = Button(self.msFrame, text = "Next", command = openMode,bg=background, width=8)
        
        #Formatting placement of elements on the page
        self.chooseLabel.grid(row = 0, column = 0, columnspan = 2)
        self.aooRadio.grid(row = 1, column = 0, sticky = W)
        self.vooRadio.grid(row = 2, column = 0, sticky = W)
        self.aaiRadio.grid(row = 3, column = 0, sticky = W)
        self.vviRadio.grid(row = 4, column = 0, sticky = W)
        self.nextButton.grid(row = 5, column = 1, columnspan=2, sticky = W)
                
        
    
def launchModeSelect(): 
    window = Tk()
    ModeSelect(window).aooRadio.select()
    window.mainloop()
    
if __name__ == '__main__':
    launchModeSelect()

