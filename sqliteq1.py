
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

cn=sqlite3.connect("dbexam.db")
print("database connected successfully")

df=pd.read_sql('select * from dept',cn)
df['avg_pay']=df['totpayment']/df['noofemp']
df.to_csv('q1.csv',index=False)

cn.close()

x=df['dname']

y1=df['noofemp']
y2=df['totpayment']

plt.subplot(1,2,1)
plt.scatter(x,y1,marker='^',edgecolor="r",s=150,c='c')
plt.title('scatter plot:departments vs no.of.employees')
plt.xlabel('x axis:departments')
plt.ylabel('y axis:no_of_employee')


plt.subplot(1,2,2)
plt.scatter(x,y2,marker='o',edgecolor='b',s=250,c='m')
plt.ylabel('y axis:total_payments')
plt.xlabel('x axis:departments')
plt.title('scatter plot:department vs total_payment')
plt.show()