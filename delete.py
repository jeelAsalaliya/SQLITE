import sqlite3
cn=sqlite3.connect("db1.db")
cn.execute("delete from developer where id=2")
cn.commit()
print("total number of record deleted:",cn.total_changes)
cn.execute("select *from developer")
cn.close()