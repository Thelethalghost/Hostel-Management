import mysql.connector as mc
import csv

db = mc.connect(
    host = "localhost",
    user = "pranav",
    passwd = "root",
    database = "Hostels"
)

myc = db.cursor()

myc.execute("SELECT * from hostels") # do not comment out this query
hostels_names = [x[1] for x in myc]
def createdatabase():
    myc.execute("CREATE DATABASE Hostels")
def createtables():
    myc.execute("CREATE TABLE Students(Adminno int PRIMARY KEY,Name varchar(50), Class smallint UNSIGNED,Father_name varchar(100), Mother_name varchar(100), DOB Varchar(15),Phone_number int UNSIGNED,Email varchar(100), Age int,Adress varchar(200), Hostel_ID int)")

    myc.execute("CREATE TABLE Hostels(Hostel_ID int PRIMARY KEY, Name varchar(20))")

def add_data_hostels():
    
    global hostels_names

    

    while True:

        hostelid = int(input("Enter the hostel id: "))                
        name = input("Enter Hostel name: ")
        myc.execute(f"INSERT INTO Hostels(Hostel_ID,Name) values(%s,%s)",(hostelid,name))
        # hostels_names.append(name)
        c = input('Another data(Y/n): ').lower()
        if c == 'n':
            break
    db.commit()


def add_data():
    while True:
        ask = input("Enter the name of the hostel name in which you want add the student: ")
        hotelid = myc.execute(f"SELECT Hostel_ID FROM Hostels WHERE Name = {ask}")
        adminno = int(input("Enter the admission number of the student: "))
        name = input("Enter the name of the student: ")
        age = int(input("Enter the age of the student: "))
        classe = int(input("Enter the class of the student: "))
        pass

# myc.execute("ALTER TABLE Students ADD FOREIGN KEY (Hostel_ID) REFERENCES Hostels(Hostel_ID)")

# createdatabase()

# createtables()

# add_data_hostels()

print(hostels_names)
