import sqlite3

mydb = sqlite3.connect("Database.db")
myCursor = mydb.cursor()

def Add(title,description):
    myCursor.execute(f'INSERT INTO Tasks(Title, Description) VALUES("{title}","{description}")')
    mydb.commit()

def Delete(d):
    myCursor.execute(f'DELETE FROM Tasks WHERE Title = "{d}"')
    mydb.commit()

def GetAll():
    myCursor.execute("SELECT * FROM Tasks")
    result = myCursor.fetchall()
    return result