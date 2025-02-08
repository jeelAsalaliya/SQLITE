import matplotlib.pyplot as plt
import numpy as np

x=np.array(['2018','2019','2020','2021'])
y=np.array([100,200,150,300])

#plt.bar(x,y)
plt.bar(x,y,width=0.2,color="red")
#plt.barh(x,y,height=0.2)

plt.show()