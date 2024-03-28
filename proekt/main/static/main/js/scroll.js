const form = document.querySelector('form');
const scrollbarPosition = window.pageYOffset;

form.addEventListener('submit', () => {
  localStorage.setItem('scrollbarPosition', scrollbarPosition);
});