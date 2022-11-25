from tkinter import *
from PIL import ImageTk, Image
from modules.IdleLibTooltip import ToolTip
import modeSelection
import Patient as P

background = 'white'
class PacingMode:
    def __init__(self, window):
        self.window = window
        self.window.geometry('500x600')
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
        self.instructionLabel3 = Label(self.frame, text  = "If you have not set any values yet, they will be set to the nominal values.", bg = background, padx = 20)

        self.titleLabel.grid(row = 0, column = 0, columnspan = 2)
        self.instructionLabel.grid(row = 1, column = 0, columnspan = 2)
        self.instructionLabel2.grid(row = 2, column = 0, columnspan = 2)
        self.instructionLabel3.grid(row = 3, column = 0, columnspan = 2)

        # add blank row before back and confirm buttons
        self.frame.grid_rowconfigure(4, minsize = 20)

    def addLrl(self, r):
        self.lrlLabel = Label(self.frame, text = "Lower Rate Limit (ppm):", bg = background, padx = 20)
        self.lrlEntry = Entry(self.frame, bg = background)
        self.lrlLabel.grid(row = r, column = 0, sticky = W)
        self.lrlEntry.grid(row = r, column = 1)
        self.lrlEntry.insert(0,self.patient.lrl)

    def addUrl(self, r):
        self.urlLabel = Label(self.frame, text = "Upper Rate Limit (ppm):", bg = background, padx = 20)
        self.urlEntry = Entry(self.frame, bg = background)
        self.urlLabel.grid(row = r, column = 0, sticky = W)
        self.urlEntry.grid(row = r, column = 1)
        self.urlEntry.insert(0,self.patient.url)

    def addApw(self, r):
        self.apwLabel = Label(self.frame, text = "Atrial Pulse Width (ms):", bg = background, padx = 20)
        self.apwEntry = Entry(self.frame, bg = background)
        self.apwLabel.grid(row = r, column = 0, sticky = W)
        self.apwEntry.grid(row = r, column = 1)
        self.apwEntry.insert(0,self.patient.apw)

    def addAamp(self, r):
        self.aampLabel = Label(self.frame, text = "Atrial Amplitude (V): ⓘ", bg = background, padx = 20)
        tip = ToolTip(self.aampLabel, "Set value to 0 to turn off A Pulse Amplitude Regulated")
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
        self.vpwLabel = Label(self.frame, text = "Ventrical Pulse Width (ms):", bg = background, padx = 20)
        self.vpwEntry = Entry(self.frame, bg = background)
        self.vpwLabel.grid(row = r, column = 0, sticky = W)
        self.vpwEntry.grid(row = r, column = 1)
        self.vpwEntry.insert(0,self.patient.vpw)

    def addVamp(self, r):
        self.vampLabel = Label(self.frame, text = "Ventrical Amplitude (V): ⓘ", bg = background, padx = 20)
        tip = ToolTip(self.vampLabel, "Set value to 0 to turn off V Pulse Amplitude Regulated")
        self.vampEntry = Entry(self.frame, bg=background)
        self.vampLabel.grid(row = r, column = 0, sticky = W)
        self.vampEntry.grid(row = r, column = 1)
        self.vampEntry.insert(0,self.patient.vamp)

    def addAsens(self, r):
        self.asensLabel = Label(self.frame, text = "Atrial Sensitivity (mV):", bg = background, padx = 20)
        self.asensEntry = Entry(self.frame, bg=background)
        self.asensLabel.grid(row = r, column = 0, sticky = W)
        self.asensEntry.grid(row = r, column = 1)
        self.asensEntry.insert(0,self.patient.asens)

    def addArp(self, r):
        self.arpLabel = Label(self.frame, text = "Atrial Refractory Period (ms):", bg = background, padx = 20)
        self.arpEntry = Entry(self.frame, bg=background)
        self.arpLabel.grid(row = r, column = 0, sticky = W)
        self.arpEntry.grid(row = r, column = 1)
        self.arpEntry.insert(0,self.patient.arp)

    def addVrp(self, r):
        self.vrpLabel = Label(self.frame, text = "Ventricular Refractory Period (ms):", bg = background, padx = 20)
        self.vrpEntry = Entry(self.frame, bg=background)
        self.vrpLabel.grid(row = r, column = 0, sticky = W)
        self.vrpEntry.grid(row = r, column = 1)
        self.vrpEntry.insert(0,self.patient.vrp)

    def addPvarp(self, r):
        self.pvarpLabel = Label(self.frame, text = "PVARP (ms):", bg = background, padx = 20)
        self.pvarpEntry = Entry(self.frame, bg=background)
        self.pvarpLabel.grid(row = r, column = 0, sticky = W)
        self.pvarpEntry.grid(row = r, column = 1)
        self.pvarpEntry.insert(0,self.patient.pvarp)        
    
    def addVsens(self, r):
        self.vsensLabel = Label(self.frame, text = "Ventricular Sensitivity (mV):", bg = background, padx = 20)
        self.vsensEntry = Entry(self.frame, bg=background)
        self.vsensLabel.grid(row = r, column = 0, sticky = W)
        self.vsensEntry.grid(row = r, column = 1)
        self.vsensEntry.insert(0,self.patient.vsens)

    def addActThr(self, r): #should we make this a dropdown???
        self.actThrLabel = Label(self.frame, text = "Activity Threshold:", bg = background, padx = 20)
        self.actThrEntry = Entry(self.frame, bg=background)
        self.actThrLabel.grid(row = r, column = 0, sticky = W)
        self.actThrEntry.grid(row = r, column = 1)
        self.actThrEntry.insert(0,self.patient.actThr)

    def addReactTime(self, r):
        self.reactTimeLabel = Label(self.frame, text = "Reaction Time (s):", bg = background, padx = 20)
        self.reactTimeEntry = Entry(self.frame, bg=background)
        self.reactTimeLabel.grid(row = r, column = 0, sticky = W)
        self.reactTimeEntry.grid(row = r, column = 1)
        self.reactTimeEntry.insert(0,self.patient.reactTime)

    def addRespFactor(self, r):
        self.respFactorLabel = Label(self.frame, text = "Response Factor:", bg = background, padx = 20)
        self.respFactorEntry = Entry(self.frame, bg=background)
        self.respFactorLabel.grid(row = r, column = 0, sticky = W)
        self.respFactorEntry.grid(row = r, column = 1)
        self.respFactorEntry.insert(0,self.patient.respFactor)

    def addRecoveryTime(self, r):
        self.recoveryTimeLabel = Label(self.frame, text = "Recovery Time (min):", bg = background, padx = 20)
        self.recoveryTimeEntry = Entry(self.frame, bg=background)
        self.recoveryTimeLabel.grid(row = r, column = 0, sticky = W)
        self.recoveryTimeEntry.grid(row = r, column = 1)
        self.recoveryTimeEntry.insert(0,self.patient.recoveryTime)

    def addMaxSensRate(self, r):
        self.maxSensRateLabel = Label(self.frame, text = "Max Sensor Rate (ppm):", bg = background, padx = 20)
        self.maxSensRateEntry = Entry(self.frame, bg=background)
        self.maxSensRateLabel.grid(row = r, column = 0, sticky = W)
        self.maxSensRateEntry.grid(row = r, column = 1)
        self.maxSensRateEntry.insert(0,self.patient.maxSensRate)

    def addFixedAVdelay(self, r):
        self.fixedAVdelayLabel = Label(self.frame, text = "Fixed AV Delay (ms):", bg = background, padx = 20)
        self.fixedAVdelayEntry = Entry(self.frame, bg=background)
        self.fixedAVdelayLabel.grid(row = r, column = 0, sticky = W)
        self.fixedAVdelayEntry.grid(row = r, column = 1)
        self.fixedAVdelayEntry.insert(0,self.patient.fixedAVdelay)


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
            else:
                self.patient.copyFromDB()
        
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
            else:
                self.patient.copyFromDB()
        
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
            else:
                self.patient.copyFromDB()
        
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
            else:
                self.patient.copyFromDB()
        
        def goBack(): 
            self.goBack("vviRadio")

        def updatePatient():
            self.patient.pacingMode="VVI"
            self.patient.lrl=self.lrlEntry.get()
            self.patient.url=self.urlEntry.get()
            self.patient.vpw=self.vpwEntry.get()
            self.patient.vamp=self.vampEntry.get()
            self.patient.vsens=self.vsensEntry.get()
            self.patient.vrp=self.vrpEntry.get()
            
        
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
        self.addBackAndConfirm(13, goBack, vviConfirm)
                
class AOOR(PacingMode): 
    def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 450
        self.window.title("Pacemaker | AOOR Pacing Mode")
        self.patient=patient
        
        #Methods
        def aoorConfirm(): 
            updatePatient()
            if(self.patient.numsValid("AOOR")):
                self.patient.saveToDB()
            else:
                self.patient.copyFromDB()
        
        def goBack(): 
            self.goBack("aoorRadio")

        def updatePatient():
            self.patient.pacingMode="AOOR"
            self.patient.lrl=self.lrlEntry.get()
            self.patient.url=self.urlEntry.get()
            self.patient.apw=self.apwEntry.get()
            self.patient.aamp=self.aampEntry.get()
            self.patient.actThr=self.actThrEntry.get()
            self.patient.reactTime=self.reactTimeEntry.get()
            self.patient.respFactor=self.respFactorEntry.get()
            self.patient.recoveryTime=self.recoveryTimeEntry.get()
            self.patient.maxSensRate=self.maxSensRateEntry.get()

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
        self.addBackAndConfirm(16, goBack, aoorConfirm)
        
class VOOR(PacingMode): 
    def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 450
        self.window.title("Pacemaker | VOOR Pacing Mode")
        self.patient=patient

        #Methods
        def voorConfirm(): 
            updatePatient()
            if(self.patient.numsValid("VOOR")):
                self.patient.saveToDB()
            else:
                self.patient.copyFromDB()
        
        def goBack(): 
            self.goBack("voorRadio")

        def updatePatient():
            self.patient.pacingMode="VOOR"
            self.patient.lrl=self.lrlEntry.get()
            self.patient.url=self.urlEntry.get()
            self.patient.vpw=self.vpwEntry.get()
            self.patient.vamp=self.vampEntry.get()
            self.patient.actThr=self.actThrEntry.get()
            self.patient.reactTime=self.reactTimeEntry.get()
            self.patient.respFactor=self.respFactorEntry.get()
            self.patient.recoveryTime=self.recoveryTimeEntry.get()
            self.patient.maxSensRate=self.maxSensRateEntry.get()
        
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
        self.addBackAndConfirm(16, goBack, voorConfirm)
        
class AAIR(PacingMode): 
     def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 550
        self.window.title("Pacemaker | AAIR Pacing Mode")
        self.patient=patient

        #Methods 
        def aairConfirm(): 
            updatePatient()
            if(self.patient.numsValid("AAIR")):
                self.patient.saveToDB()
            else:
                self.patient.copyFromDB()
        
        def goBack(): 
            self.goBack("aairRadio")

        def updatePatient():
            self.patient.pacingMode="AAIR"
            self.patient.lrl=self.lrlEntry.get()
            self.patient.url=self.urlEntry.get()
            self.patient.apw=self.apwEntry.get()
            self.patient.aamp=self.aampEntry.get()
            self.patient.asens=self.asensEntry.get()
            self.patient.arp=self.arpEntry.get()
            self.patient.pvarp=self.pvarpEntry.get()
            self.patient.actThr=self.actThrEntry.get()
            self.patient.reactTime=self.reactTimeEntry.get()
            self.patient.respFactor=self.respFactorEntry.get()
            self.patient.recoveryTime=self.recoveryTimeEntry.get()
            self.patient.maxSensRate=self.maxSensRateEntry.get()
        
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
        self.addPvarp(11)
        self.addActThr(12)
        self.addReactTime(13)
        self.addRespFactor(14)
        self.addRecoveryTime(15)
        self.addMaxSensRate(16)
        self.addBackAndConfirm(19, goBack, aairConfirm)
        
        
class VVIR(PacingMode): 
     def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 550
        self.window.title("Pacemaker | VVIR Pacing Mode")
        self.patient=patient

        #Methods 
        def vvirConfirm(): 
            updatePatient()
            if(self.patient.numsValid("VVIR")):
                self.patient.saveToDB()
            else:
                self.patient.copyFromDB()
        
        def goBack(): 
            self.goBack("vvirRadio")

        def updatePatient():
            self.patient.pacingMode="VVIR"
            self.patient.lrl=self.lrlEntry.get()
            self.patient.url=self.urlEntry.get()
            self.patient.vpw=self.vpwEntry.get()
            self.patient.vamp=self.vampEntry.get()
            self.patient.vsens=self.vsensEntry.get()
            self.patient.vrp=self.vrpEntry.get()
            self.patient.actThr=self.actThrEntry.get()
            self.patient.reactTime=self.reactTimeEntry.get()
            self.patient.respFactor=self.respFactorEntry.get()
            self.patient.recoveryTime=self.recoveryTimeEntry.get()
            self.patient.maxSensRate=self.maxSensRateEntry.get()
        
        #AAIR Frame
        self.initFrame()
        
        #Creating the elements for the AAIR Frame
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
        self.addBackAndConfirm(18, goBack, vvirConfirm)
    
class DDD(PacingMode): 
     def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 550
        self.window.title("Pacemaker | DDD Pacing Mode")
        self.patient=patient
        
        #Methods 
        def dddConfirm(): 
            updatePatient()
            if(self.patient.numsValid("DDD")):
                self.patient.saveToDB()
            else:
                self.patient.copyFromDB()
        
        def goBack(): 
            self.goBack("dddRadio")

        def updatePatient():
            self.patient.pacingMode="DDD"
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
        self.addBackAndConfirm(19, goBack, dddConfirm)

        
class DDDR(PacingMode): 
     def __init__(self, window, patient):
        super().__init__(window)
        self.width = 450
        self.height = 675
        self.window.geometry("500x720")
        self.window.title("Pacemaker | DDDDR Pacing Mode")
        self.patient=patient

        #Methods 
        def dddrConfirm(): 
            updatePatient()
            if(self.patient.numsValid("DDDR")):
                self.patient.saveToDB()
            else:
                self.patient.copyFromDB()
        
        def goBack(): 
            self.goBack("dddrRadio")

        def updatePatient():
            self.patient.pacingMode="DDDR"
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
            self.patient.actThr=self.actThrEntry.get()
            self.patient.reactTime=self.reactTimeEntry.get()
            self.patient.respFactor=self.respFactorEntry.get()
            self.patient.recoveryTime=self.recoveryTimeEntry.get()
            self.patient.maxSensRate=self.maxSensRateEntry.get()
            self.patient.fixedAVdelay=self.fixedAVdelayEntry.get()
        
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
        self.addBackAndConfirm(24, goBack, dddrConfirm)

def launchAOO(window, patient): 
    AOO(window, patient)
    
def launchVOO(window, patient): 
    VOO(window, patient)

def launchAAI(window, patient): 
    AAI(window, patient)

def launchVVI(window, patient): 
    VVI(window, patient)
    
def launchAOOR(window, patient): 
    AOOR(window, patient)
    
def launchVOOR(window, patient): 
    VOOR(window, patient)

def launchAAIR(window, patient): 
    AAIR(window, patient)
    
def launchVVIR(window, patient): 
    VVIR(window, patient)
    
def launchDDD(window, patient): 
    DDD(window, patient)
    
def launchDDDR(window, patient): 
    DDDR(window, patient)
'''
def backToSelect(window):
    modeSelection.ModeSelect(window)
'''    
    