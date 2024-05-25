// Attend que le contenu HTML soit complètement chargé avant d'exécuter le script
document.addEventListener("DOMContentLoaded", () => {
  // Récupère l'élément avec l'ID "icons" dans le DOM
  const icons = document.getElementById("icons");
  // Récupère l'élément avec l'ID "nav" dans le DOM
  const nav = document.getElementById("nav");
  // Récupère tous les éléments <li> dans la balise <nav>
  const links = document.querySelectorAll("nav li");

  // Ajoute un événement "click" à l'élément avec l'ID "icons"
  icons.addEventListener("click", () => {
    // Bascule la classe "active" de l'élément avec l'ID "nav"
    nav.classList.toggle("active");
  });

  // Pour chaque élément <li> trouvé dans la balise <nav>
  links.forEach((link) => {
    // Ajoute un événement "click" à chaque élément <li>
    link.addEventListener("click", () => {
      // Supprime la classe "active" de l'élément avec l'ID "nav"
      nav.classList.remove("active");
    });
  });
});
