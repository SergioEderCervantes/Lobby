// Para la parte de change_list.html

console.log("Entro al archivo js")

document.addEventListener('DOMContentLoaded', function() {
    const ths = document.querySelectorAll('.field-__str__');
    if (ths){
        ths.forEach(th => {
            const enlace = th.querySelector('a');
            if (enlace){
                console.log("Se encontro el enlace");
                enlace.href = "https://www.youtube.com/";
            }
            else{
                console.log("no se encontro el enlace");
            }
        })
    }
    else{
        console.log("No se encontraron th's");
    }
})
