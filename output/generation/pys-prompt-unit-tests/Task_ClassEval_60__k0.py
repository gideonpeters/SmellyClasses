import sqlite3

class MovieTicketDB:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                movie TEXT,
                cinema TEXT,
                seat TEXT,
                customer TEXT
            )
        ''')
        self.connection.commit()

    def insert_ticket(self, movie, cinema, seat, customer):
        self.cursor.execute('''
            INSERT INTO tickets (movie, cinema, seat, customer)
            VALUES (?, ?, ?, ?)
        ''', (movie, cinema, seat, customer))
        self.connection.commit()

    def search_tickets_by_customer(self, customer):
        self.cursor.execute('''
            SELECT * FROM tickets WHERE customer = ?
        ''', (customer,))
        return self.cursor.fetchall()

    def delete_ticket(self, ticket_id):
        self.cursor.execute('''
            DELETE FROM tickets WHERE id = ?
        ''', (ticket_id,))
        self.connection.commit()
