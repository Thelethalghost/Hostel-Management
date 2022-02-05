import mysql.connector as mc
from nameandpass import name,passwd

db = mc.connect(
    host="localhost",
    user={name},
    passwd={passwd},
    database = 'hostels'
)

myc = db.cursor(buffered=True)

def add_new_data():
    while True:
        ask = input("Enter the name of the hostel name in which you want add the student: ")
        hotelid = myc.execute(f"SELECT Hostel_ID FROM Hostels WHERE Name = {ask}")
        adminno = int(input("Enter the admission number of the student: "))
        name = input("Enter the name of the student: ")
        age = int(input("Enter the age of the student: "))
        classe = int(input("Enter the class of the student: "))
        gender = input("Enter the gender of the student(Male,Female): ")
        myc.execute(f"INSERT INTO {ask}(Adminno,Student_name,Age,Class,Sex,Hostel_ID) values(%s,%s,%s,%s,%s,%s)",(adminno,name,age,classe,gender,hostelid))

def delete():
    ask = input("Enter the name of the hostel you want to delete data from: ")
    adminno= int(input("Enter the admin number of the student you want to delete the data of: "))
    myc.execute(f"DELETE FROM {ask} WHERE adminno={adminno}")
    db.commit()

def modify_data():
    ask = input("enter the hostel name you want to change the data of: ")
    how = int(input("How many columns do you want to modify: "))
    def modify(table_name):
        admi = int_input("Enter the admin number of the student you want to change the data of: ")
        column_name = input("Enter the column name you want to change the data of: ")
        data = input("What do you want to write: ")
        try:
            myc.execute(f"UPDATE {table_name} SET {column_name} = {data} WHERE adminno = {admi}")
        except Exception:
            print("Wrong admin number or column name entered. Please try again")
    for i in range(how):
        modify(ask)

def search():
    num = int(input("Enter the adminno of the student you want the data of: "))
    id = myc.execute(f"SELECT Hostel_ID FROM Students WHERE Adminno = {num}")
    hostel_name = myc.execute(f"SELECT Name FROM Hostels WHERE Hostel_Id = {id}")
    myc.execute(f"SELECT * FROM Hostels WHERE Adminno = {num}")

def  display():
    ask  = input("Enter the name of the hostel you want to see the data of (Don't use space use underscore(_)):  ")
    myc.execute(f"SELECT * FROM {ask}")


def ready():
    ask = input("1. Add Student\n"
                "2. Search for a student\n"
                "3. Modify data\n"
                "4. Display data\n"
                "5. Delete data\n"
                "Enter the option you want to select: ")
    if ask == 1:
        add_new_data()
    elif ask == 2:
        search()
    elif ask == 3:
        modify_data()
    elif ask == 4 :
        display()
    elif ask == 5:
        delete()
    else:
        print("No recognizable option entered")


ready()