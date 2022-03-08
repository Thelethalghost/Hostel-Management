import mysql.connector as mc
from nameandpass import name,passwd
import startup3

def run():

    db = mc.connect(
        host = 'localhost',
        user = name,
        passwd = passwd,
        database = 'Hostels_Management'
    )

    myc = db.cursor(buffered=True)

    def createtables():
        myc.execute(
            "CREATE TABLE Students(Adminno int PRIMARY KEY,Name varchar(50),Age int UNSIGNED,Class smallint UNSIGNED,Sex char(10),Father_name varchar(100), Mother_name varchar(100), DOB Varchar(15),Phone_number bigint UNSIGNED,Email varchar(100), Hostel_ID int)")
        myc.execute("CREATE TABLE Hostels(Hostel_ID int PRIMARY KEY, Name varchar(20))")

    def add_data_hostels():

        while True:

            hostelid = int(input("Enter the hostel id: "))
            name = input("Enter Hostel name(Please refrainf from using spaces. use underscore(_) instead): ")
            myc.execute(f"INSERT INTO Hostels(Hostel_ID,Name) values(%s,%s)", (hostelid, name))
            db.commit()
            c = input('Another data(Y/n): ').lower()
            if c == 'n':
                break

    def create_tables_hostels():
        myc.execute("SELECT * from hostels")
        hostels_names = [x[1] for x in myc]
        for na in hostels_names:
            myc.execute(f"CREATE TABLE {na}(Adminno int PRIMARY KEY,Student_name varchar(50),Age smallint ,Class smallint ,Gender char(10),Hostel_ID int")
        db.commit()

    def checkup():
        check = input('Enter Data changed(Y/n): ').lower()
        if check == 'y':
            startup3.run()
        else:
            print("Please change the data")
            checkup()

    try:
        createtables()

        try:
            add_data_hostels()
            create_tables_hostels()
            print(
                'Please make sure that hostel id field in the csv file has only the numbers you have entered now. If not please change it')
            checkup()
        except:
            try:
                create_tables_hostels()
                print(
                    'Please make sure that hostel id field in the csv file has only the numbers you have entered now. If not please change it')
                checkup()
            except:
                print(
                    'Please make sure that hostel id field in the csv file has only the numbers you have entered now. If not please change it')
                checkup()
    except Exception:
        print('Tables Already created.')
        myc.execute('SELECT Hostel_ID FROM Hostels')
        hostelids = [x[0] for x in myc]
        print(hostelids)
        print('Please make sure that hostel ids in the studentsfakedata.csv file is in the range of number that are printed above')
        checkup()