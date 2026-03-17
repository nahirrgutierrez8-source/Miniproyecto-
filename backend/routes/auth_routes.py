from flask import Blueprint, request, jsonify
from backend.database import db
from backend.models.player import Player

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/login", methods=["POST"])
def login():

    data = request.json
    nickname = data.get("nickname")

    player = Player.query.filter_by(nickname=nickname).first()

    if not player:
        player = Player(nickname=nickname)
        db.session.add(player)
        db.session.commit()

    return jsonify({
        "message": "Login successful",
        "id": player.id,
        "nickname": player.nickname
    })