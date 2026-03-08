let questions = []
let currentQuestion = 0
let score = 0

async function loadQuestions(){

    const response = await fetch("/questions")

    questions = await response.json()

    showQuestion()

}

function showQuestion(){

    const q = questions[currentQuestion]

    document.getElementById("question").innerText = q.question

    const answersDiv = document.getElementById("answers")

    answersDiv.innerHTML = ""

    q.options.forEach(option => {

        const btn = document.createElement("button")

        btn.innerText = option

        btn.onclick = () => checkAnswer(option)

        answersDiv.appendChild(btn)

        answersDiv.appendChild(document.createElement("br"))

    })

}

function checkAnswer(option){

    if(option === questions[currentQuestion].answer){

        score++

    }

}

function nextQuestion(){

    currentQuestion++

    if(currentQuestion < questions.length){

        showQuestion()

    }
    else{

        document.getElementById("quiz").innerHTML =
        "<h2>Tu puntaje: " + score + "</h2>"

    }

}

window.onload = loadQuestions   