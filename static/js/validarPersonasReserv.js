document.addEventListener("DOMContentLoaded", function () {
    const numPersonasInput = document.getElementById("num_personas");
    const errorModal = document.getElementById("error-modal");
    const modalMessage = document.getElementById("modal-mensaje");
    const aceptarModalButton = document.getElementById("close-modal"); // El botón "Cerrar"
  
    // Muestra el modal cuando el valor sea menor a 6
    numPersonasInput.addEventListener("input", function () {
      if (parseInt(numPersonasInput.value) < 6 && numPersonasInput.value !== '') {
        // Establece el mensaje de error
        modalMessage.textContent = "El número de personas mínimo es de 6."; 
        errorModal.style.display = "block"; // Muestra el modal de error
      }
    });
  
    numPersonasInput.addEventListener("keydown", function (event) {
      if (event.key === "Enter") {
        if (parseInt(numPersonasInput.value) < 6) {
          event.preventDefault(); // Evita que se envíe el formulario si el valor es inválido
          // Muestra el modal si el valor es menor que 6
          modalMessage.textContent = "El número de personas mínimo es de 6."; 
          errorModal.style.display = "block"; // Muestra el modal de error
        }
      }
    });

  });
  