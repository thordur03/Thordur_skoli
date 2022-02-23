import mysql.connector

mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd = "password123"
                                )

my_cursor = mydb.cursor()


# my_cursor.execute("DROP DATABASE flask_database") # til þess að reseta databaseið 
my_cursor.execute("CREATE DATABASE flask_database")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
