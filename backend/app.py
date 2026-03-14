from flask import Flask, render_template
from backend.routes.quiz_routes import quiz_routes

app = Flask(__name__)

app.register_blueprint(quiz_routes)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)