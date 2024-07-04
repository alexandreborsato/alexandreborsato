# import sqlite
import sqlite3

# connect to database
conn = sqlite3.connect('cidadaos.db')

# create a cursor
cur = conn.cursor()

# execute a query
cur.execute('SELECT * from cidadaos2')

#print(cur.fetchone())
#print(cur.fetchall())

# fetch all the results
for row in cur.execute('SELECT * FROM cidadaos2'):
    print(row)

# fetch some of the results based on a user input

id = input("Enter the contact id: ")
# execute a query
cur.execute('SELECT * FROM cidadaos2 WHERE id = ?', (id, ))
# cur.execute('SELECT * FROM cidadaos2 WHERE id =', id)
print(cur.fetchone())

# Insert a new cidadao One by one

id = input("Enter the contact id: ")
cpf = input("Enter the contact cpf: ")
namec = input("Enter the contact full name: ")
name1st = input("Enter the contact 1st name: ")
name2nd = input("Enter the contact family name: ")
cur.execute("INSERT INTO cidadaos2 VALUES (?, ?, ?, ?, ?)", (id, cpf, namec, name1st, name2nd))
conn.commit()
print("Record inserted successfully!")

# fetche the new entry
cur.execute('SELECT * FROM cidadaos2 WHERE id = ?', (id, ))
print(cur.fetchone())

# Closing the DB connection
conn.close()
