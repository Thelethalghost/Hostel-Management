import mysql.connector as mc
from nameandpass import name,passwd


db = mc.connect(
    host="localhost",
    user=name,
    passwd=passwd,
    database = 'hostels_Management'
)

myc = db.cursor(buffered=True)

def add_new_data():
        ask = input("Enter the name of the hostel name in which you want add the student: ")
        myc.execute("SELECT Hostel_ID FROM Hostels WHERE (Name = %s) ",(ask,))
        hotelid = [x for x in myc]
        id = None
        for item in hotelid[0]:
            id = item
        adminno = int(input("Enter the admission number of the student: "))
        name = input("Enter the name of the student: ")
        age = int(input("Enter the age of the student: "))
        classe = int(input("Enter the class of the student: "))
        gender = input("Enter the gender of the student(Male,Female): ")
        query = f"INSERT INTO {ask}(Adminno,Student_name,Age,Class,Gender,Hostel_ID) values(%s,%s,%s,%s,%s,%s)"
        myc.execute(query,(adminno,name,age,classe,gender,id))
        # print(id)

def delete():
    ask = input("Enter the name of the hostel you want to delete data from: ")
    adminno= int(input("Enter the admin number of the student you want to delete the data of: "))
    myc.execute(f"DELETE FROM {ask} WHERE adminno={adminno}")
    db.commit()

def modify_data():
    ask = input("enter the hostel name you want to change the data of: ")
    how = int(input("How many columns do you want to modify: "))
    def modify(table_name):
        admi = int(input("Enter the admin number of the student you want to change the data of: "))
        column_name = input("Enter the column name you want to change the data of: ")
        data = input("What do you want to write: ")
        try:
            myc.execute(f"UPDATE {table_name} SET {column_name} = %s WHERE adminno = {admi}",(data,))
            db.commit()
        except Exception:
            print("Wrong admin number or column name entered. Please try again")
    for i in range(how):
        modify(ask)

def search():
    num = int(input("Enter the adminno of the student you want the data of: "))
    myc.execute(f"SELECT Hostel_ID FROM Students WHERE Adminno = {num}")
    id = [x for x in myc]
    query = "SELECT Name FROM Hostels WHERE (Hostel_ID = %s)"
    myc.execute(query,tuple(id[0]))
    hostel_name = [i for i in myc]
    hname = ''
    for item in hostel_name[0]:
        hname = hname + item
    def minisearch(table_name,val):
        myc.execute(f"SELECT * FROM {table_name} WHERE (Adminno = %s)",(val,))
        for y in myc:
            print(y)
    minisearch(hname,num)

def search2():
    num = int(input("Enter the adminno of the student you want the data of: "))
    myc.execute('SELECT students.*, Hostels.name FROM Students,Hostels where Students.hostel_ID = hostels.Hostel_ID and Students.Adminno = %s',(num,))
    for x in myc:
        print(x)


def  display():
    myc.execute("SELECT * FROM Hostels")
    for i in myc:
        print(i)
    ask  = input("Enter the name of the hostel you want to see the data of (Don't use space use underscore(_)):  ")
    myc.execute(f"SELECT * FROM {ask}")
    for x in myc:
        print(x)


def ready():
    while True:
        ask = int(input("1. Add Student\n"
                "2. Search for a student\n"
                "3. Modify data\n"
                "4. Display data\n"
                "5. Delete data\n"
                "6.Exit\n"
                "Enter the option you want to select: "))
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
        elif ask == 6:
            break
        else:
            print("No recognizable option entered")

def login():
    aname = input("Enter the username of mysql: ")
    pd = input("Enter the password of the mysql: ")
    if (aname == name and pd == passwd):
        ready()
    else:
        print("Wrong password entered")


# login()
search2()
# add_new_data()