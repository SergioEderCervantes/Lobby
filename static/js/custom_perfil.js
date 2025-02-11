// Previsualizar avatar
document.addEventListener("DOMContentLoaded", () => {
  const submit_btn = document.getElementById("perfil-form")
  submit_btn.addEventListener("submit", save_perfil);
});

async function save_perfil(event) {
  event.preventDefault();
  const popup = new Popup();
  const form = document.getElementById("perfil-form");
  const formData = new FormData(form);

  try {
    const response = await fetch("/custom_perfil/update/", {
      method: "POST",
      body: formData,
      headers: {
        'X-CSRFToken': formData.get('csrfmiddlewaretoken') || ''
      }
    });

    if (!response.ok) {
      const errorData = await response.json(); // Extraer el JSON del error
      throw new Error(errorData.error); // Lanzar el error con los datos del JSON
    }

    const data = await response.json(); // Parsear la respuesta JSON
    await popup.ejec({
      title: "Edicion de perfil exitoso",
      icon: "success",
      text: data.message || "Tu perfil ha sido editado con exito",
    });

    window.location.href = '/';
  } catch (error) {
    await popup.ejec({
      title: "Error en la edicion",
      icon: "error",
      text: error.message || "Error desconocido"
    })
    location.reload();
  }

}

function previewAvatar(event) {
  const reader = new FileReader();
  reader.onload = function () {
    const output = document.getElementById('profile-avatar');
    output.src = reader.result;
  };
  reader.readAsDataURL(event.target.files[0]);
}