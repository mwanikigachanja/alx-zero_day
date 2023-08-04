import sqlite3

class Database:
    def __init__(self, db_name="scores.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS scores (username TEXT, score INT)")

    def insert_score(self, username, score):
        self.cursor.execute("INSERT INTO scores VALUES (?, ?)", (username, score))
        self.connection.commit()

    def get_scores(self):
        self.cursor.execute("SELECT * FROM scores")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

