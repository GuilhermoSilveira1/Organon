document.addEventListener('DOMContentLoaded', function () {
    const addButton = document.getElementById('add-subtask');
    const formContainer = document.getElementById('subtask-forms');
    const totalForms = document.getElementById('id_subtask_set-TOTAL_FORMS');

    function updateRemoveButtons() {
        formContainer.querySelectorAll('.remove-subtask').forEach(button => {
            button.onclick = () => {
                button.closest('.subtask-form').remove();
                updateFormIndices();
            };
        });
    }

    function updateFormIndices() {
        const forms = formContainer.querySelectorAll('.subtask-form');
        forms.forEach((form, index) => {
            form.querySelectorAll('[name], [id], label').forEach(el => {
                if (el.name) el.name = el.name.replace(/subtask_set-\d+-/, `subtask_set-${index}-`);
                if (el.id) el.id = el.id.replace(/subtask_set-\d+-/, `subtask_set-${index}-`);
                if (el.htmlFor) el.htmlFor = el.htmlFor.replace(/subtask_set-\d+-/, `subtask_set-${index}-`);
            });
        });
        totalForms.value = forms.length;
    }

    addButton.addEventListener('click', function () {
        const index = parseInt(totalForms.value);
        fetch('/task/new-subtask/')  // ajuste conforme sua URL
            .then(response => response.json())
            .then(data => {
                const wrapper = document.createElement('div');
                wrapper.innerHTML = data.form_html;
                const form = wrapper.firstElementChild;

                // Atualiza os índices do novo formulário
                form.querySelectorAll('[name], [id], label').forEach(el => {
                    if (el.name) el.name = el.name.replace(/subtask_set-\d+-/, `subtask_set-${index}-`);
                    if (el.id) el.id = el.id.replace(/subtask_set-\d+-/, `subtask_set-${index}-`);
                    if (el.htmlFor) el.htmlFor = el.htmlFor.replace(/subtask_set-\d+-/, `subtask_set-${index}-`);
                });

                formContainer.appendChild(form);
                totalForms.value = index + 1;
                updateRemoveButtons();
            });
    });
});

addButton.addEventListener('click', function () {
    const index = parseInt(totalForms.value);
    fetch('/task/new-subtask/')
        .then(response => response.json())
        .then(data => {
            const wrapper = document.createElement('div');
            wrapper.innerHTML = data.form_html;
            const form = wrapper.firstElementChild;

            form.querySelectorAll('[name], [id], label').forEach(el => {
                if (el.name) el.name = el.name.replace(/subtask_set-\d+-/, `subtask_set-${index}-`);
                if (el.id) el.id = el.id.replace(/subtask_set-\d+-/, `subtask_set-${index}-`);
                if (el.htmlFor) el.htmlFor = el.htmlFor.replace(/subtask_set-\d+-/, `subtask_set-${index}-`);
            });

            formContainer.appendChild(form);
            totalForms.value = index + 1;
            updateRemoveButtons();

            // Mostra a seção de subtarefas se ainda estiver oculta
            const section = document.getElementById('subtask-section');
            if (section.style.display === 'none') {
                section.style.display = 'block';
            }
        });
});
