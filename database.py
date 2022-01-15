import mysql.connector as mc

db = mc.connect(
    host = "localhost",
    user = "pranav",
    passwd = "root",
    database = "Student"
)

myc = db.cursor()
# myc.execute("CREATE DATABASE Student")
# myc.execute("SHOW DATABASES")
# a= myc.fetchall()
# for i in range(len(a)):
#     print(a[i])
# myc.execute("CREATE TABLE Sudent_details(Name VARCHAR(50), Hobby VARCHAR(20), age smallint, Gender CHAR(12), Matric int PRIMARY KEY, marks int, Pincode int)")
while True:
    Name = input("Name: ")
    Hobby = input("HOBBY: ")
    age = int(input("age: "))
    Gender = input("Gender(M,F,N): ")
    Matric = int(input("roll number: "))
    marks = int(input("marks: "))
    pincode = int(input("Pincode: "))
    myc.execute("INSERT INTO Sudent_details(Name, Hobby, age, Gender, Matric, marks, Pincode) VALUES(%s,%s,%s,%s,%s,%s,%s)" ,(Name,Hobby,age,Gender,Matric,marks,pincode))
    db.commit()
    cont = input("Continue(Y/n): ")
    if cont.lower()=="n":
        break
