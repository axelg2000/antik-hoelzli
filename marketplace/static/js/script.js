// marketplace/static/js/script.js

// All code runs only once the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM fully loaded!");

  // ✅ 1. Header hide/show on scroll
  let lastScroll = 0;
  const header = document.querySelector('header');

  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll <= 60) {
      header.style.transform = 'translateY(0)';
      header.classList.remove('scrolled-up');
    } else if (currentScroll > lastScroll) {
      header.style.transform = 'translateY(-100%)';
    } else {
      header.style.transform = 'translateY(0)';
      header.classList.add('scrolled-up');
    }

    lastScroll = currentScroll;
  });

  // ✅ 2. Blur effect on scroll for bottom image (if present)
  const bottomImage = document.querySelector(".choice-wrapper img");
  const bottomElement = document.querySelector(".choice-wrapper");
  if (bottomImage && bottomElement) {
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
          const blurValue = Math.min(
            blurMax,
            (scrollTop / maxScroll) * blurMax
          );
          bottomImage.style.filter = `blur(${blurValue}px)`;
        } else {
          bottomImage.style.filter = `blur(${blurMin}px)`;
        }
      }

      lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
    });
  }

  // ✅ 3. Blur effect for gallerie-image
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

const fadeInElements = document.querySelectorAll('.box, .thomas-presentation-container, .bottom-container, .index-container');
if (fadeInElements.length) {
  const fadeInObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('show');
        fadeInObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1
  });

  fadeInElements.forEach(el => fadeInObserver.observe(el));
}


  // ✅ 7. Copy email to clipboard
  window.copyEmail = function () {
    const email = "your@email.com";
    navigator.clipboard.writeText(email).then(() => {
      alert("Email copied to clipboard!");
    }).catch(err => {
      alert("Failed to copy email.");
    });
  };
});