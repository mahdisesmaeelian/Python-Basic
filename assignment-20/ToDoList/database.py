import sqlite3

mydb = sqlite3.connect("Mydatabase.db")
myCursor = mydb.cursor()

def Add(title,description):
    myCursor.execute(f'INSERT INTO Tasks(Title, Description) VALUES("{title}","{description}")')
    mydb.commit()

def Delete(d):
    myCursor.execute(f'DELETE FROM Tasks WHERE Title = "{d}"')
    mydb.commit()

def CheckforDone(d,t,a):
    if d == 0 or d == None:
        myCursor.execute(f'UPDATE Tasks SET Done = 1 WHERE Title = "{t}"')
        print('done')
    else:
        myCursor.execute(f'UPDATE Tasks SET Done = 0 WHERE Title = "{t}"')
        print('undone')
    mydb.commit()

def GetAll():
    myCursor.execute("SELECT * FROM Tasks")
    result = myCursor.fetchall()
    return result