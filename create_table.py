import sqlite3
cn=sqlite3.connect("emp1.db")
print("database connected successfully")

cn.execute("drop table if exists student")

cn.execute( ' ' create table student 
	 (rollno integer primary key,
	 name text)'  ')

print("table created successfully")
cn.close()