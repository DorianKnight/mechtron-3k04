from tkinter import *
from PIL import ImageTk, Image
from connectionDisplay import displayConnection, displayNewDevice
from EgramsPlot import EgramsPlotting
import modeSelection
import pacingModes
import matplotlib.pyplot as plt

background = 'white'

# allow user to choose between the different pacing modes and then bring them to corresponding page
class EgramsDisplay: 
    def __init__(self, window, patient, token, Serobj): 
        self.window = window
        self.window.geometry('500x600')
        self.width = 350
        self.height = 250
        self.window.minsize(self.width+30, self.height+50)
        self.window.iconbitmap("images\logo.ico")
        self.window.title("Pacemaker | EgramsDisplaySelect")
        self.patient=patient
        self.token = token #This allows me to know where you've come from so we can send you back when you want to leave
        self.EgramsPlotObject = EgramsPlotting(100,self.patient,Serobj) #Initializes the serial communication object

        # display whether the DCM is connected to the pacemaker
        displayConnection(self.window)
        # display whether the DCM is connected to a new pacemaker
        displayNewDevice(self.window)
        
        self.egrams_frame = Frame(
            self.window,
            bg = background,
            width = self.width,
            height = self.height
        )
        self.egrams_frame.place(anchor="c", relx=0.5, rely=0.5)
        self.egrams_frame.grid_propagate(False)

        # set width of grid
        self.egrams_frame.columnconfigure(0,weight=1)
        self.egrams_frame.columnconfigure(1,weight=1)

        # ======= Egrams Text ======= #
        self.header_text = "Egrams Display Select"
        self.header = Label(self.egrams_frame, text = self.header_text, font=('Arial',18,'bold'),bg = background, fg = 'black')
        self.description_text = "Select the chamber you want to view"
        self.description = Label(self.egrams_frame,text = self.description_text, font=('Arial',12),bg = background, fg = 'black')
        

        # ======= Egrams Select ======= #
        self.atrialDisplay = IntVar()
        self.ventricularDisplay = IntVar()
        self.checkBoxAtria = Checkbutton(self.egrams_frame, text='Atria',variable=self.atrialDisplay, onvalue=1, offvalue=0)
        self.checkBoxVentricle = Checkbutton(self.egrams_frame, text='Ventricle',variable=self.ventricularDisplay, onvalue=1, offvalue=0)

        # ======= Display Egrams Button and Back Button ======= #
        self.DisplayEgramsButton = Button(self.egrams_frame, text = "Show Egram", bg=background, command = self.displayEgrams)
        self.back_button = Button(self.egrams_frame, text = "Back", bg = background, command = self.goBack)

        #Formatting entries
        self.header.grid(row=0,column=0,columnspan=2,pady=5,sticky='N')
        self.description.grid(row=1,column=0,columnspan=2,pady=5,sticky='NS')
        self.checkBoxAtria.grid(row=2,column=0,columnspan=1,pady=25,sticky='NS')
        self.checkBoxVentricle.grid(row=2,column=1,columnspan=1,pady=25,sticky='NS')
        self.DisplayEgramsButton.grid(row=3,column=1,columnspan=1,pady=15,sticky='NS')
        self.back_button.grid(row=3,column=0,columnspan=1,pady=15,sticky='NS')
        
    def displayEgrams(self):
        #This method will create the push button that will call for the EgramsPlot.py file to display the egrams data
        
        #Close any windows that are already open
        plt.close('all')
         
        if (self.atrialDisplay.get() == 0 and self.ventricularDisplay.get() == 0):
            #display error message saying that at least one check box needs to be clicked
            pass
        else:
            
            if (self.atrialDisplay.get() == 1 and self.ventricularDisplay.get() == 0):
                #Only plot the atria and not the ventricular egram
                self.EgramsPlotObject.DisplayEgramsAtria()

            elif (self.atrialDisplay.get() == 0 and self.ventricularDisplay.get() == 1):
                #Only plot the ventricular and not the atrial egram
                self.EgramsPlotObject.DisplayEgramsVentricle()

            else:
                #Plot both the ventricular and atrial egrams data
                self.EgramsPlotObject.DisplayEgramsDualChamber()


    def goBack(self):
            #Go back to your previous window
            plt.close('all')
            self.egrams_frame.destroy()
            #If your previous window was the specific pacemaker mode window
            if(self.token == 'pacingModes'):
                #Find out which pacing mode you came from
                if(self.patient.pacingMode == 'AOO'):
                    pacingModes.launchAOO(self.window,self.patient, self.EgramsPlotObject)
                elif(self.patient.pacingMode == 'AOOR'):
                    pacingModes.launchAOOR(self.window,self.patient, self.EgramsPlotObject)
                elif(self.patient.pacingMode == 'AAI'):
                    pacingModes.launchAAI(self.window,self.patient, self.EgramsPlotObject)
                elif(self.patient.pacingMode == 'AAIR'):
                    pacingModes.launchAAIR(self.window,self.patient, self.EgramsPlotObject)
                elif(self.patient.pacingMode == 'VOO'):
                    pacingModes.launchVOO(self.window,self.patient, self.EgramsPlotObject)
                elif(self.patient.pacingMode == 'VOOR'):
                    pacingModes.launchVOOR(self.window,self.patient, self.EgramsPlotObject)
                elif(self.patient.pacingMode == 'VVI'):
                    pacingModes.launchVVI(self.window,self.patient, self.EgramsPlotObject)
                elif(self.patient.pacingMode == 'VVIR'):
                    pacingModes.launchVVIR(self.window,self.patient, self.EgramsPlotObject)
                elif(self.patient.pacingMode == 'DDD'):
                    pacingModes.launchDDD(self.window,self.patient, self.EgramsPlotObject)
                elif(self.patient.pacingMode == 'DDDR'):
                    pacingModes.launchDDDR(self.window,self.patient, self.EgramsPlotObject)
                else:
                    #Send them back to the mode select page
                    print("You don't have a pacing mode enabled")
                    #Flag an error for communication 
                    modeSelection.launchModeSelect(self.patient.username, self.window, self.EgramsPlotObject)

            #If your previous window was the select mode window or something that I can't forsee at the moment
            else:
                modeSelection.launchModeSelect(self.patient.username, self.window, self.EgramsPlotObject)
        

'''
    def launchEgrams(self):
        EgramsDisplay(self.window, self.patient)
        '''

