from flask import Blueprint, jsonify
import json

quiz_routes = Blueprint("quiz_routes", __name__)

with open("backend/data/questions.json", encoding="utf-8") as f:
    questions = json.load(f)

@quiz_routes.route("/questions")
def get_questions():
    return jsonify(questions)