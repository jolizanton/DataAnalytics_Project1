import sqlite3

conn = sqlite3.connect('student_details.db')
print "Opened database successfully";

cursor = conn.execute("SELECT ROLL_NUMBER, NAME, CLASS from STUDENT_DETAILS")
for row in cursor:
   print "ROLL_NUMBER = ", row[0]
   print "NAME = ", row[1]
   print "CLASS = ", row[2], "\n"

conn.close()
