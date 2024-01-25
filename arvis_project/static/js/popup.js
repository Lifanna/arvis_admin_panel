function showPopup() {
    var popup = document.getElementById('popup-message');
    if (popup) {
        popup.style.display = 'block';
        setTimeout(function () {
            popup.style.display = 'none';
        }, 5000);
    }
}

function hidePopup() {
    var popup = document.getElementById('popup-message');
    if (popup) {
        popup.style.display = 'none';
    }
}

