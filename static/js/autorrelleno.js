document.addEventListener("DOMContentLoaded", function () {
    // Definir los colores originales de los campos del formulario
    const originalColor = 'rgba(255, 255, 255, 0.1)';
    const originalBorderColor = 'rgba(255, 255, 255, 0.3)';
    const originalBorderFocusColor = 'rgba(255, 255, 255, 0.6)';
    
    // Obtener todos los campos de entrada y textarea
    const inputs = document.querySelectorAll('.campoForm input, .campoForm textarea');
    
    // Función para restablecer los colores
    function resetFieldColors() {
      inputs.forEach(input => {
        // Restablecer fondo y borde a los valores originales
        if (input.value === "") { // Solo cambiar si no hay valor (cuando el campo no está autocompletado)
          input.style.backgroundColor = originalColor;
          input.style.borderColor = originalBorderColor;
        }
      });
    }
  
    // Observador para detectar cambios en los campos (para autorrelleno)
    const observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
        if (mutation.attributeName === "value") {
          resetFieldColors();
        }
      });
    });
  
    // Configurar el observador para observar cambios en los valores de los campos
    inputs.forEach(input => {
      observer.observe(input, {
        attributes: true,
        attributeFilter: ['value']
      });
    });
  
    // Restablecer los colores cada vez que un campo gane o pierda el foco
    inputs.forEach(input => {
      input.addEventListener('focus', function() {
        input.style.borderColor = originalBorderFocusColor; // Cambio al color de foco
      });
  
      input.addEventListener('blur', function() {
        // Al perder el foco, se reestablece el color original si está vacío
        if (input.value === "") {
          input.style.backgroundColor = originalColor;
          input.style.borderColor = originalBorderColor;
        }
      });
    });
  });
  