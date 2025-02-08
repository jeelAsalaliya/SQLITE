import sqlite3

cn=sqlite3.connect("dbExam.db")
print("Database connected successfully")

query='SELECT * FROM student WHERE name LIKE "_a%a"'

def disp_stud(cn,query):
	print("----Dispaly student details whose name's first and last letter is 'a'----")
	cursor=cn.execute(query)

	title=cursor.description
	for t in title:
		print(t[0],end=' ')

	print()
	for row in cursor:
		print(row)

	cn.close()


'''
.open dbExam.db

DROP TABLE student

CREATE TABLE student
(sid int PRIMARY KEY,
sname text,
city text
age int check>6)

INSERT INTO student VALUES (1,'Rama','Surat',20); 
INSERT INTO student VALUES (2,'Radha','Pune',18); 
INSERT INTO student VALUES (3,'Mahira','Mumbai',9); 
INSERT INTO student VALUES (4,'Raj','Delhi',7); 
INSERT INTO student VALUES (5,'Naina','Banglore',13); 
INSERT INTO student VALUES (6,'Neel','Hydrabad',6); 

'''