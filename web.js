// Selectors
const navLinks = document.querySelectorAll('.nav-bar a');
const sections = document.querySelectorAll('section');
const heroSection = document.querySelector('.hero');
const sidebar = document.querySelector('.sidebar');
const toggleButton = document.querySelector('.toggle-button');
const anchorLinks = document.querySelectorAll('a[href*="#"]');

// Animations
const animations = {
  fade: {
    in: 'animate__fadeIn',
    out: 'animate__fadeOut',
  },
  slide: {
    in: 'animate__slideInLeft',
    out: 'animate__slideOutLeft',
  },
};

// Add event listeners to navigation links
navLinks.forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const targetSection = document.querySelector(link.getAttribute('href'));
    targetSection.scrollIntoView({ behavior: 'mooth' });
    animateSection(targetSection, animations.fade);
  });
});

// Add event listeners to anchor links
anchorLinks.forEach((anchor) => {
  anchor.addEventListener('click', (event) => {
    event.preventDefault();
    const targetSection = document.querySelector(anchor.getAttribute('href'));
    targetSection.scrollIntoView({ behavior: 'mooth' });
    animateSection(targetSection, animations.fade);
  });
});

// Add event listener to toggle button
toggleButton.addEventListener('click', () => {
  sidebar.classList.toggle('open');
  animateSidebar(sidebar, animations.slide);
});

// Animate section on scroll
sections.forEach((section) => {
  section.addEventListener('scroll', () => {
    animateSection(section, animations.fade);
  });
});

// Animate hero section on load
window.addEventListener('load', () => {
  animateSection(heroSection, animations.fade);
});

// Animation functions
function animateSection(section, animation) {
  section.classList.add(animation.in);
  setTimeout(() => {
    section.classList.remove(animation.in);
    section.classList.add(animation.out);
  }, 1000);
}

function animateSidebar(sidebar, animation) {
  sidebar.classList.add(animation.in);
  setTimeout(() => {
    sidebar.classList.remove(animation.in);
    sidebar.classList.add(animation.out);
  }, 500);
}