// ===== Portfolio interactions =====
(function () {
  "use strict";

  // Footer year
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Sticky nav shadow on scroll
  const nav = document.getElementById("nav");
  const onScroll = () => nav.classList.toggle("scrolled", window.scrollY > 40);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // Mobile menu toggle
  const toggle = document.getElementById("navToggle");
  const menu = document.getElementById("navMenu");
  toggle.addEventListener("click", () => {
    const open = menu.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
  });
  menu.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      menu.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    })
  );

  // Typewriter effect for hero role
  const typed = document.getElementById("typed");
  const roles = [
    "Business Intelligence Manager",
    "Quantitative Researcher",
    "Data & Analytics Leader",
    "Machine Learning Practitioner",
  ];
  let roleIdx = 0;
  let charIdx = 0;
  let deleting = false;

  function tick() {
    const current = roles[roleIdx];
    if (deleting) {
      charIdx--;
    } else {
      charIdx++;
    }
    typed.textContent = current.slice(0, charIdx);

    let delay = deleting ? 45 : 90;
    if (!deleting && charIdx === current.length) {
      delay = 1600;
      deleting = true;
    } else if (deleting && charIdx === 0) {
      deleting = false;
      roleIdx = (roleIdx + 1) % roles.length;
      delay = 400;
    }
    setTimeout(tick, delay);
  }
  if (typed) tick();

  // Scroll reveal
  const revealSelectors = [
    ".tl-item", ".project", ".skill-card", ".edu-item",
    ".about__card", ".about__text", ".cert-list", ".contact"
  ];
  const revealEls = document.querySelectorAll(revealSelectors.join(","));
  revealEls.forEach((el) => el.setAttribute("data-reveal", ""));
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("visible");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("visible"));
  }
})();
