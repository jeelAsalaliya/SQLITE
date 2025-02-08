import matplotlib.pyplot as plt
import numpy as np

x1=np.array([0,1,2,3,4,5])
y1=np.array([3,0,3,0,3,0])
y2=np.array([0,-3,0,-3,0,-3])

plt.plot(x1,y1,'m',marker='o',ms=20,mfc='c',mec='b')
plt.plot(x1,y2,'b--',marker='H',ms=15,mfc='#00ff00',mec='#ff0000')

plt.show()