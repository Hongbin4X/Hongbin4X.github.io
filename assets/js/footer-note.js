(function () {
  var note = document.querySelector('.footer-note');
  if (!note) return;

  var button = note.querySelector('button');
  var particles = note.querySelector('.footer-note__particles');
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var captionTimeout;

  button.addEventListener('click', function () {
    window.clearTimeout(captionTimeout);
    note.classList.add('is-active');
    captionTimeout = window.setTimeout(function () {
      note.classList.remove('is-active');
    }, 2400);

    if (reducedMotion.matches || particles.childElementCount >= 8) return;

    var heart = document.createElement('span');
    heart.className = 'footer-note__particle';
    heart.textContent = '♥';
    heart.style.setProperty('--drift', (Math.random() * 32 - 16) + 'px');
    particles.appendChild(heart);
    window.setTimeout(function () {
      heart.remove();
    }, 1500);
  });
}());
