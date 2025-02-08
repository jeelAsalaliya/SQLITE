import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Q8.csv',index_col=0)

x=df['Year']
y=df['Totalsales']

plt.bar(x,y,width=0.5,color='red',alpha=0.5)

plt.xlabel('Years')
plt.ylabel('Total Sales')
plt.title('Sales Report')

plt.show()


'''
.open dbExam.db

CREATE TABLE sales
(SID int PRIMARY KEY,
Year int
Totalsales int);

INSERT INTO sales VALUES (1,2018,78000); 
INSERT INTO sales VALUES (2,2019,56000); 
INSERT INTO sales VALUES (3,2020,14000); 
INSERT INTO sales VALUES (4,2021,88000); 
INSERT INTO sales VALUES (5,2022,74000); 
INSERT INTO sales VALUES (6,2023,64000); 

.header=ON
.output Q8.csv
SELECT * FROM sales;
'''



