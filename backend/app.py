from flask import Flask, jsonify, render_template, request
from backend.routes.quiz_routes import quiz_routes
from backend.routes.auth_routes import auth_routes
from backend.database import db

# ✅ 1. CREAR APP PRIMERO
app = Flask(__name__)

# CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# DB INIT
db.init_app(app)

# ✅ 2. RUTAS DESPUÉS

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nickname = data.get("nickname")

    return jsonify({
        "player_id": nickname
    })

@app.route("/")
def index():
    return render_template("index.html")

# BLUEPRINTS
app.register_blueprint(quiz_routes)
app.register_blueprint(auth_routes)

# CREAR DB
with app.app_context():
    db.create_all()

# RUN
if __name__ == "__main__":
    
    app.run(debug=True)