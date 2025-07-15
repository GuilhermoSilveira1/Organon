let timer;
let isPaused = false;
let currentPhase = 'focus';
let timeLeft = focusedTime;

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('session-count').textContent = sessionsRemaining;
    document.getElementById('status').textContent = 'Hora de focar!';
    updateDisplay();
    startTimer();
});

function updateDisplay() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    document.getElementById('timer').textContent =
        `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

function switchPhase() {
    if (currentPhase === 'focus') {
        currentPhase = 'break';
        timeLeft = breakTime;
        document.getElementById('status').textContent = 'Hora da pausa!';
    } else {
        sessionsRemaining--;
        document.getElementById('session-count').textContent = sessionsRemaining;
        if (sessionsRemaining > 0) {
            currentPhase = 'focus';
            timeLeft = focusedTime;
            document.getElementById('status').textContent = 'Hora de focar!';
        } else {
            clearInterval(timer);
            document.getElementById('status').textContent = 'Todas as sessões concluídas!';
            return;
        }
    }
}

function tick() {
    if (!isPaused) {
        if (timeLeft > 0) {
            timeLeft--;
            updateDisplay();
        } else {
            switchPhase();
        }
    }
}

function startTimer() {
    clearInterval(timer);
    timer = setInterval(tick, 1000);
}

function togglePauseResume() {
    const button = document.querySelector('.control-buttons button');
    isPaused = !isPaused;
    button.textContent = isPaused ? 'Resume' : 'Pause';
    if (!isPaused) startTimer();
}

function restartTimer() {
    clearInterval(timer);
    currentPhase = 'focus';
    timeLeft = focusedTime;
    isPaused = false;
    document.getElementById('status').textContent = 'Hora de focar!';
    document.getElementById('session-count').textContent = sessionsRemaining;
    updateDisplay();
    startTimer();
}
