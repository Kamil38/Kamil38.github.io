// Credit: w3schools
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

document.addEventListener("DOMContentLoaded", function() {
  document.querySelector('.typewriter h2').classList.add('start-typing');
});

// This code is provided by CHATGPT
document.addEventListener('DOMContentLoaded', function() {
  var links = document.querySelectorAll('.topnav a');
  var currentUrl = window.location.href;

  links.forEach(function(link) {
      if (link.href === currentUrl) {
          link.classList.add('active');
      }

      link.addEventListener('click', function() {
          links.forEach(function(link) {
              link.classList.remove('active');
          });

          this.classList.add('active');
      });
  });
});


