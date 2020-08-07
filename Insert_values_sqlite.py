import sqlite3

conn = sqlite3.connect('student_details.db')
print "Opened database successfully";

conn.execute("INSERT INTO STUDENT_DETAILS (ROLL_NUMBER,NAME,CLASS) \
      VALUES (1, 'Joliz', 12)");

conn.execute("INSERT INTO STUDENT_DETAILS (ROLL_NUMBER,NAME,CLASS) \
      VALUES (2, 'Jozil', 10)");

conn.execute("INSERT INTO STUDENT_DETAILS (ROLL_NUMBER,NAME,CLASS) \
      VALUES (3, 'Melvin', 9)");

conn.execute("INSERT INTO STUDENT_DETAILS (ROLL_NUMBER,NAME,CLASS) \
      VALUES (4, 'Shalvin', 8)");


conn.commit()
print "Records created successfully";
conn.close()
