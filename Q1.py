import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

cn=sqlite3.connect("dbExam.db")
print("Database connected successfully")

df=pd.read_sql('SELECT * FROM dept',cn)
df['avg_pay']=df['totpayment']/df['noofemp']

df.to_csv('Q1.csv',index=False)

cn.close()

x=df['dname']

y1=df['noofemp']
y2=df['totpayment']

plt.subplot(1,2,1)
plt.scatter(x,y1,marker='^',edgecolor='r',s=150,c='c')
plt.title('scatter plot: deparments VS no.of employees')
plt.xlabel('X axis: departments')
plt.ylabel('Y axis: no. of employees')

plt.subplot(1,2,2)
plt.scatter(x,y2,marker='o',edgecolor='b',s=250,c='m')
plt.title('scatter plot: deparments VS total payments')
plt.xlabel('X axis: departments')
plt.ylabel('Y axis: total payments')

plt.show()


'''
.open dbExam.db

CREATE TABLE dept
(did int PRIMARY KEY,
dname text,
noofemp int,
totpayment int);

INSERT INTO dept VALUES (10,'Account',10,3000); 
INSERT INTO dept VALUES (20,'Sales',20,70000); 
INSERT INTO dept VALUES (30,'Purchase',25,65000); 
INSERT INTO dept VALUES (40,'Production',50,88000); 
INSERT INTO dept VALUES (50,'Management',5,90000); 

'''
