document.addEventListener("DOMContentLoaded", function () {
  const numPersonasInput = document.getElementById("num_personas");
  const errorModal = document.getElementById("error-modal");
  const modalMessage = document.getElementById("modal-mensaje");
  const aceptarModalButton = document.getElementById("close-modal"); // El botón "Cerrar"

  // Muestra el modal cuando el valor sea menor a 6
  numPersonasInput.addEventListener("change", function () {
    if (parseInt(numPersonasInput.value) < 6 && numPersonasInput.value !== '') {
      // Establece el mensaje de error
      modalMessage.textContent = "El número de personas mínimo es de 6.";
      errorModal.style.display = "block"; // Muestra el modal de error
    }
  });

  aceptarModalButton.addEventListener("click", () => {
    errorModal.style.display = "none";
  })


});
