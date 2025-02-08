import matplotlib.pyplot as plt
import numpy as np

y=np.array([100,170,230,300])
x=list(map(str,range(2018,2018+len(y))))

plt.bar(x,y,width=0.5,color=['red','orange','green','blue'],alpha=0.5)
plt.grid(color="brown",linestyle='--',linewidth=2,alpha=0.5)

#axis=both(default)
plt.minorticks_on()
plt.grid(color="brown",linestyle='--',linewidth=2,axis='y',which='minor')

plt.xlabel('years')
plt.ylabel('number of students')
plt.title('bca')
plt.show()