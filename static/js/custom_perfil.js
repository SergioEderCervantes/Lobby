 // Previsualizar avatar
 function previewAvatar(event) {
    const avatar = document.getElementById('profile-avatar');
    avatar.src = URL.createObjectURL(event.target.files[0]);
  }