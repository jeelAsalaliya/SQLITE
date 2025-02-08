import sqlite3
cn=sqlite3.connect("db1.db")
print('--------------fetchall data--------------')
cursor=cn.execute("select *from developer")
print(cursor.fetchall())

print('--------------fetch one record----------')
cursor=cn.execute("select *from developer")
print(cursor.fetchone())
cn.commit()
cn.close()