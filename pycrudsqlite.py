import sqlite3
from tkinter import *

iid=0
iname=""
iage=0
iemail=""

# Function to create a SQLite database and table
def create_database():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS records
                 (id INTEGER PRIMARY KEY,
                 name TEXT,
                 age INTEGER,
                 email TEXT)''')
    conn.commit()
    conn.close()

# Function to insert a new record into the database
def insert_record():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO records (id, name, age, email) VALUES (?, ?, ?, ?)",
              (id_entry.get(), name_entry.get(), age_entry.get(), email_entry.get()))
    conn.commit()
    conn.close()
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    email_entry.delete(0, END)
    id_entry.delete(0, END)

# Function to update an existing record in the database
def update_record():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("UPDATE records SET name=?, age=?, email=? WHERE id=?",
              (name_entry.get(), age_entry.get(), email_entry.get(), id_entry.get()))

    conn.commit()
    conn.close()
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    email_entry.delete(0, END)
    
    
# Function to delete a record from the database
def delete_record():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("DELETE FROM records WHERE id=?", (id_entry.get(),))
    conn.commit()
    conn.close()
    id_entry.delete(0, END)

# Function to list all records on the screen
def list_records():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM records")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Function to print the database content
def print_database_content():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM records")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Create the database and table if they don't exist
create_database()

# Create the GUI
root = Tk()

# Labels
Label(root, text="Your ID:").grid(row=0)
Label(root, text="Your Name:").grid(row=1)
Label(root, text="Your Age:").grid(row=2)
Label(root, text="Your Email:").grid(row=3)


# Entry fields
id_entry = Entry(root)
name_entry = Entry(root)
age_entry = Entry(root)
email_entry = Entry(root)

id_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
age_entry.grid(row=2, column=1)
email_entry.grid(row=3, column=1)

# Buttons
Button(root, text="Insert", command=insert_record).grid(row=7, column=0, pady=10)
Button(root, text="Update", command=update_record).grid(row=7, column=1, pady=10)
Button(root, text="Delete", command=delete_record).grid(row=7, column=2, pady=10)
Button(root, text="List Records", command=list_records).grid(row=8, column=0, pady=10)
Button(root, text="Print Database Content", command=print_database_content).grid(row=8, column=1, pady=10)

root.mainloop()
