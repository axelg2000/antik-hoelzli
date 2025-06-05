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
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM fully loaded!");

  const bottomImage = document.querySelector(".choice-wrapper img");
  const bottomElement = document.querySelector(".choice-wrapper");
  if (!bottomImage || !bottomElement) return;

  const blurMax = 5;
  const blurMin = 0;
  const maxScroll = 200;

  let isInView = false;
  let lastScrollTop = 0;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      isInView = entry.isIntersecting;
      if (!isInView) {
        bottomImage.style.filter = `blur(${blurMin}px)`;
      }
    });
  });
  observer.observe(bottomElement);

  window.addEventListener("scroll", () => {
    const scrollTop = window.scrollY;

    if (isInView) {
      if (scrollTop > lastScrollTop) {
        // Scrolling down: increase blur
        const blurValue = Math.min(
          blurMax,
          (scrollTop / maxScroll) * blurMax
        );
        bottomImage.style.filter = `blur(${blurValue}px)`;
      } else {
        // Scrolling up: decrease blur quickly
        bottomImage.style.filter = `blur(${blurMin}px)`;
      }
    }

    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
  });
});

document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM fully loaded! Ready to scroll.");

  window.addEventListener("scroll", () => {

    const scrollTop = window.scrollY;

    const maxScroll = 200;
    const blurMax = 5;
    const blurMin = 0;

    const blurValue = Math.max(
      blurMin,
      blurMax - (scrollTop / maxScroll) * blurMax
    );

    const image = document.querySelector(".gallerie-image img");
    if (image) {
      image.style.filter = `blur(${blurValue}px)`;
    }
  });
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
};

