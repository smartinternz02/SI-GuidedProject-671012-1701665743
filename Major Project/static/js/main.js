// This script can handle common functionality shared across multiple pages
// Example: Show/hide a navigation menu on small screens
document.addEventListener('DOMContentLoaded', function () {
    const menuButton = document.getElementById('menu-button');
    const navMenu = document.getElementById('nav-menu');

    menuButton.addEventListener('click', function () {
        navMenu.classList.toggle('show-menu');
    });

    // Add more common JavaScript code as needed for other pages
});