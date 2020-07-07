import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item Text,Qty INTEGER,price REAL)")
    conn.commit()
    conn.close()

#create_table()

def insert(item,qty,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,qty,price))
    conn.commit()
    conn.close()

#insert('Milk bottle', 5, 6)

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

#print(view())

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def select(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store WHERE item=?",(item,))
    rows=cur.fetchall()
    conn.close()
    return rows

#print(select('Coffee cup'))

def update_qty_price(Qty,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET Qty=?, price=? WHERE item=?",(Qty,price,item))
    conn.commit()
    conn.close()

update_qty_price(10,8.99,'Coffee cup')
print(view())