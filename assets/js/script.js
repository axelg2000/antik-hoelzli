let lastScroll = 0;
const header = document.querySelector('header');

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset;

  if (currentScroll <= 60) {
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


document.getElementById("toggleSlider").addEventListener("click", function () {
  const sliderContainer = document.getElementById("sliderContainer");
  sliderContainer.style.display = sliderContainer.style.display === "none" ? "block" : "none";
});

// Handle slider change
document.getElementById("priceRange").addEventListener("input", function () {
  const maxPrice = parseInt(this.value);
  document.getElementById("priceValue").textContent = maxPrice;

  const items = Array.from(document.querySelectorAll("#itemList li"));

  items.forEach(item => {
    const itemPrice = parseInt(item.getAttribute("data-price"));
    item.style.display = itemPrice <= maxPrice ? "list-item" : "none";
  });
});


function copyEmail() {
  const email = "your@email.com";
  navigator.clipboard.writeText(email).then(() => {
    alert("Email copied to clipboard!");
  }).catch(err => {
    alert("Failed to copy email.");
  });
}