import numpy as np
import matplotlib.pyplot as plt



data = np.loadtxt('graph1.txt', delimiter=',', dtype='Float64', skiprows=1)
print(data)
##plt(data[:, 1], data[:, 0], 'g')
gps = data[:,1];
data2 = np.loadtxt('graph2.txt', delimiter=',', dtype='Float64', skiprows=1)
acclr = data2[:,1]
print(np.std(gps))
print(np.std(acclr))
