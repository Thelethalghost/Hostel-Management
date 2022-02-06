import mysql.connector as mc
from nameandpass import name,passwd
import startup2

db = mc.connect(
    host = 'localhost',
    user = {name},
    passwd = {passwd}
)

myc = db.cursor()

try:
    myc.execute('CREATE DATABASE Hostels')
    startup2.run()
except Exception:
    print('Database already present\n Run startup2.py')
    #This would be better so that the work is automated.
    startup2.run()

