import sqlite3
import pandas as pd

cn=sqlite3.connect("dbExam.db")
print("Database connected successfully")

cn.execute("DROP TABLE IF EXISTS emp")
cn.execute('''CREATE TABLE emp 
	(empno integer primary key, 
	 name text,
	 city rext,
	 designation text,
	 salary integer,
	 hiredate text)''')

print("Table created successfully")

rows=[(1,'Raj','Surat','Manager',66000,'1988-11-17'),
	(2,'Jay','Pune','President',90000,'1998-05-01'),
	(3,'Neel','Mumbai','Accountant',20000,'1985-04-09'),
	(4,'Rahul','Delhi','Clerk',25000,'1990-03-21'),
	(5,'Aditya','Banglore','Analyst',50000,'1992-07-30')]

cn.executemany("INSERT INTO emp(empno,name,city,designation,salary,hiredate) VALUES(?,?,?,?,?,?)",rows)
cn.commit()
print("Records inserted successfully")

print('----Dispaly employee details using cursor----')
cursor=cn.execute('SELECT * FROM emp')

title=cursor.description
for t in title:
	print(t[0],end=' ')
	
print()
for row in cursor:
	print(row)
	
df=pd.read_sql('SELECT * FROM emp',cn)
df.to_csv('Q11-12.csv',index=False)

cn.close()