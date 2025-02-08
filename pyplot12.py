import matplotlib.pyplot as plt
import numpy as np

x=np.array(['2018','2019','2020','2021'])
y_boys=np.array([50,120,60,100])
y_girls=np.array([60,80,90,200])
y_total=np.array([110,200,150,300])

b1=plt.bar(x,y_boys,width=0.5)
b2=plt.bar(x,y_girls,width=0.5,bottom=y_boys)
b3=plt.bar(x,y_total,width=0.5,bottom=np.add(y_boys,y_girls))

plt.legend(['boys','girls','total'])
plt.bar_label(b1,label_type='center')
plt.bar_label(b2,label_type='center')
plt.bar_label(b3,label_type='edge')

plt.show()