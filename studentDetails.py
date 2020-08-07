student_details={}
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

    student_details[roll_number]= [name,Class]
    repeat = input("Would you like to store another student's details? (y/n) ")
    if repeat == 'n':
        active = False

details_required_roll_number= int(input("Enter the roll number to view the details:"))
for roll_number,details in student_details.items():
    if details_required_roll_number==roll_number:
        print (f"\nName: {details[0].title()}\nClass: {details[1]}")

