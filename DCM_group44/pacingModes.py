from tkinter import *
from PIL import ImageTk, Image
from modules.IdleLibTooltip import ToolTip
import modeSelection
import Patient as P
import main
from EgramsWindow import EgramsDisplay

import SerialCommunications as Serial
from tkinter import messagebox
#import serial_test as S


background = 'white'

# creates pages to change pacing mode-specific parameters  
class PacingMode:
    def __init__(self, window, patient, Serobj):
        self.window = window
        self.window.geometry('500x600')
        self.window.iconbitmap("images\logo.ico")
        self.patient = patient
        self.Serobj = Serobj

    def initFrame(self):
        self.frame = Frame(self.window, bg = background, width = self.width, height = self.height)
        self.frame.place(anchor="c", relx=0.5, rely=0.5)
        self.frame.grid_propagate(False)
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1,weight=2)
        self.frame.columnconfigure(2,weight=1)
        
    def goBack(self, radioBtn): 
            self.frame.destroy()
            MS=modeSelection.ModeSelect(self.window,self.Serobj)
            getattr(MS, radioBtn).select()
            MS.patient=self.patient
    
    def confirmation(self, mode): 
        if(self.patient.numsValid(mode)):
                self.patient.saveToDB()
                self.enableApplyBtn()
        else:
            self.patient.copyFromDB()
            
    def applyChanges(self): 
        self.Serobj.SendData(self.patient)
        print("lrl",self.patient.lrl)
        

    def updatePatient(self, mode):
        self.patient.pacingMode = mode
        match mode: 
            case "AOO": 
                self.patient.lrl=self.lrlEntry.get()
                self.patient.url=self.urlEntry.get()
                self.patient.apw=self.apwEntry.get()
                self.patient.aamp=self.aampEntry.get()
            case "VOO": 
                self.patient.lrl=self.lrlEntry.get()
                self.patient.url=self.urlEntry.get()
                self.patient.vpw=self.vpwEntry.get()
                self.patient.vamp=self.vampEntry.get()
            case "AAI": 
                self.patient.lrl=self.lrlEntry.get()
                self.patient.url=self.urlEntry.get()
                self.patient.apw=self.apwEntry.get()
                self.patient.aamp=self.aampEntry.get()
                self.patient.asens=self.asensEntry.get()
                self.patient.arp=self.arpEntry.get()
            case "VVI": 
                self.patient.lrl=self.lrlEntry.get()
                self.patient.url=self.urlEntry.get()
                self.patient.vpw=self.vpwEntry.get()
                self.patient.vamp=self.vampEntry.get()
                self.patient.vsens=self.vsensEntry.get()
                self.patient.vrp=self.vrpEntry.get()
            case "AOOR": 
                self.patient.lrl=self.lrlEntry.get()
                self.patient.url=self.urlEntry.get()
                self.patient.apw=self.apwEntry.get()
                self.patient.aamp=self.aampEntry.get()
                self.patient.actThr=self.actThrSelected.get()
                self.patient.reactTime=self.reactTimeEntry.get()
                self.patient.respFactor=self.respFactorEntry.get()
                self.patient.recoveryTime=self.recoveryTimeEntry.get()
                self.patient.maxSensRate=self.maxSensRateEntry.get()
            case "VOOR":
                self.patient.lrl=self.lrlEntry.get()
                self.patient.url=self.urlEntry.get()
                self.patient.vpw=self.vpwEntry.get()
                self.patient.vamp=self.vampEntry.get()
                self.patient.actThr=self.actThrSelected.get()
                self.patient.reactTime=self.reactTimeEntry.get()
                self.patient.respFactor=self.respFactorEntry.get()
                self.patient.recoveryTime=self.recoveryTimeEntry.get()
                self.patient.maxSensRate=self.maxSensRateEntry.get()
            case "AAIR":
                self.patient.lrl=self.lrlEntry.get()
                self.patient.url=self.urlEntry.get()
                self.patient.apw=self.apwEntry.get()
                self.patient.aamp=self.aampEntry.get()
                self.patient.asens=self.asensEntry.get()
                self.patient.arp=self.arpEntry.get()
                self.patient.actThr=self.actThrSelected.get()
                self.patient.reactTime=self.reactTimeEntry.get()
                self.patient.respFactor=self.respFactorEntry.get()
                self.patient.recoveryTime=self.recoveryTimeEntry.get()
                self.patient.maxSensRate=self.maxSensRateEntry.get()
            case "VVIR":
                self.patient.lrl=self.lrlEntry.get()
                self.patient.url=self.urlEntry.get()
                self.patient.vpw=self.vpwEntry.get()
                self.patient.vamp=self.vampEntry.get()
                self.patient.vsens=self.vsensEntry.get()
                self.patient.vrp=self.vrpEntry.get()
                self.patient.actThr=self.actThrSelected.get()
                self.patient.reactTime=self.reactTimeEntry.get()
                self.patient.respFactor=self.respFactorEntry.get()
                self.patient.recoveryTime=self.recoveryTimeEntry.get()
                self.patient.maxSensRate=self.maxSensRateEntry.get()
            case "DDD":
                self.patient.lrl=self.lrlEntry.get()
                self.patient.url=self.urlEntry.get()
                self.patient.apw=self.apwEntry.get()
                self.patient.aamp=self.aampEntry.get()
                self.patient.asens=self.asensEntry.get()
                self.patient.arp=self.arpEntry.get()
                self.patient.pvarp=self.pvarpEntry.get()
                self.patient.vpw=self.vpwEntry.get()
                self.patient.vamp=self.vampEntry.get()
                self.patient.vsens=self.vsensEntry.get()
                self.patient.vrp=self.vrpEntry.get()
                self.patient.fixedAVdelay=self.fixedAVdelayEntry.get()
            case "DDDR": 
                self.patient.lrl=self.lrlEntry.get()
                self.patient.url=self.urlEntry.get()
                self.patient.apw=self.apwEntry.get()
                self.patient.aamp=self.aampEntry.get()
                self.patient.asens=self.asensEntry.get()
                self.patient.arp=self.arpEntry.get()
                self.patient.pvarp=self.pvarpEntry.get()
                self.patient.vpw=self.vpwEntry.get()
                self.patient.vamp=self.vampEntry.get()
                self.patient.vsens=self.vsensEntry.get()
                self.patient.vrp=self.vrpEntry.get()
                self.patient.actThr=self.actThrSelected.get()
                self.patient.reactTime=self.reactTimeEntry.get()
                self.patient.respFactor=self.respFactorEntry.get()
                self.patient.recoveryTime=self.recoveryTimeEntry.get()
                self.patient.maxSensRate=self.maxSensRateEntry.get()
                self.patient.fixedAVdelay=self.fixedAVdelayEntry.get()

    def addTitleAndInstructions(self, mode):
        # title and instructions
        self.titleLabel = Label(self.frame, text = mode, font = ("Arial", 24), bg = background, padx = 20, pady = 10)
        self.instructionLabel = Label(self.frame, text = "Please enter the values for the following parameters.", bg = background, padx = 20)
        self.instructionLabel2 = Label(self.frame, text  = "These values will be checked to ensure that they are valid entries.", bg = background, padx = 20)
        self.instructionLabel3 = Label(self.frame, text  = "If you have not set any values yet, they will be set to the nominal values.", bg = background, padx = 20)

        self.titleLabel.grid(row = 0, column = 0, columnspan = 3)
        self.instructionLabel.grid(row = 1, column = 0, columnspan = 3)
        self.instructionLabel2.grid(row = 2, column = 0, columnspan = 3)
        self.instructionLabel3.grid(row = 3, column = 0, columnspan = 3)

        # add blank row before back and confirm buttons
        self.frame.grid_rowconfigure(4, minsize = 20)

    def entryChanged(self):
        # disable apply button
        try:
            if (self.apply['state'] == NORMAL):
                self.apply['state'] = DISABLED
        except Exception as ep:
            pass
        return True # needs to return true for it to work
        
    
    def enableApplyBtn(self):
        try:
            self.apply['state'] = NORMAL
        except Exception as ep:
            pass

    # ========= Functions to add entry boxes for each parameter. r represents row to place entry box on =========
    def addLrl(self, r):
        self.lrlLabel = Label(self.frame, text = "Lower Rate Limit (ppm):", bg = background, padx = 20)
        self.lrlEntry = Entry(self.frame, bg = background, validate="key", validatecommand=self.entryChanged)
        self.lrlLabel.grid(row = r, column = 0, sticky = W)
        self.lrlEntry.grid(row = r, column = 1, columnspan = 2)
        self.lrlEntry.insert(0,self.patient.lrl)
        print(self.patient.lrl)

    def addUrl(self, r):
        self.urlLabel = Label(self.frame, text = "Upper Rate Limit (ppm):", bg = background, padx = 20)
        self.urlEntry = Entry(self.frame, bg = background, validate="key", validatecommand=self.entryChanged)
        self.urlLabel.grid(row = r, column = 0, sticky = W)
        self.urlEntry.grid(row = r, column = 1, columnspan = 2)
        self.urlEntry.insert(0,self.patient.url)

    def addApw(self, r):
        self.apwLabel = Label(self.frame, text = "Atrial Pulse Width (ms):", bg = background, padx = 20)
        self.apwEntry = Entry(self.frame, bg = background, validate="key", validatecommand=self.entryChanged)
        self.apwLabel.grid(row = r, column = 0, sticky = W)
        self.apwEntry.grid(row = r, column = 1, columnspan = 2)
        self.apwEntry.insert(0,self.patient.apw)

    def addAamp(self, r):
        self.aampLabel = Label(self.frame, text = "Atrial Amplitude (V): ⓘ", bg = background, padx = 20)
        # add tooltip (hover over label and a pop-up with more details appears)
        tip = ToolTip(self.aampLabel, "Set value to 0 to turn off A Pulse Amplitude Regulated")
        self.aampEntry = Entry(self.frame, bg = background, validate="key", validatecommand=self.entryChanged)
        self.aampLabel.grid(row = r, column = 0, sticky = W)
        self.aampEntry.grid(row = r, column = 1, columnspan = 2)
        self.aampEntry.insert(0,self.patient.aamp)

    def addVpw(self, r):
        self.vpwLabel = Label(self.frame, text = "Ventrical Pulse Width (ms):", bg = background, padx = 20)
        self.vpwEntry = Entry(self.frame, bg = background, validate="key", validatecommand=self.entryChanged)
        self.vpwLabel.grid(row = r, column = 0, sticky = W)
        self.vpwEntry.grid(row = r, column = 1, columnspan = 2)
        self.vpwEntry.insert(0,self.patient.vpw)

    def addVamp(self, r):
        self.vampLabel = Label(self.frame, text = "Ventrical Amplitude (V): ⓘ", bg = background, padx = 20)
        tip = ToolTip(self.vampLabel, "Set value to 0 to turn off V Pulse Amplitude Regulated")
        self.vampEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.vampLabel.grid(row = r, column = 0, sticky = W)
        self.vampEntry.grid(row = r, column = 1, columnspan = 2)
        self.vampEntry.insert(0,self.patient.vamp)

    def addAsens(self, r):
        self.asensLabel = Label(self.frame, text = "Atrial Sensitivity (V):", bg = background, padx = 20)
        self.asensEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.asensLabel.grid(row = r, column = 0, sticky = W)
        self.asensEntry.grid(row = r, column = 1, columnspan = 2)
        self.asensEntry.insert(0,self.patient.asens)

    def addArp(self, r):
        self.arpLabel = Label(self.frame, text = "Atrial Refractory Period (ms):", bg = background, padx = 20)
        self.arpEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.arpLabel.grid(row = r, column = 0, sticky = W)
        self.arpEntry.grid(row = r, column = 1, columnspan = 2)
        self.arpEntry.insert(0,self.patient.arp)

    def addVrp(self, r):
        self.vrpLabel = Label(self.frame, text = "Ventricular Refractory Period (ms):", bg = background, padx = 20)
        self.vrpEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.vrpLabel.grid(row = r, column = 0, sticky = W)
        self.vrpEntry.grid(row = r, column = 1, columnspan = 2)
        self.vrpEntry.insert(0,self.patient.vrp)

    def addPvarp(self, r):
        self.pvarpLabel = Label(self.frame, text = "PVARP (ms):", bg = background, padx = 20)
        self.pvarpEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.pvarpLabel.grid(row = r, column = 0, sticky = W)
        self.pvarpEntry.grid(row = r, column = 1, columnspan = 2)
        self.pvarpEntry.insert(0,self.patient.pvarp)        
    
    def addVsens(self, r):
        self.vsensLabel = Label(self.frame, text = "Ventricular Sensitivity (V):", bg = background, padx = 20)
        self.vsensEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.vsensLabel.grid(row = r, column = 0, sticky = W)
        self.vsensEntry.grid(row = r, column = 1, columnspan = 2)
        self.vsensEntry.insert(0,self.patient.vsens)

    def addActThr(self, r): #should we make this a dropdown???
        self.actThrLabel = Label(self.frame, text = "Activity Threshold:", bg = background, padx = 20)
        # self.actThrEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.actThrLabel.grid(row = r, column = 0, sticky = W)
        # self.actThrEntry.grid(row = r, column = 1, columnspan = 2)
        #self.actThrEntry.insert(0,self.patient.actThr)

        # dropdown
        self.actThrOptions = [
            "V-Low",
            "Low",
            "Med-Low",
            "Med",
            "Med-High",
            "High",
            "V-High"
        ]
        self.actThrSelected = StringVar()

        # initial dropdown text
        self.actThrSelected.set(self.patient.actThr)

        # create dropdown menu
        self.actThrDrop = OptionMenu(self.frame, self.actThrSelected, *self.actThrOptions)
        self.actThrDrop.config(width=15)
        self.actThrDrop.grid(row = r, column = 1, columnspan = 2)

    def addReactTime(self, r):
        self.reactTimeLabel = Label(self.frame, text = "Reaction Time (s):", bg = background, padx = 20)
        self.reactTimeEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.reactTimeLabel.grid(row = r, column = 0, sticky = W)
        self.reactTimeEntry.grid(row = r, column = 1, columnspan = 2)
        self.reactTimeEntry.insert(0,self.patient.reactTime)

    def addRespFactor(self, r):
        self.respFactorLabel = Label(self.frame, text = "Response Factor:", bg = background, padx = 20)
        self.respFactorEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.respFactorLabel.grid(row = r, column = 0, sticky = W)
        self.respFactorEntry.grid(row = r, column = 1, columnspan = 2)
        self.respFactorEntry.insert(0,self.patient.respFactor)

    def addRecoveryTime(self, r):
        self.recoveryTimeLabel = Label(self.frame, text = "Recovery Time (min):", bg = background, padx = 20)
        self.recoveryTimeEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.recoveryTimeLabel.grid(row = r, column = 0, sticky = W)
        self.recoveryTimeEntry.grid(row = r, column = 1, columnspan = 2)
        self.recoveryTimeEntry.insert(0,self.patient.recoveryTime)

    def addMaxSensRate(self, r):
        self.maxSensRateLabel = Label(self.frame, text = "Max Sensor Rate (ppm):", bg = background, padx = 20)
        self.maxSensRateEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.maxSensRateLabel.grid(row = r, column = 0, sticky = W)
        self.maxSensRateEntry.grid(row = r, column = 1, columnspan = 2)
        self.maxSensRateEntry.insert(0,self.patient.maxSensRate)

    def addFixedAVdelay(self, r):
        self.fixedAVdelayLabel = Label(self.frame, text = "Fixed AV Delay (ms):", bg = background, padx = 20)
        self.fixedAVdelayEntry = Entry(self.frame, bg=background, validate="key", validatecommand=self.entryChanged)
        self.fixedAVdelayLabel.grid(row = r, column = 0, sticky = W)
        self.fixedAVdelayEntry.grid(row = r, column = 1, columnspan = 2)
        self.fixedAVdelayEntry.insert(0,self.patient.fixedAVdelay)

     # ========= Functions to add buttons. r represents row to place entry box on =========
    def addBackAndConfirm(self, r, cmdBack, cmdConfirm, cmdApply):
        # add blank row before back and confirm buttons
        self.frame.grid_rowconfigure(r, minsize = 20)

        self.back = Button(self.frame, text = "Back", width=5, command = cmdBack)
        self.back.grid(row = r+1, column = 0, sticky = S)
        
        self.save = Button(self.frame, text = "Save", width=5, command = cmdConfirm)
        self.save.grid(row = r+1, column = 1, sticky = SW)
        
        self.apply = Button(self.frame, text = "Apply", width=5, state = NORMAL, command = cmdApply)
        self.apply.grid(row = r+1, column = 2, sticky = S)

    # ========= Function to add display Egrams buttons =========
    def addDisplayEgrams(self,rowOfBox):
        self.egramsDisplay = Button(self.frame, text = "Display Egrams Plot", width=15, command= self.launchEgrams)
        self.egramsDisplay.grid(row = rowOfBox+1, column = 0, sticky=S, columnspan=3, pady=15)
    
    def launchEgrams(self):
        self.frame.destroy()
        EgramsDisplay(self.window, self.patient, 'pacingModes', self.Serobj)

class AOO(PacingMode): 
    def __init__(self, window, patient, Serobj):
        super().__init__(window, patient, Serobj)
        self.width = 450
        self.height = 350
        self.window.title("Pacemaker | AOO Pacing Mode")
        self.patient = patient

        #Methods
        def aooConfirm(): 
            self.updatePatient("AOO")
            self.confirmation("AOO")
            
        def aooApply(): 
            self.applyChanges()
        
        def goBack(): 
            self.goBack("aooRadio")

        '''def updatePatient():
            self.patient.pacingMode="AOO"
            self.patient.lrl=self.lrlEntry.get()
            self.patient.url=self.urlEntry.get()
            self.patient.apw=self.apwEntry.get()
            self.patient.aamp=self.aampEntry.get()
        '''
        
        #AOO Frame
        self.initFrame()
        
        #Elements on the page
        self.addTitleAndInstructions("AOO")
        self.addLrl(5)
        self.addUrl(6)
        self.addApw(7)
        self.addAamp(8)
        self.addBackAndConfirm(9, goBack, aooConfirm, aooApply)
        self.addDisplayEgrams(10)


class VOO(PacingMode): 
    def __init__(self, window, patient, Serobj):
        super().__init__(window, patient, Serobj)
        self.width = 450
        self.height = 350
        self.window.title("Pacemaker | VOO Pacing Mode")
        self.patient=patient
        
        #Methods
        def vooConfirm(): 
            self.updatePatient("VOO")
            self.confirmation("VOO")
        
        def vooApply(): 
            self.applyChanges()
        
        def goBack(): 
            self.goBack("vooRadio")

        '''def updatePatient():
            self.patient.pacingMode="VOO"
            self.patient.lrl=self.lrlEntry.get()
            self.patient.url=self.urlEntry.get()
            self.patient.vpw=self.vpwEntry.get()
            self.patient.vamp=self.vampEntry.get()
        '''
        #VOO Frame
        self.initFrame()
        
        #Elements on the page
        self.addTitleAndInstructions("VOO")
        self.addLrl(5)
        self.addUrl(6)
        self.addVpw(7)
        self.addVamp(8)
        self.addBackAndConfirm(9, goBack, vooConfirm, vooApply)

class AAI(PacingMode): 
    def __init__(self, window, patient, Serobj):
        super().__init__(window, patient, Serobj)
        self.width = 450
        self.height = 450
        self.window.title("Pacemaker | AAI Pacing Mode")
        self.patient=patient

        #set these to patient specific parameters
        
        #Methods 
        def aaiConfirm():
            self.updatePatient("AAI")
            self.confirmation("AAI")
        
        def aaiApply(): 
            self.applyChanges()
        
        def goBack(): 
            self.goBack("aaiRadio")

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
        self.addBackAndConfirm(13, goBack, aaiConfirm, aaiApply)
    
class VVI(PacingMode): 
    def __init__(self, window, patient, Serobj):
        super().__init__(window, patient, Serobj)
        self.width = 450
        self.height = 450
        self.window.title("Pacemaker | VVI Pacing Mode")
        self.patient=patient

        #set these to patient specific parameters        
        def vviConfirm(): 
            self.updatePatient("VVI")
            self.confirmation("VVI")
        
        def vviApply(): 
            self.applyChanges()
        
        def goBack(): 
            self.goBack("vviRadio")
        '''
        def updatePatient():
            self.patient.pacingMode="VVI"
        ''' 
            
        
        #VVI Frame
        self.initFrame()
        
        #Creating the elements for the VVI Frame
        self.addTitleAndInstructions("VVI")
        self.addLrl(5)
        self.addUrl(6)
        self.addVpw(7)
        self.addVamp(8)
        self.addVsens(9)
        self.addVrp(10)
        self.addBackAndConfirm(13, goBack, vviConfirm, vviApply)
                
class AOOR(PacingMode): 
    def __init__(self, window, patient, Serobj):
        super().__init__(window, patient, Serobj)
        self.width = 450
        self.height = 450
        self.window.title("Pacemaker | AOOR Pacing Mode")
        self.patient=patient
        
        #Methods
        def aoorConfirm(): 
            self.updatePatient("AOOR")
            self.confirmation("AOOR")
        
        def aoorApply(): 
            self.applyChanges()
        
        def goBack(): 
            self.goBack("aoorRadio")
            
        #AOOR Frame
        self.initFrame()
        
        #Creating the elements for the AOOR Frame
        self.addTitleAndInstructions("AOOR")
        self.addLrl(5)
        self.addUrl(6)
        self.addApw(7)
        self.addAamp(8)
        self.addActThr(9)
        self.addReactTime(10)
        self.addRespFactor(11)
        self.addRecoveryTime(12)
        self.addMaxSensRate(13)
        self.addBackAndConfirm(16, goBack, aoorConfirm, aoorApply)
        
class VOOR(PacingMode): 
    def __init__(self, window, patient, Serobj):
        super().__init__(window, patient, Serobj)
        self.width = 450
        self.height = 450
        self.window.title("Pacemaker | VOOR Pacing Mode")
        self.patient=patient

        #Methods
        def voorConfirm(): 
            self.updatePatient("VOOR")
            self.confirmation("VOOR")
        
        def voorApply():
            self.applyChanges()
        
        def goBack(): 
            self.goBack("voorRadio")
        
        #VOOR Frame
        self.initFrame()
        
        #Creating the elements for the VOOR Frame
        self.addTitleAndInstructions("VOOR")
        self.addLrl(5)
        self.addUrl(6)
        self.addVpw(7)
        self.addVamp(8)
        self.addActThr(9)
        self.addReactTime(10)
        self.addRespFactor(11)
        self.addRecoveryTime(12)
        self.addMaxSensRate(13)
        self.addBackAndConfirm(16, goBack, voorConfirm, voorApply)
        
class AAIR(PacingMode): 
     def __init__(self, window, patient, Serobj):
        super().__init__(window, patient, Serobj)
        self.width = 450
        self.height = 550
        self.window.title("Pacemaker | AAIR Pacing Mode")
        self.patient=patient

        #Methods 
        def aairConfirm():
            self.updatePatient("AAIR") 
            self.confirmation("AAIR")
        
        def aairApply(): 
            self.applyChanges()
        
        def goBack(): 
            self.goBack("aairRadio")
        
        #AAIR Frame
        self.initFrame()
        
        #Creating the elements for the AAIR Frame
        self.addTitleAndInstructions("AAIR")
        self.addLrl(5)
        self.addUrl(6)
        self.addApw(7)
        self.addAamp(8)
        self.addAsens(9)
        self.addArp(10)
        self.addActThr(11)
        self.addReactTime(12)
        self.addRespFactor(13)
        self.addRecoveryTime(14)
        self.addMaxSensRate(15)
        self.addBackAndConfirm(18, goBack, aairConfirm, aairApply)
        
        
class VVIR(PacingMode): 
     def __init__(self, window, patient, Serobj):
        super().__init__(window, patient, Serobj)
        self.width = 450
        self.height = 550
        self.window.title("Pacemaker | VVIR Pacing Mode")
        self.patient=patient

        #Methods 
        def vvirConfirm(): 
            self.updatePatient("VVIR")
            self.confirmation("VVIR")
        
        def vvirApply(): 
            self.appyChanges()
        
        def goBack(): 
            self.goBack("vvirRadio")
        
        #VVIR Frame
        self.initFrame()
        
        #Creating the elements for the VVIR Frame
        self.addTitleAndInstructions("VVIR")
        self.addLrl(5)
        self.addUrl(6)
        self.addVpw(7)
        self.addVamp(8)
        self.addVsens(9)
        self.addVrp(10)
        self.addActThr(11)
        self.addReactTime(12)
        self.addRespFactor(13)
        self.addRecoveryTime(14)
        self.addMaxSensRate(15)
        self.addBackAndConfirm(18, goBack, vvirConfirm, vvirApply)
    
class DDD(PacingMode): 
     def __init__(self, window, patient, Serobj):
        super().__init__(window, patient, Serobj)
        self.width = 450
        self.height = 500
        self.window.title("Pacemaker | DDD Pacing Mode")
        self.patient=patient
        
        #Methods 
        def dddConfirm(): 
            self.updatePatient("DDD")
            self.confirmation("DDD")
        
        def dddApply(): 
            self.applyChanges()
        
        def goBack(): 
            self.goBack("dddRadio")


        #DDD Frame
        self.initFrame()
        
        #Creating the elements for the DDD Frame
        self.addTitleAndInstructions("DDD")
        self.addLrl(5)
        self.addUrl(6)
        self.addApw(7)
        self.addAamp(8)
        self.addAsens(9)
        self.addArp(10)
        self.addPvarp(11)
        self.addVpw(12)
        self.addVamp(13)
        self.addVsens(14)
        self.addVrp(15)
        self.addFixedAVdelay(16)
        self.addBackAndConfirm(19, goBack, dddConfirm, dddApply)

        
class DDDR(PacingMode): 
     def __init__(self, window, patient, Serobj):
        super().__init__(window, patient, Serobj)
        self.width = 450
        self.height = 600
        self.window.geometry("500x720")
        self.window.title("Pacemaker | DDDDR Pacing Mode")
        self.patient=patient

        #Methods 
        def dddrConfirm(): 
            self.updatePatient("DDDR")
            self.confirmation("DDDR")
        
        def dddrApply(): 
            self.applyChanges()
        
        def goBack(): 
            self.goBack("dddrRadio")
        
        #DDDR Frame
        self.initFrame()
        
        #Creating the elements for the DDDR Frame
        self.addTitleAndInstructions("DDDR")
        self.addLrl(5)
        self.addUrl(6)
        self.addApw(7)
        self.addAamp(8)
        self.addAsens(9)
        self.addArp(10)
        self.addPvarp(11)
        self.addVpw(12)
        self.addVamp(13)
        self.addVsens(14)
        self.addVrp(15)
        self.addActThr(16)
        self.addReactTime(17)
        self.addRespFactor(18)
        self.addRecoveryTime(19)
        self.addMaxSensRate(20)
        self.addFixedAVdelay(21)
        self.addBackAndConfirm(24, goBack, dddrConfirm, dddrApply)

def launchAOO(window, patient, Serobj): 
    AOO(window, patient, Serobj)
    
def launchVOO(window, patient, Serobj): 
    VOO(window, patient, Serobj)

def launchAAI(window, patient, Serobj): 
    AAI(window, patient, Serobj)

def launchVVI(window, patient, Serobj): 
    VVI(window, patient, Serobj)
    
def launchAOOR(window, patient, Serobj): 
    AOOR(window, patient, Serobj)
    
def launchVOOR(window, patient, Serobj): 
    VOOR(window, patient, Serobj)

def launchAAIR(window, patient, Serobj): 
    AAIR(window, patient, Serobj)
    
def launchVVIR(window, patient, Serobj): 
    VVIR(window, patient, Serobj)
    
def launchDDD(window, patient, Serobj): 
    DDD(window, patient, Serobj)
    
def launchDDDR(window, patient, Serobj): 
    DDDR(window, patient, Serobj)

'''
def backToSelect(window):
    modeSelection.ModeSelect(window)
'''    
    