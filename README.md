# MechTron 3K04 Group 44: Assignment 2

## Simulink
### Instructions
The Simulink file is located within the “simulink_group44” folder. To simulate the pacemaker download the file "Group44PACEMAKER.slx". 

#### FDRM Board:
To simulate the pacemaker download the file "Group44PACEMAKER.slx". If you wish to deploy the code to the FDRM board, you must first comment out the requirements table held within the Output pins subsystem

#### Operating Modes:
If you wish to switch the operating mode, navigate to the inputs subsystem and find the "mode" string constant box. Enter in "AOO" for Asynchronous pacing of the atria, "VOO" for asynchronous pacing of the ventricle, "AAI" for sensing in the atria and inhibiting paces if a natural heart beat was sensed, and "VVI" for sensing in the ventricle and inhibiting paces if a natural heart beat was sensed.

## DCM
### Requirements
* The latest version of Python (this version should have Tkinter and SQLite3 automatically installed)
* Pillow
  * Install with `pip install pillow`
 
### Instructions for Launching DCM
1. Clone the repository.
2. Open terminal and navigate to the DCM_group44 folder: `cd DCM_group44`
3. Launch the DCM by running main.py through the terminal: `python3 main.py`

### Documentation
For additional information about the structure of the DCM program and what each of the files do, view the PDF in DCM_group44 called **"documentation.pdf"**

For even further explanations, please refer to this video we created walking through our entire project: https://www.youtube.com/watch?v=dQw4w9WgXcQ

### Demo
Here are some of our favourite pages!
* Welcome Page
<img width="289" alt="image" src="https://user-images.githubusercontent.com/68765813/197439833-0de690bf-c172-43df-beab-b4cdebc84bdb.png">

* Login Page
<img width="291" alt="image" src="https://user-images.githubusercontent.com/68765813/197439864-6187fadf-43a7-46f7-917c-3079e4ba86ea.png">

* Registration Page
<img width="301" alt="image" src="https://user-images.githubusercontent.com/68765813/197439879-57ca4c62-4c92-464b-b57c-6a4f5be501a4.png">


* Pacing Mode Selection Page
<img width="295" alt="image" src="https://user-images.githubusercontent.com/68765813/197439896-626d501a-86f0-4db6-a0b1-0c6a08778977.png">

* VVI Pacing Mode - initially with nominal values specified in the pacemaker document
<img width="415" alt="image" src="https://user-images.githubusercontent.com/68765813/197439910-729ccf48-f4ec-4c61-b299-11d7d5c0d2a6.png">

## Group Members
Noor Al-Rajab, Kailin Chu, Kabir Gupta, Dorian Knight, Mathew Nacev
