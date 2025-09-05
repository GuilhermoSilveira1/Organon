// Elementos do DOM
const timerEl = document.getElementById("timer");
const statusEl = document.getElementById("status");
const sessionCountEl = document.getElementById("session-count");
const playPauseBtn = document.getElementById("play-pause");

// Variáveis de controle
let focusedTime, breakTime, sessionsLeft;
let internalFocusedTime, internalBreakTime;
let intervalId;
let isPaused = false;

// Atualiza a interface do usuário
function updateUI({ statusMsg = "", timerSeconds = 0, sessions = null }) {
    if (statusMsg) statusEl.textContent = statusMsg;
    if (sessions !== null) sessionCountEl.textContent = sessions;
    renderTimer(timerSeconds);
}

// Renderiza o tempo no formato MM:SS
function renderTimer(segundos) {
    const minutos = Math.floor(segundos / 60);
    const seg = segundos % 60;
    timerEl.textContent = 
        String(minutos).padStart(2, "0") + ":" + String(seg).padStart(2, "0");
}

// Busca os dados do timer via API
async function fetchTimerData(id) {
    try {
        const res = await fetch(`/pomodoro/api/${id}`, {
            headers: { 'Accept': 'application/json' }
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return await res.json();
    } catch (e) {
        console.error("Erro na requisição:", e);
        updateUI({ statusMsg: "Erro ao carregar dados." });
        return null;
    }
}

// Inicia o ciclo de foco
function startFocus() {
    internalFocusedTime = focusedTime;
    updateUI({ statusMsg: "Está na hora de focar!", timerSeconds: internalFocusedTime, sessions: sessionsLeft });

    intervalId = setInterval(() => {
        if (!isPaused) {
            internalFocusedTime--;
            if (internalFocusedTime < 0) {
                clearInterval(intervalId);
                startBreak();
            } else {
                updateUI({ timerSeconds: internalFocusedTime });
            }
        }
    }, 1000);
}

// Inicia o ciclo de descanso
function startBreak() {
    internalBreakTime = breakTime;
    updateUI({ statusMsg: "Recarregando as energias...", timerSeconds: internalBreakTime, sessions: sessionsLeft });

    intervalId = setInterval(() => {
        if (!isPaused) {
            internalBreakTime--;
            if (internalBreakTime < 0) {
                clearInterval(intervalId);
                sessionsLeft--;
                if (sessionsLeft > 0) {
                    startFocus();
                } else {
                    updateUI({ statusMsg: "Sessões concluídas! Parabéns!", timerSeconds: 0, sessions: 0 });
                }
            } else {
                updateUI({ timerSeconds: internalBreakTime });
            }
        }
    }, 1000);
}

// Lógica do botão play/pause
playPauseBtn.textContent = "⏸️"; // Começa como "Pause"
playPauseBtn.addEventListener("click", () => {
    isPaused = !isPaused;
    playPauseBtn.textContent = isPaused ? "▶️" : "⏸️";
});

// Inicializa o timer ao carregar a página
document.addEventListener('DOMContentLoaded', async () => {
    const timerId = timerEl.dataset.timerId;
    const dados = await fetchTimerData(timerId);
    if (!dados) return;

    focusedTime = dados.focused_time * 60;
    breakTime = dados.break_time * 60;
    sessionsLeft = dados.sessions;

    if (sessionsLeft > 0) {
        startFocus();
    } else {
        updateUI({ statusMsg: "Nenhuma sessão restante.", timerSeconds: 0, sessions: 0 });
    }
});