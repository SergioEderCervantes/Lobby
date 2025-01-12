document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("reservation-form");
    const fields = form.querySelectorAll(".campoForm");
  
    // Mostrar el primer campo visible
    //fields[0].classList.add("visible");
  
    // Validar la fecha
    const inputFecha = fields[0].querySelector("input, textarea");
    inputFecha.addEventListener("input", function () {
        if (inputFecha.value.trim() !== "") {
            fields[1].classList.add("visible");
        } else {
            fields[1].classList.remove("visible");
        }
    });
  
    // Validar la hora
    const inputHora = fields[1].querySelector("input, textarea");
    inputHora.addEventListener("input", function () {
        if (inputHora.value.trim() !== "") {
            fields[2].classList.add("visible");
        } else {
            fields[2].classList.remove("visible");
            document.getElementById("toggle").disabled = false;
        }
    });
  
  
  });
  
  