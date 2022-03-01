import mysql.connector as mc
from nameandpass import name,passwd
import pandas as pd

def run():
    db = mc.connect(
        host = 'localhost',
        user = name,
        passwd = passwd,
        database = 'Hostels_Management'
    )

    myc = db.cursor(buffered=True)



    def add_data_students():
        studata = pd.read_csv(r'Studentsfakedata.csv',index_col=False, delimiter=',')
        studata.head()
        for i,row in studata.iterrows():
            myc.execute(f"INSERT INTO Students(Adminno,Name,Age,Class,Sex,Father_name,Mother_name,DOB,Phone_number,Email,Hostel_Id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",tuple(row))
            db.commit()

    def add_data_hotels_students():
        myc.execute("SELECT * from hostels")
        hostels_names = [x[1] for x in myc]
        myc.execute("SELECT * from hostels")
        hostels_id = [x[0] for x in myc]
        for i in hostels_id:
            myc.execute(f"SELECT Adminno, Name,Age,Class,Sex,Hostel_ID FROM students where Hostel_ID = {i}")
            name = hostels_names[i-1]
            data = myc.fetchall()
            for row in data:
            # print(type(row))
                myc.execute(f"INSERT INTO {name}(Adminno,Student_name,Age,Class,Gender,Hostel_ID) VALUES(%s,%s,%s,%s,%s,%s)",row)
                db.commit()

    try:
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
