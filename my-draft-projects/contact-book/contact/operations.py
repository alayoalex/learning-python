import os
import sqlite3


def create_database():
    fl = open("data/book.db", "w")
    fl.close()
    conn = sqlite3.connect("data/book.db")
    c = conn.cursor()
    c.executescript("resources/Contact-Book-Crear.ddl")
    conn.commit()
    conn.close()

def save(data):
    conn = sqlite3.connect("data/book.db")
    # Create a table    
    c = conn.cursor()
    #c.execute('''CREATE TABLE contacto (name text, address text, phone text, email text)''')
    # Insert a row of data
    c.execute("INSERT INTO contacto VALUES (?,?,?)", data)
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


def get_by_name(parameter):
    conn = sqlite3.connect("data/database.db")
    c = conn.cursor()
    c.execute('SELECT * FROM contacto WHERE name=?', parameter)
    return c.fetchall() 

def get_by_mobile(parameter):
    conn = sqlite3.connect("data/database.db")
    c = conn.cursor()
    c.execute('SELECT * FROM contacto WHERE phone=?', parameter)
    return c.fetchall() 


def sorting(self, parameter_list):
    pass 