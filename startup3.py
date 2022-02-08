import mysql.connector as mc
from nameandpass import name,passwd
import pandas as pd

db = mc.connect(
    host = 'localhost',
    user = {name},
    passwd = {passwd},
    database = 'hostels'
)

myc = db.cursor(buffered=True)

myc.execute("SELECT * from hostels")
hostels_names = [x[1] for x in myc]
myc.execute("SELECT * from hostels")
hostels_id = [x[0] for x in myc]

def create_tables_hostels():
    for name in hostels_names:
        # tup = (name,)
        myc.execute(f"CREATE TABLE {name}(Adminno int PRIMARY KEY,Student_name varchar(50),Age smallint ,Class smallint ,Gender char(10),Hostel_ID int,FOREIGN KEY (Adminno) REFERENCES Students(Adminno), FOREIGN KEY(Hostel_ID) REFERENCES Hostels(Hostel_ID) ON UPDATE CASCADE ON DELETE CASCADE)")
        db.commit()
    myc.execute("ALTER TABLE Students ADD FOREIGN KEY(Hostel_ID) REFERENCES Hostels(Hostel_ID) ON UPDATE CASCADE ON DELETE CASCADE")

def add_data_students():
    studata = pd.read_csv(r'D:\Pranav\Studentsfakedata.csv',index_col=False, delimiter=',')
    studata.head()
    for i,row in studata.iterrows():
        myc.execute(f"INSERT INTO Students(Adminno,Name,Age,Class,Sex,Father_name,Mother_name,DOB,Phone_number,Email,Hostel_Id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",tuple(row))
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

try:
    create_tables_hostels()
    try:
        add_data_students()
        try:
            add_data_hotels_students()
            print('Data Entered')
        except:
            print('Data Already Entered')
            print('Run Ready.py')
    except:
        try:
            add_data_hotels_students()
            print('Data Entered')
        except:
            print('Data Already entered')
            print('Run Ready.py')
    print('Run Ready.py')
except Exception:
    try:
        add_data_students()
        try:
            add_data_hotels_students()
            print('Data Entered')
        except:
            print('Data Already Entered')
            print('Run Ready.py')
    except:
        try:
            add_data_hotels_students()
            print('Data Entered')
        except:
            print('Data Already entered')
            print('Run Ready.py')

    print('Run Ready.py')
