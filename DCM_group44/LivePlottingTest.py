'''
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.5)

n = 0
while(True):
    y = np.random.random()
    plt.scatter(n,y)
    n+=1
    plt.pause(0.5)

plt.show()
'''

from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate(i):
    global x
    x += 1 #np.abs(np.random.randn())
    y = np.random.randn()
    data.append((x, y))
    line.set_data(formatData(data))
    ax.relim()
    ax.autoscale_view(scaley=True)
    
    #formatData(data)
    #print(data)
def formatData(data):
    #Iterate through the deque data and isolate all of the x-coords into one tuple and all of the y-coords into another tuple
    x = []
    y = []  #Initialize empty lists
    for i in range(len(data)):
        x.append(data[i][0])
        y.append(data[i][1])
    print(x)
    print(y)
    return x,y
        
        
    
    
fig, ax = plt.subplots()
x = 0
y = np.random.randn()
#plt.ylim([-1,1])
data = deque([(x, y)], maxlen=10)
line = plt.plot((0),(0), c='black')[0]
#line.set_data(zip(*[(0,2),(1,3),(2,-1)]))
#line.set_data((0,1,2),(2,3,-1))
ax.relim()
ax.autoscale_view(scaley=True)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()