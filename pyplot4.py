import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([1,4,9,16,25])

plt.plot(x,y)
plt.plot(x,y,'sg')
plt.plot(x,y,'r--o')

plt.xlabel('x axis-some numbers')
plt.ylabel('y axis-some numbers')
plt.show()