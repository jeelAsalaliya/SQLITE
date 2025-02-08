import pandas as pd
import matplotlib.pyplot as plt

data={
	'RNo':[1,2,3,4,5,6],
	'Name':['AAA','BBB','CCC','DDD','EEE','FFF'],
	'Maths':[11,78,10,10,32,89],
	'Science':[22,65,67,20,61,94],
	'English':[54,88,33,30,55,66],
	'SS':[36,49,48,15,87,63],
	'GK':[59,69,70,25,90,40]
      }

df=pd.DataFrame(data)
df.to_csv('Q13.csv',index=False)

df=pd.read_csv('Q13.csv')

nm=df['Name']
total=df['Maths']+df['Science']+df['English']+df['SS']+df['GK']

plt.pie(total,labels=nm,autopct='%1.1f%%')
plt.legend()

plt.title('Student-wise Total Marks Report')

plt.show()
