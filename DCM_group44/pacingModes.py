from tkinter import *
from PIL import ImageTk, Image
import modeSelection
import Patient as P

background = 'white'

class PacingMode:
    def __init__(self, window):
        self.window = window
        self.window.geometry('500x500')
        self.window.iconbitmap("images\logo.ico")
        self.patient = P.Patient()

    def initFrame(self):
        self.frame = Frame(self.window, bg = background, width = self.width, height = self.height)
        self.frame.place(anchor="c", relx=0.5, rely=0.5)
        self.frame.grid_propagate(False)
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1,weight=3)
        
    def goBack(self, radioBtn): 
            self.frame.destroy()
            MS=modeSelection.ModeSelect(self.window)
            getattr(MS, radioBtn).select()
            MS.patient=self.patient

    def addTitleAndInstructions(self, mode):
        # title and instructions
        self.titleLabel = Label(self.frame, text = mode, font = ("Arial", 24), bg = background, padx = 20, pady = 10)
        self.instructionLabel = Label(self.frame, text = "Please enter the values for the following parameters.", bg = background, padx = 20)
        self.instructionLabel2 = Label(self.frame, text  = "These values will be checked to ensure that they are valid entries.", bg = background, padx = 20)
        self.instructionLabel3 = Label(self.frame, text  = "If you have not set any values yet, they will be set to default.", bg = background, padx = 20)

        self.titleLabel.grid(row = 0, column = 0, columnspan = 2)
        self.instructionLabel.grid(row = 1, column = 0, columnspan = 2)
        self.instructionLabel2.grid(row = 2, column = 0, columnspan = 2)
        self.instructionLabel3.grid(row = 3, column = 0, columnspan = 2)

        # add blank row before back and confirm buttons
        self.frame.grid_rowconfigure(4, minsize = 20)

    def addLrl(self, r):
        self.lrlLabel = Label(self.frame, text = "Lower Rate Limit:", bg = background, padx = 20)
        self.lrlEntry = Entry(self.frame, bg = background)
        self.lrlLabel.grid(row = r, column = 0, sticky = W)
        self.lrlEntry.grid(row = r, column = 1)
        self.lrlEntry.insert(0,self.patient.lrl)

    def addUrl(self, r):
        self.urlLabel = Label(self.frame, text = "Upper Rate Limit:", bg = background, padx = 20)
        self.urlEntry = Entry(self.frame, bg = background)
        self.urlLabel.grid(row = r, column = 0, sticky = W)
        self.urlEntry.grid(row = r, column = 1)
        self.urlEntry.insert(0,self.patient.url)

    def addApw(self, r):
        self.apwLabel = Label(self.frame, text = "Atrial Pulse Width:", bg = background, padx = 20)
        self.apwEntry = Entry(self.frame, bg = background)
        self.apwLabel.grid(row = r, column = 0, sticky = W)
        self.apwEntry.grid(row = r, column = 1)
        self.apwEntry.insert(0,self.patient.apw)

    def addAamp(self, r):
        self.aampLabel = Label(self.frame, text = "Atrial Amplitude:", bg = background, padx = 20)
        self.aampEntry = Entry(self.frame, bg = background)
        self.aampLabel.grid(row = r, column = 0, sticky = W)
        self.aampEntry.grid(row = r, column = 1)
        self.aampEntry.insert(0,self.patient.aamp)

    def addBackAndConfirm(self, r, cmdBack, cmdConfirm):
        # add blank row before back and confirm buttons
        self.frame.grid_rowconfigure(r, minsize = 20)

        self.back = Button(self.frame, text = "Back", width=12, command = cmdBack)
        self.back.grid(row = r+1, column = 0, sticky=S)
        self.confirm = Button(self.frame, text = "Confirm changes", width=12, command = cmdConfirm)
        self.confirm.grid(row = r+1, column = 1, sticky=SE, padx = 40)

    def addVpw(self, r):
        self.vpwLabel = Label(self.frame, text = "Ventrical Pulse Width:", bg = background, padx = 20)
        self.vpwEntry = Entry(self.frame, bg = background)
        self.vpwLabel.grid(row = r, column = 0, sticky = W)
        self.vpwEntry.grid(row = r, column = 1)
        self.vpwEntry.insert(0,self.patient.vpw)

    def addVamp(self, r):
        self.vampLabel = Label(self.frame, text = "Ventrical Amplitude:", bg = background, padx = 20)
        self.vampEntry = Entry(self.frame, bg=background)
        self.vampLabel.grid(row = r, column = 0, sticky = W)
        self.vampEntry.grid(row = r, column = 1)
        self.vampEntry.insert(0,self.patient.vamp)

    def addAsens(self, r):
        self.asensLabel = Label(self.frame, text = "Atrial Sensitivity:", bg = background, padx = 20)
        self.asensEntry = Entry(self.frame, bg=background)
        self.asensLabel.grid(row = r, column = 0, sticky = W)
        self.asensEntry.grid(row = r, column = 1)
        self.asensEntry.insert(0,self.patient.asens)

    def addArp(self, r):
        self.arpLabel = Label(self.frame, text = "ARP:", bg = background, padx = 20)
        self.arpEntry = Entry(self.frame, bg=background)
        self.arpLabel.grid(row = r, column = 0, sticky = W)
        self.arpEntry.grid(row = r, column = 1)
        self.arpEntry.insert(0,self.patient.arp)

    def addPvarp(self, r):
        self.pvarpLabel = Label(self.frame, text = "PVARP:", bg = background, padx = 20)
        self.pvarpEntry = Entry(self.frame, bg=background)
        self.pvarpLabel.grid(row = r, column = 0, sticky = W)
        self.pvarpEntry.grid(row = r, column = 1)
        self.pvarpEntry.insert(0,self.patient.pvarp)        

    def addHyst(self, r):
        boolState="normal"
        if(self.patient.hystBool==0):
            boolState="disabled"
    
        self.hystBool=bool(self.patient.hystBool)

        self.hystCheck = Checkbutton(self.frame,text = "Hysteresis:",command=self.updateFields, bg=background,padx = 20)
        self.hystCheck.grid(row=r,column=0,sticky=W, padx = 20)

        # set whether checkmark is initially selected based on saved values
        if(self.patient.hystBool==0):
            self.hystCheck.deselect()
        else:
            self.hystCheck.select()

        self.hystEntry = Entry(self.frame, bg=background, state=boolState)
        self.hystEntry.grid(row = r, column = 1)
        self.hystEntry.insert(0,self.patient.hrl)

    def addRs(self, r):
        self.rsLabel = Label(self.frame, text = "Rate Smoothing:", bg = background, padx = 20)
        self.rsEntry = Entry(self.frame, bg=background)
        self.rsLabel.grid(row = r, column = 0, sticky = W)
        self.rsEntry.grid(row = r, column = 1)
        self.rsEntry.insert(0,self.patient.rs)
    
    def addVsens(self, r):
        self.vsensLabel = Label(self.frame, text = "Ventricular Sensitivity:", bg = background, padx = 20)
        self.vsensEntry = Entry(self.frame, bg=background)
        self.vsensLabel.grid(row = r, column = 0, sticky = W)
        self.vsensEntry.grid(row = r, column = 1)
        self.vsensEntry.insert(0,self.patient.vsens)

    def updateFields(self):
        self.hystBool = not(self.hystBool)
        if(self.hystBool):
            self.hystEntry.config(state= "normal")
        else:
            self.hystEntry.config(state= "disabled")

class AOO(PacingMode): 
    def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 350
        self.window.title("Pacemaker | AOO Pacing Mode")
        self.patient=patient
        
        #Methods
        def aooConfirm(): 
            updatePatient()
            if(self.patient.numsValid("AOO")):
                self.patient.saveToDB()
        
        def goBack(): 
            self.goBack("aooRadio")

        def updatePatient():
            self.patient.pacingMode="AOO"
            self.patient.lrl=self.lrlEntry.get()
            self.patient.url=self.urlEntry.get()
            self.patient.apw=self.apwEntry.get()
            self.patient.aamp=self.aampEntry.get()

        
        #AOO Frame
        self.initFrame()
        
        #Elements on the page
        self.addTitleAndInstructions("AOO")
        self.addLrl(5)
        self.addUrl(6)
        self.addApw(7)
        self.addAamp(8)
        self.addBackAndConfirm(9, goBack, aooConfirm)

class VOO(PacingMode): 
    def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 350
        self.window.title("Pacemaker | VOO Pacing Mode")
        self.patient=patient
        
        #Methods
        def vooConfirm(): 
            updatePatient()
            if(self.patient.numsValid("VOO")):
                self.patient.saveToDB()
        
        def goBack(): 
            self.goBack("vooRadio")

        def updatePatient():
            self.patient.pacingMode="VOO"
            self.patient.lrl=self.lrlEntry.get()
            self.patient.url=self.urlEntry.get()
            self.patient.vpw=self.vpwEntry.get()
            self.patient.vamp=self.vampEntry.get()
        
        #VOO Frame
        self.initFrame()
        
        #Elements on the page
        self.addTitleAndInstructions("VOO")
        self.addLrl(5)
        self.addUrl(6)
        self.addVpw(7)
        self.addVamp(8)
        self.addBackAndConfirm(9, goBack, vooConfirm)

class AAI(PacingMode): 
    def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 450
        self.window.title("Pacemaker | AAI Pacing Mode")
        self.patient=patient

        #set these to patient specific parameters
        
        #Methods 
        def aaiConfirm(): 
            updatePatient()
            if(self.patient.numsValid("AAI")):
                self.patient.saveToDB()
        
        def goBack(): 
            self.goBack("aaiRadio")

        def updatePatient():
            self.patient.pacingMode="AAI"
            self.patient.lrl=self.lrlEntry.get()
            self.patient.url=self.urlEntry.get()
            self.patient.apw=self.apwEntry.get()
            self.patient.aamp=self.aampEntry.get()
            self.patient.asens=self.asensEntry.get()
            self.patient.arp=self.arpEntry.get()
            self.patient.pvarp=self.pvarpEntry.get()
            self.patient.hystBool=self.hystBool
            self.patient.hrl=self.hystEntry.get()
            self.patient.rs=self.rsEntry.get()

        #AAI Frame
        self.initFrame()
        
        #Creating all the elements for the AAI Page
        self.addTitleAndInstructions("AAI")
        self.addLrl(5)
        self.addUrl(6)
        self.addApw(7)
        self.addAamp(8)
        self.addAsens(9)
        self.addArp(10)
        self.addPvarp(11)
        self.addHyst(12)
        self.addRs(13)
        self.addBackAndConfirm(14, goBack, aaiConfirm)
    
class VVI(PacingMode): 
    def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 450
        self.window.title("Pacemaker | VVI Pacing Mode")
        self.patient=patient

        #set these to patient specific parameters        
        def vviConfirm(): 
            updatePatient()
            if(self.patient.numsValid("VVI")):
                self.patient.saveToDB()
        
        def goBack(): 
            self.goBack("vviRadio")

        def updatePatient():
            self.patient.pacingMode="VVI"
            self.patient.lrl=self.lrlEntry.get()
            self.patient.url=self.urlEntry.get()
            self.patient.vpw=self.vpwEntry.get()
            self.patient.vamp=self.vampEntry.get()
            self.patient.vsens=self.vsensEntry.get()
            #self.patient.vrp=self.vrpEntry.get()
            self.patient.hystBool=self.hystBool
            self.patient.hrl=self.hystEntry.get()
            self.patient.rs=self.rsEntry.get()
        
        #VVI Frame
        self.initFrame()
        
        #Creating the elements for the VVI Frame
        self.addTitleAndInstructions("VVI")
        self.addLrl(5)
        self.addUrl(6)
        self.addVpw(7)
        self.addVamp(8)
        self.addVsens(9)
        self.addHyst(10)
        self.addRs(11)
        self.addBackAndConfirm(12, goBack, vviConfirm)
                
    
def launchAOO(window, patient): 
    AOO(window, patient)
    
def launchVOO(window, patient): 
    VOO(window, patient)

def launchAAI(window, patient): 
    AAI(window, patient)

def launchVVI(window, patient): 
    VVI(window, patient)
'''
def backToSelect(window):
    modeSelection.ModeSelect(window)
'''    
    