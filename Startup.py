import mysql.connector as mc
from nameandpass import name,passwd

db = mc.connect(
    host = 'localhost',
    user = {name},
    passwd = {passwd}
)

myc = db.cursor()

try:
    myc.execute('CREATE DATABASE Hostels')
    print('Now run startup2.py')
except Exception:
    print('Database already present\n Run startup2.py')

