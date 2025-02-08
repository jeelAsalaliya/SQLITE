import sqlite3

cn=sqlite3.connect("dbExam.db")
print("Database connected successfully")

cn.execute("DROP TABLE IF EXISTS student")
cn.execute('''CREATE TABLE student 
	(rno integer primary key, 
	 name text,
	 age integer check(age>6),
	 sub1 integer,
	 sub2 integer,
	 sub3 integer,
	 total integer)''')

print("Table created successfully")

rows=[(1,'Raj',9,56,45,66,167),
	(2,'Jay',12,88,44,55,187),
	(3,'Neel',18,36,52,23,111),
	(4,'Rahul',20,68,98,78,244),
	(5,'Aditya',7,20,30,40,90)]

cn.executemany("INSERT INTO student(rno,name,age,sub1,sub2,sub3,total) VALUES(?,?,?,?,?,?,?)",rows)
cn.commit()
print("Records inserted successfully")

cn.execute('UPDATE student SET name="Ram" WHERE rno=1')
cn.commit()
print("Record updated successfully")

cn.execute('DELETE FROM student	WHERE rno=2')
cn.commit()
print('Record deleted successfully')

print('----Dispaly student details of highest total marks----')
cursor=cn.execute('''SELECT * FROM student 
		   WHERE total IN (SELECT max(total) FROM student)''')

title=cursor.description
for t in title:
	print(t[0],end=' ')

print()
for row in cursor:
	print(row)

cn.close()