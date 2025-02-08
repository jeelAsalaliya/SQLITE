import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

cn=sqlite3.connect("dbExam.db")
print("Database connected successfully")

cn.execute("DROP TABLE IF EXISTS teacher")
cn.execute('''CREATE TABLE teacher 
	(tid integer primary key, 
	 tname text,
	 salary real,
	 working_hrs real)''')

print("Table created successfully")

rows=[(101,'Raj',66000,72),
	(102,'Jay',55000,65),
	(103,'Neel',20000,70),
	(104,'Rahul',47000,68),
	(105,'Aditya',70000,54)]

cn.executemany("INSERT INTO teacher(tid,tname,salary,working_hrs) VALUES(?,?,?,?)",rows)
cn.commit()
print("Records inserted successfully")

print('----Dispaly details of teacher in descending order of salary----')
cursor=cn.execute('SELECT * FROM teacher ORDER BY salary DESC')

title=cursor.description
for t in title:
	print(t[0],end=' ')
	
print()
for row in cursor:
	print(row)

print()
print('----Dispaly details of highest salaried teachers----')
cursor=cn.execute('''SELECT tname,salary,working_hrs FROM teacher 
		WHERE salary IN (SELECT max(salary) FROM teacher)''')

title=cursor.description
for t in title:
	print(t[0],end=' ')
	
print()
for row in cursor:
	print(row)

print()
print('----Dispaly details of teachers whose salary between 45000 and 65000----')
cursor=cn.execute('''SELECT tname,salary FROM teacher 
		WHERE salary BETWEEN 45000 AND 65000''')

title=cursor.description
for t in title:
	print(t[0],end=' ')
	
print()
for row in cursor:
	print(row)

df=pd.read_sql('SELECT * FROM teacher',cn)
x=df['tname']

y1=df['working_hrs']
y2=df['salary']

plt.subplot(1,2,1)
plt.bar(x,y1)
plt.title('bar chart: Teachers VS Working hours')
plt.xlabel('X axis: teacher names')
plt.ylabel('Y axis: working hours')

plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title('line chart: Teachers VS Salary')
plt.xlabel('X axis: teacher names')
plt.ylabel('Y axis: salary')

plt.show()
