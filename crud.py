import sqlite3

conn = sqlite3.connect("database.db", timeout=50)
db = conn.cursor()
try:
    sqliteConnection = sqlite3.connect('database.db', check_same_thread=False)
    db = sqliteConnection.cursor()
    #print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    db.execute(sqlite_select_Query)
    record = db.fetchall()
    #print("SQLite Database Version is: ", record)
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

# Created a table one time use
db.execute("""CREATE TABLE city (name varchar(255))""")
print("table successfull")


for i in range(5):
    city = input("Input: ")
    print(city)
    db.execute("INSERT INTO city ?", city)
