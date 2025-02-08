import sqlite3
cn=sqlite3.connect("db1.db")
cn.execute("update developer set salary=6000.00 where id=1")
cn.commit()
print("total number of rows updated:",cn.total_changes)
cn.close()