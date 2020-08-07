import sqlite3

conn = sqlite3.connect('student_details.db')
cursor = conn.cursor()
# create a table
conn.execute('''CREATE TABLE STUDENT_DETAILS_NEW
         (ROLL_NUMBER INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         CLASS            INT     NOT NULL);''')