from backend.database import Database

class ScoreManager:
    def __init__(self):
        self.db = Database()

    def add_score(self, username, score):
        self.db.insert_score(username, score)

    def get_scores(self):
        return self.db.get_scores()

    def close(self):
        self.db.close()

