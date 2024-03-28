import sqlite3
import os

class BookManagementDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, available INTEGER)")

    def add_book(self, title, author):
        self.cursor.execute("INSERT INTO books (title, author, available) VALUES (?, ?, 1)", (title, author))
        self.connection.commit()

    def remove_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        self.connection.commit()

    def borrow_book(self, book_id):
        self.cursor.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
        self.connection.commit()

    def return_book(self, book_id):
        self.cursor.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))
        self.connection.commit()

    def search_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        return books

    def close_connection(self):
        self.connection.close()
        os.remove(self.db_name)
