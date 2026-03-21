from flask import Blueprint, request, jsonify
from backend.models.player import Player
from backend.database import db
import json

quiz_routes = Blueprint("quiz_routes", __name__)

with open("backend/data/questions.json", encoding="utf-8") as f:
    questions = json.load(f)
@quiz_routes.route("/questions")
def get_questions():
    return jsonify(questions)

@quiz_routes.route("/save_score", methods=["POST"])
def save_score():

    data = request.get_json()

    player_id = data.get("player_id")
    score = data.get("score")

    player = Player.query.get(player_id)

    if player:
        player.score = score
        db.session.commit()

    return jsonify({"message": "Score saved"})

@quiz_routes.route("/leaderboard")
def leaderboard():

    players = Player.query.order_by(Player.score.desc()).limit(10).all()

    leaderboard = []

    for player in players:
        leaderboard.append({
            "nickname": player.nickname,
            "score": player.score
        })

    return jsonify(leaderboard)