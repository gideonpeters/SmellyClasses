import sqlite3

class StudentDatabaseProcessor:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_student_table(self):
        conn = sqlite3.connect(self.database_name)
        conn.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        gender TEXT NOT NULL,
                        grade INTEGER NOT NULL
                        )''')
        conn.commit()
        conn.close()

    def insert_student(self, student_data):
        conn = sqlite3.connect(self.database_name)
        conn.execute("INSERT INTO students (name, age, gender, grade) VALUES (?, ?, ?, ?)",
                     (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
        conn.commit()
        conn.close()

    def search_student_by_name(self, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name=?", (name,))
        result = cursor.fetchall()
        conn.close()
        return result

    def delete_student_by_name(self, name):
        conn = sqlite3.connect(self.database_name)
        conn.execute("DELETE FROM students WHERE name=?", (name,))
        conn.commit()
        conn.close()
