import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,4,9,16,25]

plt.plot(x,y,'s:r')
plt.plot(x,y,marker='s',linestyle=':',color='red')

plt.xlabel('x axis-some numbers')
plt.ylabel('y axis-some numbers')
plt.show()