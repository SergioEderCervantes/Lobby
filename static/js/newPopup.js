

class Popup {
    #overlay;
    #loader;


    constructor() {
        this.#createOverlayHtml();
        this.#createLoaderHtml();
        this.showOverlayAndLoader();
    }

    // IMPORTANT: cuando se muestre el loader poner visibility: visible y opacity: 1 si no no se mostrara
    #createOverlayHtml() {
        this.#overlay = document.createElement("div");
        this.#overlay.setAttribute("id", "popup_overlay")
    }
    #createLoaderHtml() {
        this.#loader = document.createElement("div");
        this.#loader.setAttribute("id", "loader_container");
        let innerhtml = `
            <div class="loader">
                <div class="loader__circle"></div>
                <div class="loader__circle"></div>
                <div class="loader__circle"></div>
                <div class="loader__circle"></div>
                <div class="loader__circle"></div>
            </div>
        `;
        this.#loader.innerHTML = innerhtml;

        this.#overlay.appendChild(this.#loader);
    }

    showOverlayAndLoader(){
        document.body.appendChild(this.#overlay);
        this.#overlay.style.visibility = 'visible';
        this.#overlay.style.opacity = 1;
    }

    closeLoader(){
        this.#loader.style.visibility = 'hidden';
        this.#loader.style.opacity = 0;
    }
    
    closeOverlay(){
        document.body.removeChild(this.#overlay);
    }

    async ejec(data = {}) {
        data.background = "#171717"; 
        data.color = "#fff";
        this.closeLoader();
        return Swal.fire(data);
    }
}
