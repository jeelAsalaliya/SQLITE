import matplotlib.pyplot as plt
import numpy as np

x1=np.array([0,2,4,6,8,10])
y1=x1*2
y2=x1*3

x3=np.array([0,1,2,3,4,5,6,7,8])
y3=x3*4

plt.plot(x1,y1,'o:r')
plt.plot(x1,y2,'^-.g')
plt.plot(x3,y3,'*--',color='black')
plt.legend(['x1y1','x1y2','x3y3'])
plt.show()