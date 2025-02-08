import sqlite3
cn=sqlite3.connect("db1.db")

cn.execute('''insert into developer(id,name,age,salary)values(1,'amit',32,25000.00)''')
cn.execute('''insert into developer(id,name,age,salary)values(2,'kinjal',35,15000.00)''')
cn.execute('''insert into developer(id,name,age,salary)values(3,'priyank',36,35000.00)''')
cn.execute('''insert into developer(id,name,age,salary)values(4,'rahul',30,40000.00)''')
cn.execute('''insert into developer(id,name,age,salary)values(5,'jay',33,45000.00)''')

cn.commit()
print("record created successfully")
cn.close()