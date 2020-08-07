import sqlite3

with sqlite3.connect(":memory:") as con:
    c = con.cursor()
    c.execute('''create table sensors(date text , city text , code text , sensor_id real , temparature real)''')
    for table in c.execute("select name from sqlite_master where type = 'table'"):
        print("Table" , table[0])
        c.execute("INSERT INTO sensors VALUES ('2016-11-05','Utrecht','Red',42,15.14)")
        c.execute("select * from sensors")
        print(c.fetchone())
