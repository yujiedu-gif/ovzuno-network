(() => {
  const root = document.documentElement;
  root.classList.add("js");

  const header = document.querySelector(".site-header");
  const setHeaderState = () => header?.classList.toggle("site-header--compact", window.scrollY > 24);
  setHeaderState();
  window.addEventListener("scroll", setHeaderState, { passive: true });

  const revealItems = document.querySelectorAll(".reveal-block");
  if ("IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-revealed");
        observer.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -10%", threshold: 0.08 });
    revealItems.forEach((item) => revealObserver.observe(item));

    const hero = document.querySelector("[data-motion-root]");
    if (hero) {
      const motionObserver = new IntersectionObserver(([entry]) => {
        hero.classList.toggle("motion-paused", !entry.isIntersecting);
      }, { threshold: 0.02 });
      motionObserver.observe(hero);
    }
  } else {
    revealItems.forEach((item) => item.classList.add("is-revealed"));
  }

})();
