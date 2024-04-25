import sqlite3

class DatabaseProcessor:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_table(self, table_name, *columns):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE {table_name} ({', '.join(columns)})")
        conn.commit()
        conn.close()

    def insert_into_database(self, table_name, data):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        for entry in data:
            cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?)", (entry['name'], entry['age']))
        conn.commit()
        conn.close()

    def search_database(self, table_name, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name} WHERE name=?", (name,))
        result = cursor.fetchall()
        conn.close()
        return result

    def delete_from_database(self, table_name, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE name=?", (name,))
        conn.commit()
        conn.close()
