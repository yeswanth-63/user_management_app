// function for pop message if invalid credentials are entered
document.addEventListener("DOMContentLoaded", function () {
  const popup = document.getElementById('popup');
  if (popup) {
    popup.style.display = 'block';
    setTimeout(() => {
      popup.style.display = 'none';
    }, 3000); // disappears after 3 seconds
  }
});
