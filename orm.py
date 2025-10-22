import sqlite3

class DBclient():
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.close = self.conn.close()
    
    def insert(self, query, data):
        try:
            self.cursor.manyexecute(query, data)
        except Error:
            print("error")


    def update(self, query):
        try:
            self.cursor.execute(query)
        except Error:
            print("Error")

    def delete(self, query):
        try:
            self.cursor.execute(query)
        except Error:
            print("error")

    def get_by_one(self):
        try:
            print(self.cursor.fetchall())
        except Error:
            print("error")

    def get_all(self):
        print(row for row in self.cursor.fetchall())

