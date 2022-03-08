import mysql.connector as mc
from nameandpass import name,passwd
import startup2

db = mc.connect(
    host = 'localhost',
    user = name,
    passwd = passwd
)

myc = db.cursor(buffered=True)

try:
    myc.execute('CREATE DATABASE Hostels_Management')
    startup2.run()
except Exception:
    startup2.run()

