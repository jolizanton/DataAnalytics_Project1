import sqlite3
conn = sqlite3.connect('student_details.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE STUDENT_DETAILS
         (ROLL_NUMBER INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         CLASS            INT     NOT NULL);''')
print ("Table created successfully")
conn.close()