import matplotlib.pyplot as plt
import  numpy as np

x=np.array([0,1,2,3,4,5])
y=x*2

plt.subplot(3,3,1)
plt.plot(x,y)

y=x*x
plt.subplot(3,3,2)
plt.plot(x,y)

y=x/(x+1)
plt.subplot(3,3,3)
plt.plot(x,y)

y=np.array([0,1,1,2,2,3])
plt.subplot(3,3,4)
plt.plot(x,y)

y=np.array([-5,5,-4,4,-3,3])
plt.subplot(3,3,5)
plt.plot(x,y)

y=np.array([5,4,3,2,1,0])
plt.subplot(3,3,6)
plt.plot(x,y)
plt.show()