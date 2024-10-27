// Cambiar la url para que la redirija al change
const change_link = document.getElementById('change_info')
if (change_link){
    const current_url = change_link.href;
    console.log(current_url);
    const new_url = current_url.replace("/view/#", "/change");
    console.log(new_url);
    change_link.href = new_url;
}

