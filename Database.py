import csv
import sqlite3

def create_table():
    conn = sqlite3.connect("data/pokemon.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS  Pokemon (
        PokedexNumber TEXT,
        Pokemon TEXT,
        CatchRate TEXT,
        HP TEXT,
        Male TEXT,
        Female TEXT,
        WildLocation TEXT
        )
        """
        )
    conn.commit()
    conn.close()

def search(Name):
    conn = sqlite3.connect("data/pokemon.db")
    c = conn.cursor()
    c.execute(f"SELECT rowid, * FROM Pokemon WHERE Pokemon='{Name}' ")
    result=c.fetchall()
    conn.commit()
    conn.close()
    return result

def searchAll(Location,Name):
    conn = sqlite3.connect("data/pokemon.db")
    c = conn.cursor()
    c.execute(f"SELECT rowid, * FROM Pokemon WHERE Pokemon IS NOT '{Name}' AND WildLocation LIKE '%{Location}%'")
    result=c.fetchall()
    conn.commit()
    conn.close()
    return result

def fromCSV():
    conn=sqlite3.connect("data/pokemon.db")
    c = conn.cursor()
    with open('data/pokemon.csv','r') as f:
        dr=csv.DictReader(f)
        to_db=[(i['#'],i['Name'],i['Catch Rate'],i['HP'],i['Male'],i['Female'],i['Location']) for i in dr]
    c.executemany("INSERT INTO Pokemon VALUES(?, ?, ?, ?, ?, ?, ?)",to_db)
    conn.commit()
    conn.close()

def delete_table():
    conn=sqlite3.connect("data/pokemon.db")
    c = conn.cursor()
    c.execute("DROP TABLE Pokemon")
    conn.commit()
    conn.close()

delete_table()
create_table()
fromCSV()
