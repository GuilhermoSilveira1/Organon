const timerEl = document.getElementById("timer");
const statusEl = document.getElementById("status");
const sessionCountEl = document.getElementById("session-count");

let focusedTime, breakTime, sessionsLeft;
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

// Função usada para renderizar o tempo na tela e mostrar o número de sessões
function renderTimer(segundos, mensagem) {
    const minutos = Math.floor(segundos / 60);
    const seg = segundos % 60;
    timerEl.textContent = 
        String(minutos).padStart(2, "0") + ":" + String(seg).padStart(2, "0");
    sessionCountEl.textContent = mensagem;
}

// Função para mostrar o tempo de foco restante, uma mensagem no status e as sessões restantes
function startFocus() {
    statusEl.textContent = "Está na hora de focar!";
    intervalId = setInterval(() => {
        focusedTime--;
        if (focusedTime < 0) {
            clearInterval(intervalId);
            startBreak();
        } else {
            renderTimer(focusedTime, sessionsLeft);
        }
    }, 1000);
}

function startBreak() {
    statusEl.textContent = "Recarregando as energias...";
    intervalId = setInterval(() => {
        breakTime--;
        if (breakTime < 0) {
            clearInterval(intervalId);
            sessionsLeft--;
            startFocus();
        } else {
            renderTimer(breakTime, sessionsLeft);
        }
    }, 1000);
}

/* Nessa função puxa os dados do banco e mostra na tela,
além disso, chama a função para iniciar o tempo de foco*/
async function initTimer() {
    const timerId = document.getElementById("timer").dataset.timerId;
    const dados = await fetchTimerData(timerId);
    if (!dados) return;

    focusedTime = dados.focused_time * 60;
    breakTime = dados.break_time * 60;
    sessionsLeft = dados.sessions

    startFocus();
}

initTimer();
