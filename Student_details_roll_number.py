import sqlite3

conn = sqlite3.connect('student_details.db')
cursor = conn.cursor()

active=True
while active:
    details_required_roll_number=int(input("Enter the roll number:"))

    cursor = conn.execute("SELECT ROLL_NUMBER, NAME, CLASS from STUDENT_DETAILS_NEW")
    for row in cursor:
        if details_required_roll_number==row[0]:
            print (f"Find the details of Roll number:{row[0]}")
            print ("NAME = ", row[1])
            print ("CLASS = ", row[2], "\n")

    repeat = input("Would you like to see another student's details? (y/n) ")
    if repeat == 'n':
        active = False

conn.close()
