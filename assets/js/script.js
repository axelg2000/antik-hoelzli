let lastScroll = 0;
const header = document.querySelector('header');

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset;

  if (currentScroll <= 10) {
    // Top of the page: show header, remove background
    header.style.transform = 'translateY(0)';
    header.classList.remove('scrolled-up');
  } else if (currentScroll > lastScroll) {
    // Scrolling down: hide header
    header.style.transform = 'translateY(-100%)';
  } else {
    // Scrolling up: show header + add background
    header.style.transform = 'translateY(0)';
    header.classList.add('scrolled-up');
  }

  lastScroll = currentScroll;
});