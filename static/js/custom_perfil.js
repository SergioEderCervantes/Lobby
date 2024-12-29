 // Previsualizar avatar
 document.addEventListener("DOMContentLoaded", () => {
  const submit_btn = document.getElementById("perfil-form")
  submit_btn.addEventListener("submit", save_perfil);
});


async function save_perfil(params) {
  event.preventDefault(); 
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
      throw new Error(JSON.stringify(errorData)); // Lanzar el error con los datos del JSON
    }

    const data = await response.json(); // Parsear la respuesta JSON
    console.log("Respuesta JSON:", data);
  } catch (error) {
    // Intentar parsear el JSON del error lanzado
    let errorData;
    try {
        errorData = JSON.parse(error.message); // Intentar extraer el JSON
    } catch {
        errorData = { message: error.message }; // Fallback
    }
    console.error("Error capturado:", errorData.error);
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
async function name(params) {
  
}