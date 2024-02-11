document.addEventListener("DOMContentLoaded", function() {
  const navbar = document.querySelector('.navbar'); // Navbar seçimi
  const darkModeToggle = document.getElementById('darkModeToggle'); // Dark mode toggle butonu

  // Sayfa yüklenirken tema kontrolü
  function checkTheme() {
    const theme = localStorage.getItem('theme') || 'light'; // Local storage'dan tema bilgisi
    document.body.classList.add(theme + '-theme'); // Tema sınıfını body'e ekleme
    navbar.classList.add('navbar-custom'); // Özel navbar sınıfını ekleme
  }

  // Sayfa kaydırıldığında navbar rengini değiştiren fonksiyon
  function toggleNavbarColorOnScroll() {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        navbar.classList.add('navbar-scrolled');
      } else {
        navbar.classList.remove('navbar-scrolled');
      }
    });
  }

  // Dark mode toggle butonuna tıklandığında tema değiştirme
  darkModeToggle.addEventListener('click', () => {
    if (document.body.classList.contains('light-theme')) {
      document.body.classList.replace('light-theme', 'dark-theme');
      localStorage.setItem('theme', 'dark'); // Temayı local storage'a kaydet
    } else {
      document.body.classList.replace('dark-theme', 'light-theme');
      localStorage.setItem('theme', 'light'); // Temayı local storage'a kaydet
    }
  });

  checkTheme(); // Tema kontrolü fonksiyonunu çağırma
  toggleNavbarColorOnScroll(); // Kaydırma ile navbar rengini değiştirme fonksiyonunu çağırma
});