// Elementos do DOM
const subtaskSectionEl = document.getElementById("subtask-section");
const subtaskFormsEl = document.getElementById("subtask-forms");
const addSubtaskButton = document.getElementById("add-subtask");

// Busca os dados da subtask via API
async function fetchSubtaskForm() {
    try {
        const res = await fetch("/task/new-subtask", {
            headers: { 'Accept': 'application/json' }
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return await res.json();
    } catch (e) {
        console.error("Erro na requisição:", e);
        return null;
    }
}

// Adiciona o formulário de subtarefa ao DOM
addSubtaskButton.addEventListener("click", async () => {
    const data = await fetchSubtaskForm();
    if (data && data.form_html) {
        subtaskFormsEl.insertAdjacentHTML("beforeend", data.form_html);
        subtaskSectionEl.style.display = "block";
    }
});

// Remove uma subtarefa ao clicar no botão "Remover"
subtaskFormsEl.addEventListener("click", (e) => {
    if (e.target.classList.contains("remove-subtask")) {
        const subtaskFormEl = e.target.closest(".subtask-form");
        subtaskFormEl.remove();

        if (!subtaskFormsEl.hasChildNodes()) {
            subtaskSectionEl.style.display = "none";
        }
    }
});

// Inicializa a visibilidade da seção de subtarefas
document.addEventListener("DOMContentLoaded", () => {
    if (!subtaskFormsEl.hasChildNodes()) {
        subtaskSectionEl.style.display = "none";
    }
});