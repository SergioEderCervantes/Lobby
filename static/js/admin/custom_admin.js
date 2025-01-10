// Para la parte de change_list.html

document.addEventListener('DOMContentLoaded', function() {
    const resultTableBody = document.getElementById("result_list").querySelector("tbody");
    if (!resultTableBody){
        return;
    }
    const rows = Array.from(resultTableBody.children);
    if (!rows){
        return;
    }
    rows.forEach((row) =>{
        links = row.querySelectorAll('a');
        links.forEach((link) => {
            // Cambio de link
            const enlacePrev = link.href;
            const urlParts = enlacePrev.split('/');
            const objetoID = urlParts[urlParts.length - 3];
            const urlActual = urlParts.slice(0, -3).join('/');
    
    
            const nuevaURL = urlActual + '/' + objetoID + "/view";
    
            link.href = nuevaURL;
            console.log(link.href);
        })
    })
});