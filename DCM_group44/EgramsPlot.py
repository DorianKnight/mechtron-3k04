#Author: Group 44
#Date: Saturday November 26th 2022
#Purpose: Display egrams data from the serial communications rx line

from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from SerialCommunications import SerialObject

class EgramsPlotting:
    def __init__(self,refreshRate,patient, Serobj):
        #refreshRate is how often you want to call echo (eg every 1 ms, 5 ms - it's your choice)
        self.refreshRate = refreshRate
        #Initializes the serial communication object to receive egrams data
        self.pacemakerSerial = Serobj
        self.patient = patient
    
    def __del__(self):
        pass

    def DisplayEgramsAtria(self):
        #Displays internal heart electrical activity of the atrium
        
        #Allows the animate function to access the time and voltage values
        self.x = 0
        self.y = 0
        
        #Setting up the figure and the deque data structure used to facilitate the moving window
        fig, self.ax = plt.subplots()
        self.data = deque([(0,0)],maxlen=int(10000/self.refreshRate)) #Records the last 10,000 ms (10 sec) of activity
        self.line = plt.plot((0),(0),c='black')[0]
        plotAnimation = animation.FuncAnimation(fig, self.AnimateAtrialEgram,interval = self.refreshRate)
        
        #plotAnimation.save()
        plt.show()

    def DisplayEgramsVentricle(self):
        #Displays internal heart electrical activity of the ventricle

        #Allows the animate function to access the time and voltage values
        self.x = 0
        self.y = 0
        
        #Setting up the figure and the deque data structure used to facilitate the moving window
        fig, self.ax = plt.subplots()
        self.data = deque([(0,0)],maxlen=int(10000/self.refreshRate)) #Records the last 10,000 ms (10 sec) of activity
        self.line = plt.plot((0),(0),c='black')[0]
        plotAnimation = animation.FuncAnimation(fig, self.AnimateVentricularEgrams,interval = self.refreshRate)
        
        #plotAnimation.save()
        plt.show()

    def DisplayEgramsDualChamber(self):
        #Displays internal heart electrical activity of both chambers
        #Allows the animate function to access the time and voltage values
        self.x = 0
        self.y1 = 0 #Activity of atria
        self.y2 = 0 #Activity of ventricle
        
        #Setting up the figure and the deque data structure used to facilitate the moving window
        fig, self.ax = plt.subplots(2)
        self.dataAtria = deque([(0,0)],maxlen=int(10000/self.refreshRate)) #Records the last 10,000 ms (10 sec) of activity
        self.dataVentricle = deque([(0,0)],maxlen=int(10000/self.refreshRate))
        
        #Set current editable plot as the top one
        plt.subplot(2,1,1) 
        self.lineAtria = plt.plot((0),(0),c='black')[0]
        #Set current editable plot as the bottom one
        plt.subplot(2,1,2)
        self.lineVentricle = plt.plot((0),(0),c='black')[0]
        plotAnimation = animation.FuncAnimation(fig, self.AnimateDualChamberEgram,interval = self.refreshRate)
        
        #plotAnimation.save()
        plt.show()
    
    def FormatData(self, data):
        #Iterate through the deque data and isolate all of the x-coords into one tuple and all of the y-coords into another tuple
        x = []
        y = []  #Initialize empty lists
        #These x and y are purposely different from self.x and self.y
        for i in range(len(data)):
            x.append(data[i][0])
            y.append(data[i][1])
        print(x)
        print(y)
        return x,y

    def AnimateAtrialEgram(self,i):
        #Get Atrial Egrams data
        egramsDictionary = self.pacemakerSerial.ReceiveEgramsData(self.patient)
        self.x += self.refreshRate
        self.y = egramsDictionary['egramsAtrial']
        self.data.append((self.x,self.y))
        self.line.set_data(self.FormatData(self.data))
        
        #Redefine the axis bounds
        self.ax.relim()
        #Autoscale to the new bounds
        self.ax.autoscale_view()


    def AnimateVentricularEgrams(self,i):
        #Get ventricular egrams data
        egramsDictionary = self.pacemakerSerial.ReceiveEgramsData(self.patient)
        self.x += self.refreshRate
        self.y = egramsDictionary['egramsVentricular']
        self.data.append((self.x,self.y))
        self.line.set_data(self.FormatData(self.data))
        
        #Redefine the axis bounds
        self.ax.relim()
        #Autoscale to the new bounds
        self.ax.autoscale_view()
    
    def AnimateDualChamberEgram(self,i):
        #Get both atrial and ventricular egrams data
        egramsDictionary = self.pacemakerSerial.ReceiveEgramsData(self.patient)
        self.x += self.refreshRate
        self.y1 = egramsDictionary['egramsAtrial']
        self.y2 = egramsDictionary['egramsVentricular']
        self.dataAtria.append((self.x,self.y1))
        self.dataVentricle.append((self.x,self.y2))

        plt.subplot(2,1,1) 
        self.lineAtria.set_data(self.FormatData(self.dataAtria))
        plt.subplot(2,1,2)
        self.lineVentricle.set_data(self.FormatData(self.dataVentricle))

        #Redefine the axis bounds on the first plot
        self.ax[0].relim()
        #Autoscale to the new bounds on the first plot
        self.ax[0].autoscale_view()

        #Redefine the axis bounds on the second plot
        self.ax[1].relim()
        #Autoscale to the new bounds on the second plot
        self.ax[1].autoscale_view()