function mostrarLoader() {
    const loader = document.getElementById('loader');
    loader.style.display = 'flex';
    setTimeout(() => {
        loader.style.display = 'none';
    }, 5000);
}

function ejecutarTodasLasConsultas() {
    mostrarLoader();
    const buttons = document.querySelectorAll('.consulta button');
    const buttonShowAll = document.getElementById("ejecutarTodo");
    setTimeout(() => {
        const resultados = document.querySelectorAll('[id^="resultado"]');
        resultados.forEach((resultado) => {
            resultado.style.display = 'block';
        });
        buttons.forEach((button) => {
            button.textContent = 'Ejecutada';
            button.disabled = true;
        });
        buttonShowAll.textContent = 'Ejecutado';
        buttonShowAll.disabled = true;
    }, 5000);
}

function ejecutarConsulta(claveConsulta, idResultado) {
    const loader = document.getElementById('loader');
    const button = document.querySelector(`button[onclick="ejecutarConsulta('${claveConsulta}', '${idResultado}')"]`);
    loader.style.display = 'flex';
    setTimeout(() => {
        loader.style.display = 'none';
        const resultado = document.getElementById(idResultado);
        resultado.style.display = 'block';
        button.textContent = 'Ejecutada';
        button.disabled = true;
    }, 2000);
}

// Toggle Theme
const body = document.body;
document.getElementById('toggleTheme').addEventListener('click', () => {
    body.classList.toggle('dark-theme');
});
