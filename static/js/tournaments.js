const bgElements = document.querySelectorAll('.backImage');

if (bgElements) {
    bgElements.forEach((bgElement) => {
        const bgUrl = bgElement.dataset.bgUrl;
        if (bgUrl) {
            bgElement.style.backgroundImage = `url('${bgUrl}')`;
        }
    })
}