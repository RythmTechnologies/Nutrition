// Dark Mode - Light Mode
const toggle = document.getElementById('darkModeToggle')

if (toggle) {
    toggle.addEventListener('click', function () {
        if (document.body.getAttribute('data-bs-theme') == 'dark') {
            document.body.setAttribute('data-bs-theme', 'light');
            localStorage.setItem("theme", "light");
            toggle.innerHTML = '<i class="fa-solid fa-moon"></i>'
          } else {
            document.body.setAttribute('data-bs-theme', 'dark');
            localStorage.setItem("theme", "dark");
            toggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
          }
        })
      }

if (localStorage.getItem('theme') == 'dark') {
    document.body.setAttribute('data-bs-theme', 'dark')
    toggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
} else {
    document.body.setAttribute('data-bs-theme', 'light')
    toggle.innerHTML = '<i class="fa-solid fa-moon"></i>'
}