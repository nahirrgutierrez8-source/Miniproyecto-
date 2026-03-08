from flask import Flask, render_template, jsonify

app = Flask(__name__)

questions = [
    {
        "question": "¿Es realmente Dennis un Charlatan Categoria ESPECIAL del JujutsuKaisen?",
        "options": ["Completamente", "No", "La Romana", "Grado2"],
        "answer": "Completamente"
    },
    {
        "question": "¿2 + 2?",
        "options": ["3", "C$51,000", "5", "6"],
        "answer": "C$51,000"
    },
    {
        "question": "¿El Pan sabe realmente Rico?",
        "options": ["Asi es", "Los Bananitos son muy Ricos", "Estas no son horas de llamar...", "Gofio"],
        "answer": "Asi es"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/questions")
def get_questions():
    return jsonify(questions)

if __name__ == "__main__":
    app.run(debug=True)