// Para la parte de change_list.html



document.addEventListener('DOMContentLoaded', function() {
    const ths = document.querySelectorAll('.field-__str__');
    if (ths){
        ths.forEach(th => {
            const enlace = th.querySelector('a');
            if (enlace){
                const enlacePrev = enlace.href;
                const urlParts = enlacePrev.split('/');
                const objetoID = urlParts[urlParts.length - 3];
                const urlActual = urlParts.slice(0, -3).join('/');


                const nuevaURL = urlActual + '/' + objetoID + "/view";

                enlace.href = nuevaURL;
            }
        })
    }
})
