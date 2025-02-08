import matplotlib.pyplot as plt
import numpy as np

x1=np.arange(0.0,2.0,0.02)

y1=np.cos(2*(np.pi)*x1)
y2=np.cos(30+2*(np.pi)*x1)
y3=np.cos(60+2*(np.pi)*x1)

plt.plot(x1,y1,'r',linewidth='10')
plt.plot(x1,y2,'b--',linewidth='5')
plt.plot(x1,y3,'g-.')
plt.show()