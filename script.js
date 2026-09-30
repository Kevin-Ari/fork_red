const menuButton = document.querySelector('.menu-toggle');
const menu = document.querySelector('.main-nav');
const programsButton = document.querySelector('.programs-toggle');
const programs = document.querySelector('.nav-dropdown');

function closeMenu() {
  menu.classList.remove('open');
  programs.classList.remove('open');
  menuButton.setAttribute('aria-expanded', 'false');
  menuButton.setAttribute('aria-label', 'Abrir menú');
  programsButton.setAttribute('aria-expanded', 'false');
}

menuButton.addEventListener('click', () => {
  const open = menu.classList.toggle('open');
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
});

menu.addEventListener('click', (event) => {
  if (event.target.closest('a')) closeMenu();
});

programsButton.addEventListener('click', () => {
  const open = programs.classList.toggle('open');
  programsButton.setAttribute('aria-expanded', String(open));
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') closeMenu();
});

window.matchMedia('(min-width: 1051px)').addEventListener('change', (event) => {
  if (event.matches) closeMenu();
});
