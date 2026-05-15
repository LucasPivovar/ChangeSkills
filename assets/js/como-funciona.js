document.addEventListener('DOMContentLoaded', () => {
    const inputs = document.querySelectorAll('input[name="carga"], input[name="modalidade"], #select-dia, #input-horario, #is-kids');
    const resumoModalidade = document.getElementById('resumo-modalidade');
    const resumoCarga = document.getElementById('resumo-carga');
    const resumoHorario = document.getElementById('resumo-horario');
    const statusMsg = document.getElementById('horario-status');

    function updateSummary() {
        const cargaElement = document.querySelector('input[name="carga"]:checked');
        const modalidadeElement = document.querySelector('input[name="modalidade"]:checked');
        const diaElement = document.getElementById('select-dia');
        const horarioElement = document.getElementById('input-horario');
        const isKidsElement = document.getElementById('is-kids');

        if (!cargaElement || !modalidadeElement || !diaElement || !horarioElement) return;

        const carga = cargaElement.value;
        const modalidade = modalidadeElement.value;
        const dia = diaElement.value;
        const horario = horarioElement.value;
        const isKids = isKidsElement.checked;

        resumoCarga.innerText = carga === "1 hora / semana" ? "1h / semana" : "2h / semana";
        resumoModalidade.innerText = modalidade;
        resumoHorario.innerText = `${dia} • ${horario}`;

        // Validação simples de horário
        const [hours, minutes] = horario.split(':').map(Number);
        let valid = true;
        let msg = "Horário válido ✅";

        if (dia === 'Sábado') {
            if (hours < 8 || hours >= 16) {
                valid = false;
                msg = "Fora do horário (Sáb: 08:00–16:00) ❌";
            }
        } else {
            if (hours < 7 || hours >= 22) {
                valid = false;
                msg = "Fora do horário (07:00–22:00) ❌";
            }
        }

        if (isKids && hours >= 20) {
            valid = false;
            msg = "Aulas kids somente até 20:00 ❌";
        }

        if (statusMsg) {
            statusMsg.innerText = msg;
            statusMsg.className = valid ? "status-msg valid" : "status-msg invalid";
        }
    }

    inputs.forEach(input => input.addEventListener('change', updateSummary));
    const inputHorario = document.getElementById('input-horario');
    if (inputHorario) {
        inputHorario.addEventListener('input', updateSummary);
    }
    
    updateSummary();
});
