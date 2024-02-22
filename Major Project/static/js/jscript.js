// This script can contain additional custom JavaScript code for specific pages or components
// Example: Add custom behavior to elements on a specific page
document.addEventListener('DOMContentLoaded', function () {
    const pageTitle = document.title;

    if (pageTitle === 'Your Page Title') {
        // Add specific behavior for this page
        // Example: Change the background color of a specific element
        const specialElement = document.getElementById('special-element');
        specialElement.style.backgroundColor = '#ffcc00';
    }
    
    // Add more custom JavaScript code as needed for other pages or components
});