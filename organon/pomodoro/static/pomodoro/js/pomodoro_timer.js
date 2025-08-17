const timerEl = document.getElementById("timer");
const statusEl = document.getElementById("status");
const sessionCountEl = document.getElementById("session-count");

let focusedTime, breakTime;
let intervalId;

// Buscar dados do timer
async function fetchTimerData(id) {
    try {
        const res = await fetch(`/pomodoro/api/${id}`, {
            headers: { 'Accept': 'application/json' }
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return await res.json();
    } catch (e) {
        console.error("Erro na requisição:", e);
        statusEl.textContent = "Erro ao carregar dados.";
        return null;
    }
}

function renderTimer(segundos, mensagem) {
    const minutos = Math.floor(segundos / 60);
    const seg = segundos % 60;
    timerEl.textContent = 
        String(minutos).padStart(2, "0") + ":" + String(seg).padStart(2, "0");
    sessionCountEl.textContent = mensagem;
}

function startFocus() {
    statusEl.textContent = "Foco!";
    intervalId = setInterval(() => {
        focusedTime--;
        if (focusedTime < 0) {
            clearInterval(intervalId);
            startBreak();
        } else {
            renderTimer(focusedTime, "Está na hora de focar!");
        }
    }, 1000);
}

function startBreak() {
    statusEl.textContent = "Descanso!";
    intervalId = setInterval(() => {
        breakTime--;
        if (breakTime < 0) {
            clearInterval(intervalId);
            startFocus();
        } else {
            renderTimer(breakTime, "Recarregando as energias...");
        }
    }, 1000);
}

async function initTimer() {
    const timerId = document.getElementById("timer").dataset.timerId;
    const dados = await fetchTimerData(timerId);
    if (!dados) return;

    focusedTime = dados.focused_time * 60;
    breakTime = dados.break_time * 60;

    startFocus();
}

initTimer();
