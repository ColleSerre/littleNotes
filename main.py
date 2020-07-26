import sqlite3
from sqlite3 import Error

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("/home/darenpalmer/todoApp/notes.db")
        print("CONNECTED...")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS notes (title text, body text)")
        return connection
    except Error as e:
        print(f"Error: {e}")


def printNotes():
    try:
        cursor.execute("SELECT * FROM notes")
        for i in cursor.fetchall():
            print(i)
        count = cursor.lastrowid
        if count == 1:
            print("You have 1 note...")
        else:
            print(f"You have {count} notes...")
    except Error as e:
        print(f"{e}")


def insertNote(title, body):
    try:
        cursor.execute("INSERT INTO notes VALUES ('{}','{}')".format(title, body))
        connection.commit()
        print("NOTE ADDED !")
    except Error as e:
        print(f"Error: {e}")


def clearNotes():
    try:
        cursor.execute("DELETE FROM notes;")
        connection.commit()
        print("NOTES CLEARED...")
    except Error as e:
        print(f"Error: {e}")



connection = create_connection()
cursor = connection.cursor()
insertNote(input("Enter note title: "), input("Enter note body: "))
printNotes()
if input("delete all ? ").lower() == "y":
    clearNotes()
