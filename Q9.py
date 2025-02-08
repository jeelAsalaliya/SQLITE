import pandas as pd
import matplotlib.pyplot as plt

data={
	'Prod_name':['AC','TV','Microwave','Refrigerator','Dish Washer'],
	'Jan':[1000,2000,3000,4000,5000],
	'Feb':[500,1500,3500,4500,2500],
	'Mar':[1700,3700,700,2700,4700],
	'Apr':[2900,900,1900,4900,3900],
	'May':[2200,3200,4200,200,1200],
	'Jun':[500,400,300,200,100]
      }

df=pd.DataFrame(data)
df.to_csv('Q9.csv',index=False)

df=pd.read_csv('Q9.csv')

df['Totalsales']=df['Jan']+df['Feb']+df['Mar']+df['Apr']+df['May']+df['Jun']
df['Avgsales']=df['Totalsales']/6
df.to_csv('Q9.csv',index=False)

x=df['Prod_name']
y_total=df['Totalsales']
y_avg=df['Avgsales']

plt.plot(x,y_total,'or--',label='Total Sales')
plt.plot(x,y_avg,'Hg:',label='Avg Sales')
plt.legend()

plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Total and Average Sales Report')

plt.show()

