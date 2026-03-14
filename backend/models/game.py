from backend.database import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer)
    score = db.Column(db.Integer)