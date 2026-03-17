from flask import Flask, render_template
from backend.routes.quiz_routes import quiz_routes
from backend.routes.auth_routes import auth_routes
from backend.database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(quiz_routes)
app.register_blueprint(auth_routes)

with app.app_context():
    db.create_all()
    
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)