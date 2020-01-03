import os
import sqlite3


"""def counter():
    if not os.path.exists("data/counter.txt"):
        count = open("data/counter.txt", 'w')
        count.write(str(1))
        count.close()
    else:
        count = open("data/counter.txt", 'r')
        c = int(count.read())
        c += 1
        countmore = open("data/counter.txt", 'w')
        countmore.write(str(c))
        return c
"""        

def save(*data):
    conn = sqlite3.connect("data/database.db")
    # Create a table    
    c = conn.cursor()
    #c.execute('''CREATE TABLE contacto (name text, address text, phone text, email text)''')
    # Insert a row of data
    c.execute("INSERT INTO contacto VALUES (?,?,?,?)", data)
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def update(parameter_list):
    pass


def delete(self, parameter_list):
    pass


def listing():
    conn = sqlite3.connect("data/database.db")
    c = conn.cursor()
    c.execute('SELECT * FROM contacto')
    return c.fetchall() 


def get(parameter_list):
    pass


def sorting(self, parameter_list):
    pass 