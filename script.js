// Header shadow on scroll
const header = document.getElementById('header');
window.addEventListener('scroll', () => header.classList.toggle('scrolled', window.scrollY > 20));

// Mobile menu
const burger = document.getElementById('burger');
const nav = document.getElementById('nav');
burger.addEventListener('click', () => nav.classList.toggle('open'));
nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => nav.classList.remove('open')));

// Reveal on scroll
const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Contact form (demo — hələ backend-ə qoşulmayıb)
document.getElementById('form').addEventListener('submit', e => {
  e.preventDefault();
  document.getElementById('formNote').textContent = 'Təşəkkürlər! Müraciətiniz qəbul edildi.';
  e.target.reset();
});

document.getElementById('year').textContent = new Date().getFullYear();
