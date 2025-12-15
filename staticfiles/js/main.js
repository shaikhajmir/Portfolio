// main.js — advanced animations (GSAP + ScrollTrigger + Lenis + VanillaTilt + Lottie helpers)
// Requires: gsap, ScrollTrigger, Lenis, VanillaTilt loaded in base.html

document.addEventListener('DOMContentLoaded', () => {
  // If GSAP missing, degrade gracefully
  if (typeof gsap === 'undefined') {
    console.warn('GSAP missing — advanced animations skipped.');
    return;
  }
  gsap.registerPlugin(ScrollTrigger);

  /* ---------- Preloader control ---------- */
  const preloader = document.getElementById('preloader');
  const removePreloader = () => {
    if (!preloader) return;
    gsap.to(preloader, { autoAlpha: 0, duration: 0.65, ease: 'power2.inOut', onComplete: () => preloader.remove() });
  };

  // trigger entrance after small delay to let Lottie play
  setTimeout(removePreloader, 800);

  /* ---------- Hero subtle parallax (mouse + auto) ---------- */
  const hero = document.querySelector('.hero-float');
  if (hero) {
    // slow periodic sway
    gsap.to(hero, { y: -8, rotation: -0.5, duration: 3.6, ease: 'sine.inOut', yoyo: true, repeat: -1 });
    // mouse parallax
    window.addEventListener('mousemove', (e) => {
      const cx = window.innerWidth / 2;
      const cy = window.innerHeight / 2;
      const dx = (e.clientX - cx) / cx;
      const dy = (e.clientY - cy) / cy;
      gsap.to(hero, { x: dx * 6, y: -8 + dy * 6, rotation: dx * 0.6, duration: 0.8, ease: 'power3.out' });
    });
  }

  /* ---------- Project cards reveal + tilt ---------- */
  const projectCards = document.querySelectorAll('.project-card');
  if (projectCards.length) {
    gsap.from(projectCards, {
      y: 22, autoAlpha: 0, stagger: 0.12, duration: 0.9, ease: 'power3.out',
      scrollTrigger: { trigger: projectCards[0].parentElement, start: 'top 85%' }
    });
    if (typeof VanillaTilt !== 'undefined') {
      projectCards.forEach(el => VanillaTilt.init(el, { max: 12, speed: 400, glare: true, 'max-glare': 0.12, scale: 1.02 }));
    }
  }

  /* ---------- Skill bars: fill + bubble animation ---------- */
  document.querySelectorAll('.lang-wrap[data-prog]').forEach(el => {
    const pct = parseInt(el.dataset.prog || '0', 10);
    const bar = el.querySelector('.lang-bar');
    const bubble = el.querySelector('.lang-bubble');
    ScrollTrigger.create({
      trigger: el,
      start: 'top 85%',
      once: true,
      onEnter: () => {
        gsap.fromTo(bar, { width: '0%' }, { width: pct + '%', duration: 1.0, ease: 'power2.out' });
        if (bubble) gsap.fromTo(bubble, { x: -18, autoAlpha: 0 }, { x: 0, autoAlpha: 1, duration: 0.9, ease: 'back.out(1.3)' });
      }
    });
  });

  /* ---------- Counters: GSAP tween ---------- */
  document.querySelectorAll('[data-counter]').forEach(wrapper => {
    const display = wrapper.querySelector('[data-count-display]');
    if (!display) return;
    const target = parseInt(display.dataset.target || '0', 10);
    ScrollTrigger.create({
      trigger: wrapper,
      start: 'top 85%',
      once: true,
      onEnter: () => {
        gsap.fromTo({ val: 0 }, { val: target, duration: 1.4, ease: 'power3.out', onUpdate: function() {
          display.textContent = Math.floor(this.targets()[0].val);
        }});
      }
    });
  });

  /* ---------- Scroll-driven fades for generic sections ---------- */
  document.querySelectorAll('.reveal').forEach((el) => {
    ScrollTrigger.create({
      trigger: el,
      start: 'top 88%',
      onEnter: () => el.classList.add('show')
    });
  });

  /* ---------- Certificate modal (GSAP) ---------- */
  const certModal = document.querySelector('.cert-modal');
  if (certModal) {
    const modalImg = certModal.querySelector('img');
    document.querySelectorAll('.cert-thumb').forEach(img => {
      img.addEventListener('click', () => {
        const src = img.dataset.full || img.src;
        modalImg.src = src;
        certModal.classList.add('open');
        gsap.fromTo(modalImg, { scale: 0.88, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 0.45, ease: 'back.out(1.2)' });
      });
    });
    const backdrop = certModal.querySelector('.backdrop');
    if (backdrop) backdrop.addEventListener('click', () => {
      gsap.to(certModal.querySelector('img'), { scale: 0.88, autoAlpha: 0, duration: 0.28, onComplete: () => certModal.classList.remove('open') });
    });
  }

  /* ---------- Lottie elements fade-in ---------- */
  document.querySelectorAll('lottie-player').forEach(el => {
    ScrollTrigger.create({ trigger: el, start: 'top 95%', onEnter: () => gsap.fromTo(el, { autoAlpha: 0, y: 10 }, { autoAlpha: 1, y: 0, duration: 0.6 }) });
  });

  /* ---------- Chatbot entrance pulse ---------- */
  const bot = document.getElementById('chatbot-toggle');
  if (bot) {
    gsap.fromTo(bot, { scale: 0.9, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 0.75, ease: 'back.out(1.2)' });
    gsap.to(bot, { scale: 1.04, duration: 0.9, repeat: 1, yoyo: true, ease: 'sine.inOut', delay: 1.0 });
  }

  /* ---------- Accessibility: reduce motion respect ---------- */
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    gsap.globalTimeline.timeScale(0.0001);
  }
});
