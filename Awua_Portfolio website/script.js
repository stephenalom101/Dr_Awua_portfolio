// Hamburger menu
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('nav-menu');

if (hamburger && navMenu) {
  hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('open');
  });
  navMenu.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => navMenu.classList.remove('open'));
  });
}

// Smooth scroll with navbar offset
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const id = this.getAttribute('href');
    if (id === '#') return;
    const el = document.querySelector(id);
    if (el) {
      e.preventDefault();
      const navH = document.getElementById('navbar').offsetHeight;
      const targetPosition = el.getBoundingClientRect().top + window.pageYOffset - navH;
      window.scrollTo({ top: targetPosition, behavior: 'smooth' });
    }
  });
});

// Fade-in observer
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.classList.add('visible');
  });
}, { threshold: 0.12 });

document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

// Skill bar animation
const skillObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.querySelectorAll('.skill-fill').forEach(bar => {
        bar.style.width = bar.getAttribute('data-w');
      });
    }
  });
}, { threshold: 0.3 });

const skillsSection = document.getElementById('experience');
if (skillsSection) skillObserver.observe(skillsSection);
