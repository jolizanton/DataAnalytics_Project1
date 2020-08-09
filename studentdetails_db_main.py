import sqlite3

conn = sqlite3.connect('db/student_details.db')
cursor = conn.cursor()

try:
    conn.execute('''CREATE TABLE STUDENT_DETAILS_NEW
             (ROLL_NUMBER INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             CLASS            INT     NOT NULL);''')
except sqlite3.OperationalError:
    print("Table already exist")

choice=input("Press '1' to enter the details/Press '2' to view the details:")
if choice=='1':

    active=True
    while active:
        print ("Press q to quit")
        print("Enter the details:")
        roll_number=int(input("Enter the roll number:"))

        if roll_number== 'q':
            break

        name=input("Enter the name:")
        if name == 'q':
            break
        Class= input("Enter the class:")
        if Class == 'q':
            break

        repeat = input("Would you like to store another student's details? (y/n) ")
        if repeat == 'n':
            active = False

        try:
            cursor.execute("""
            INSERT INTO STUDENT_DETAILS_NEW(ROLL_NUMBER, NAME, CLASS)
            VALUES (?,?,?)
            """, (roll_number, name, Class))
            conn.commit()
        except sqlite3.IntegrityError:
            print ("Details of this roll number already exist")
        else:
            print ('Data entered successfully.')

else:
    active = True
    while active:
        details_required_roll_number = int(input("Enter the roll number:"))
        cursor = conn.execute("SELECT ROLL_NUMBER, NAME, CLASS from STUDENT_DETAILS_NEW")
        for row in cursor:
            if details_required_roll_number == row[0]:
                print (f"Find the details of Roll number:{row[0]}")
                print ("NAME = ", row[1])
                print ("CLASS = ", row[2], "\n")
        else:
            print ("Details of this roll number does not exist")

        repeat = input("Would you like to see another student's details? (y/n) ")
        if repeat == 'n':
            active = False

conn.close()
