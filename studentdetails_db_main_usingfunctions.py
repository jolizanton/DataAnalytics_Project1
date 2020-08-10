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

def enter_details(roll_number,name,Class):
    if roll_number != 'q'and name != 'q' and Class != 'q':
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


def view_details(details_required_roll_number):
    if details_required_roll_number != 'q':

        cursor = conn.execute("SELECT ROLL_NUMBER, NAME, CLASS from STUDENT_DETAILS_NEW")
        data_exist=False

        for row in cursor:
            if details_required_roll_number == row[0]:
                data_exist=True

                print (f"Find the details of Roll number:{row[0]}")
                print ("NAME = ", row[1])
                print ("CLASS = ", row[2], "\n")
        if not data_exist:
            print ("Details of this roll number does not exist")

choice = input("Press '1' to enter the details/Press '2' to view the details:")

active =True
while active:
    if choice == '1':
        print ("Press q to quit")
        print("Enter the details:")
        enter_details(int(input("Enter the roll number:")), input("Enter the name:"), input("Enter the class:"))
    else:
        view_details(int(input("Enter the roll number:")))

    repeat = input("Would you like to store another student's details? (y/n) ")
    if repeat == 'n':
        active = False


conn.close()
