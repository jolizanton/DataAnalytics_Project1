import sqlite3

conn = sqlite3.connect('student_details.db')
cursor = conn.cursor()

student_details = []

active=True
while active:
    print ("Press q or 0 to quit")
    print("Enter the details:")
    roll_number=int(input("Enter the roll number:"))
    if roll_number== 'q' or '0':
        break
    name=input("Enter the name:")
    if name == 'q' or '0':
        break
    Class= input("Enter the class:")
    if Class == 'q' or '0':
        break

    repeat = input("Would you like to store another student's details? (y/n) ")
    if repeat == 'n':
        active = False

    cursor.execute("""
    INSERT INTO STUDENT_DETAILS_NEW(ROLL_NUMBER, NAME, CLASS)
    VALUES (?,?,?)
    """, (roll_number, name, Class))
    conn.commit()
    print ('Data entered successfully.')

conn.close()
