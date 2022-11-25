from tkinter import *

# ========= Connection =========
# display whether the DCM is connected to the pacemaker
def displayConnection(window):
    connectionChecker=False
    if(connectionChecker==False):
        connectionBanner=Label(window,text="Not connected - ", fg= 'red', font=("Helvetica",12), padx=10)
        connectionBanner.grid(row=0,column=0, sticky=W)
    else:
        connectionBanner=Label(window,text="Connected - ",fg="green", font=("Helvetica",12), padx=10)
        connectionBanner.grid(row=0,column=0, sticky=W)

# ========= New Device =========
# display whether the DCM is connected to a new pacemaker
def displayNewDevice(window):    
    newDeviceChecker=False
    if(newDeviceChecker==False):
        deviceBanner = Label(window,text="No new device",fg='black', font=("Helvetica", 12), padx=10)
        deviceBanner.grid(row=0,column=2, sticky=E)
    else:
        deviceBanner = Label(window,text="New device detected", fg="black", font=("Helvetica",12), padx=10)
        deviceBanner.grid(row=0,column=2, sticky=E)
        