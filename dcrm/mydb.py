import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

# prepare cursor object
cursorObject = dataBase.cursor();

# create db
cursorObject.execute('CREATE DATABASE dcrm')

print('All done!')