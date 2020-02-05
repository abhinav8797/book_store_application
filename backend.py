import sqlite3

class Database:

    def __init__(self,db):
        self.conn =sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(" CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY,title text, author text, year integer, isbn integer)")
        self.conn.commit()
        print("database connected")

    def insert(self,title,author,year,isbn):
        self.cur.execute(" INSERT INTO bookstore VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self. conn.commit()

    def view(self):
        self.cur.execute(" SELECT * FROM bookstore")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute(" SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM bookstore WHERE id=? ",(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()
         
    
