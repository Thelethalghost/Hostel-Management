import mysql.connector as mc
import csv
import pandas as pd

db = mc.connect(
    host="localhost",
    user="root",
    passwd="root"
)

myc = db.cursor(buffered=True)

# myc.execute("SELECT * from hostels")
# hostels_names = [x[1] for x in myc]
# myc.execute("SELECT * from hostels")
# hostels_id = [x[0] for x in myc]

def createdatabase():
    myc.execute("CREATE DATABASE Hostels")

def createtables():
    myc.execute(
        "CREATE TABLE Students(Adminno int PRIMARY KEY,Name varchar(50),Age int UNSIGNED,Class smallint UNSIGNED,Sex char(10),Father_name varchar(100), Mother_name varchar(100), DOB Varchar(15),Phone_number bigint UNSIGNED,Email varchar(100), Hostel_ID int)")

    myc.execute("CREATE TABLE Hostels(Hostel_ID int PRIMARY KEY, Name varchar(20))")

def add_data_hostels():

    while True:

        hostelid = int(input("Enter the hostel id: "))
        name = input("Enter Hostel name(Please refrainf from using spaces. use underscore(_) instead): ")
        myc.execute(f"INSERT INTO Hostels(Hostel_ID,Name) values(%s,%s)", (hostelid, name))
        c = input('Another data(Y/n): ').lower()
        if c == 'n':
            break
    db.commit()

def create_tables_hostels():
    for name in hostels_names:
        # tup = (name,)
        myc.execute(f"CREATE TABLE {name}(Adminno int PRIMARY KEY,Student_name varchar(50),Age smallint ,Class smallint ,Gender char(10),Hostel_ID int,FOREIGN KEY (Adminno) REFERENCES Students(Adminno), FOREIGN KEY(Hostel_ID) REFERENCES Hostels(Hostel_ID))")
        db.commit()
    myc.execute("ALTER TABLE Students ADD FOREIGN KEY(Hostel_ID) REFERENCES Hostels(Hostel_ID)")

def add_data_students():
    studata = pd.read_csv(r'D:\Pranav\Studentsfakedata.csv',index_col=False, delimiter=',')
    studata.head()
    for i,row in studata.iterrows():
        myc.execute(f"INSERT INTO Students(Adminno,Name,Age,Class,Sex,Father_name,Mother_name,DOB,Phone_number,Email,Hostel_Id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",tuple(row))
        # myc.execute(sql,tuple(row))
        # print(tuple(row))
        # print(row)
        db.commit()

def add_data_hotels_students():
    for i in hostels_id:
        myc.execute(f"SELECT Adminno, Name,Age,Class,Sex,Hostel_ID FROM students where Hostel_ID = {i}")
        name = hostels_names[i-1]
        data = myc.fetchall()
        for row in data:
            # print(type(row))
             myc.execute(f"INSERT INTO {name}(Adminno,Student_name,Age,Class,Gender,Hostel_ID) VALUES(%s,%s,%s,%s,%s,%s)",row)
             db.commit()
            # print(name)
            # print(x)

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
        column_name = input("Enter the column name you want to change the data of: ")
        data = input("What do you want to write: ")
        myc.execute(f"UPDATE {table_name} SET {column_name} = {data}")

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

def startup():
    try:
        createdatabase()
        print("in the conection after root add a , and add database='Hostels'")
        print("After adding run startup_2 by removing the hash'#'")
        print("Add hash in the starting of the line containg startup()")


    except Exception:
        print("in the conection after root add a , and add database='Hostels'")
        print("After adding run startup_2 by removing the hash'#'")
        print("Add hash in the starting of the line containg startup()")

def startup_2():
    createtables()
    add_data_hostels()
    print("Unhash the first four hashed lines")
    print("Unhash startup_3 and hash startup_2 and run again")

def startup_3():
    add_data_students()
    create_tables_hostels()
    add_data_hotels_students()
    print('Hash the startup_3() line and unhash the ready line and run to start using this sytem')

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



startup()
# startup_2()
# startup_3()
# ready()
