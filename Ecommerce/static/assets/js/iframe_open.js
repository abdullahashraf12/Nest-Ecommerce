
document.addEventListener('DOMContentLoaded', function() {
    const overlay = document.querySelector('.overlay');
    const popup = document.querySelector('.popup');
    const iframe = popup.querySelector('iframe');
    const triggers = document.querySelectorAll('.popup-trigger');
  
    triggers.forEach(function(trigger) {
      trigger.addEventListener('click', function(e) {
        e.preventDefault();
        const src = this.getAttribute('data-src');
        iframe.src = src;
        overlay.style.display = 'block';
        popup.style.display = 'block';
      });
    });
  
    overlay.addEventListener('click', function() {
      overlay.style.display = 'none';
      popup.style.display = 'none';
      iframe.src = ''; // Reset iframe src
    });
  });
  
  
  
  