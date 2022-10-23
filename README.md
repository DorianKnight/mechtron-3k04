# mechtron-3k04
Simulating a pacemaker for MechTron 3K04

To simulate the pacemaker download the file "Group44PACEMAKER.slx". If you wish to deploy the code to the FDRM board, you must first comment out the requirements table held within the Output pins subsystem

If you wish to switch the operating mode. Navigate to the inputs subsystem and find the "mode" string constant box. Enter in "AOO" for Asynchronous pacing of the atria, "VOO" for asynchronous pacing of the ventricle, "AAI" for sensing in the atria and inhibiting paces if a natural heart beat was sensed, and "VVI" for sensing in the ventricle and inhibiting paces if a natural heart beat was sensed.

For further explanations, please refer to this video we created walking through our entire project: https://www.youtube.com/watch?v=dQw4w9WgXcQ