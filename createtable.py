import mysql.connector as mc
import csv

db = mc.connect(
    host = "localhost",
    user = "pranav",
    passwd = "root",
    database = "Hostels"
)
myc = db.cursor()
def createdatabase():
    myc.execute("CREATE DATABASE Hostels")
def createtables():
    myc.execute("CREATE TABLE Students(Adminno int PRIMARY KEY,Name varchar(50), Class smallint UNSIGNED,Father_name varchar(100), Mother_name varchar(100), DOB Varchar(15),Phone_number int UNSIGNED,Email varchar(100), Age int,Adress varchar(200) )")

    myc.execute("CREATE TABLE Hostels(Hostel_ID int PRIMARY KEY, Name varchar(20))")
    myc.execute("CREATE TABLE Sneh_Sadan(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
    myc.execute("CREATE TABLE RR_House(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
    myc.execute("CREATE TABLE East_House(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
    myc.execute("CREATE TABLE West_House(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
    myc.execute("CREATE TABLE North_House(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
    myc.execute("CREATE TABLE South_House(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
    myc.execute("CREATE TABLE Gokul(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
    myc.execute("CREATE TABLE Shanti_vihar(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
    myc.execute("CREATE TABLE Padma_Kutir(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
    myc.execute("CREATE TABLE Varuna(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
    myc.execute("CREATE TABLE Nilgiri(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
    myc.execute("CREATE TABLE River_Side_Hostel(Adminno int PRIMARY KEY,Student_name varchar(50), Age int,class smallint UNSIGNED, Hostel_ID int, FOREIGN KEY (Adminno) REFERENCES Students(Adminno))")
# createdatabase()
# createtables()
