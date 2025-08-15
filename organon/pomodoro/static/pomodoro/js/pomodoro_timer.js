async function fetchTimerData(timerId) {
    try {
        const response = await fetch(`/get-timer/${timerId}`);
        if (!response.ok) throw new Error(`Erro ao buscar dados: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error("Erro na requisição:", error);
        return null;
    }
}

// Atualiza o UI para modo Foco
function displayFocusMode(sessionsRemaining, focusedTime) {
    const status = document.getElementById("status");
    const timerElement = document.getElementById("timer");
    const sessionsElement = document.getElementById("session-count");

    status.innerHTML = "Está na hora de focar!";
    timerElement.innerHTML = focusedTime;
    sessionsElement.innerHTML = sessionsRemaining;
}

// Atualiza o UI para modo Pausa
function displayBreakMode(sessionsRemaining, breakTime) {
    const status = document.getElementById("status");
    const timerElement = document.getElementById("timer");
    const sessionsElement = document.getElementById("sessions-count");

    status.innerHTML = "Recarregando as energias!";
    timerElement.innerHTML = breakTime;
    sessionsElement.innerHTML = sessionsRemaining;
}

// Controla a lógica do timer
async function loadTimer(timerId) {
    const dados = await fetchTimerData(timerId);
    if (!dados) return;

    // Exibe dados iniciais
    displayFocusMode(dados.focused_time);

    // Exemplo: caso queira alternar depois
    // displayBreakMode(dados.sessions - 1, dados.break_time);
    displayBreakMode(dados.sessions - 1, dados.break_time)
}

// Inicializa o script
document.addEventListener("DOMContentLoaded", () => {
    const timerElement = document.getElementById("timer");
    if (timerElement && timerElement.dataset.timerId) {
        loadTimer(timerElement.dataset.timerId);
    }
});
