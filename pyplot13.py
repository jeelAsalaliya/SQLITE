import matplotlib.pyplot as plt
import numpy as np

x=np.array(['2018','2019','2020','2021'])
y_boys=np.array([50,100,60,100])
y_girls=np.array([60,80,90,200])
y_child=np.array([10,20,30,40])
y_total=np.array([120,220,180,340])

w=0.2
x_axis=np.arange(len(x))
plt.bar(x_axis+(w/2),y_boys,width=w,label='boys')
plt.bar(x_axis+(w+w/2),y_girls,width=w,label='girls')
plt.bar(x_axis+(w*2+w/2),y_child,width=w,label='child')
plt.bar(x_axis+(w*3+w/2),y_total,width=w,label='total')

plt.xticks(x_axis,x)
plt.legend()
plt.show()