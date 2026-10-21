// Copy the sample assignment language on Step 4.
document.querySelectorAll('.copybtn').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var box = btn.closest('details');
    var text = Array.from(box.querySelectorAll('li, p')).map(function (el, i) {
      return el.tagName === 'LI' ? (i + 1) + '. ' + el.innerText : el.innerText;
    }).join('\n\n');
    navigator.clipboard.writeText(text).then(function () {
      btn.textContent = 'Copied';
      setTimeout(function () { btn.textContent = 'Copy this language'; }, 2000);
    });
  });
});
