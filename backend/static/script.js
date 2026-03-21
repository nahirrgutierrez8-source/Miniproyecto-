let questions = []
let currentQuestion = 0
let score = 0
let player_id = null;


// LOGIN
async function login() {

    console.log("Botón presionado");
    
    const nickname = document.getElementById("nickname").value;

    if (!nickname) {
    alert("Escribe un nickname");
    return;
}

    const response = await fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ nickname })
    });

    const data = await response.json();

    player_id = data.player_id;

    document.getElementById("login-container").style.display = "none";
    document.getElementById("quiz-container").style.display = "block";

    loadQuestions();
}


// CARGAR PREGUNTAS
async function loadQuestions(){

    const response = await fetch("/questions")
    questions = await response.json()   
    
    showQuestion()

}


// MOSTRAR PREGUNTA
function showQuestion(){

    const q = questions[currentQuestion]

    document.getElementById("question").innerText = q.question

    const optionsDiv = document.getElementById("options") 

    optionsDiv.innerHTML = ""

    q.options.forEach(option => {

        const btn = document.createElement("button")

        btn.innerText = option

        btn.onclick = () => checkAnswer(option)

        optionsDiv.appendChild(btn)

    })

}


// VALIDAR RESPUESTA
function checkAnswer(option){

    const correct = questions[currentQuestion].answer;

    const buttons = document.querySelectorAll("#options button");

    buttons.forEach(btn => {

        if(btn.innerText === correct){
            btn.style.backgroundColor = "green";
            btn.style.color = "white";
        }

        if(btn.innerText === option && option !== correct){
            btn.style.backgroundColor = "red";
            btn.style.color = "white";
        }

        btn.disabled = true;
    });

    if(option === correct){
        score++;
    }
    setTimeout(() => {
    nextQuestion();
}, 1000);
}


// SIGUIENTE PREGUNTA
function nextQuestion(){

    currentQuestion++

    if(currentQuestion < questions.length){

        showQuestion()

    }
    else{

        document.getElementById("quiz-container").innerHTML =
"<h2 class='result'>🏆 Puntaje final: " + score + "</h2>";

    }

}
