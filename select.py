import sqlite3
cn=sqlite3.connect("db1.db")
cn=cn.execute("select id,name,age,salary from developer")
for row in cn:
	print("id=",row[0])
	print("name=",row[1])
	print("age=",row[2])
	print("salary=",row[3])

print("operation performed successfully")
cn.close()