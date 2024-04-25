import sqlite3
import os
from tempfile import gettempdir

class UserLoginDB:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def insert_user(self, username, password):
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        self.cursor.execute(query, (username, password))
        self.connection.commit()

    def search_user_by_username(self, username):
        query = "SELECT * FROM users WHERE username = ?"
        self.cursor.execute(query, (username,))
        return self.cursor.fetchone()

    def delete_user_by_username(self, username):
        query = "DELETE FROM users WHERE username = ?"
        self.cursor.execute(query, (username,))
        self.connection.commit()

    def validate_user_login(self, username, password):
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
        return self.cursor.fetchone() is not None

    def close_connection(self):
        self.connection.close()
`