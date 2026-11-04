// Header shadow on scroll
const header = document.getElementById('header');
window.addEventListener('scroll', () => header.classList.toggle('scrolled', window.scrollY > 40));

// Mobile menu
const nav = document.getElementById('nav');
document.getElementById('burger').addEventListener('click', () => nav.classList.toggle('open'));
nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => nav.classList.remove('open')));

// Reveal on scroll
const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Registration form -> WhatsApp
const WHATSAPP = '994557812525';
document.getElementById('form')?.addEventListener('submit', e => {
  e.preventDefault();
  const f = new FormData(e.target);
  const text =
    `Salam! Qeydiyyat müraciəti:\n` +
    `👤 Valideyn: ${f.get('parent')}\n` +
    `📞 Telefon: ${f.get('phone')}\n` +
    `🎒 Sinif: ${f.get('grade')}\n` +
    `🏫 Filial: ${f.get('branch')}\n` +
    `📚 Proqram: ${f.get('program')}`;
  window.open(`https://wa.me/${WHATSAPP}?text=${encodeURIComponent(text)}`, '_blank');
});

document.getElementById('year').textContent = new Date().getFullYear();
