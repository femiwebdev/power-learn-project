// src/js/script.js

// Function to toggle light/dark mode
function toggleTheme() {
    const body = document.body;
    body.classList.toggle('dark-mode');
}

// Function to validate the form
function validateForm(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorMessages = [];
    
    // Name validation
    if (name.trim() === '') {
        errorMessages.push('Name is required.');
    }
    
    // Email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        errorMessages.push('Please enter a valid email address.');
    }
    
    // Password validation
    if (password.length < 6) {
        errorMessages.push('Password must be at least 6 characters long.');
    }
    
    // Display error messages or success feedback
    const resultSection = document.getElementById('result');
    if (errorMessages.length > 0) {
        resultSection.innerHTML = errorMessages.join('<br>');
        resultSection.style.color = 'red';
    } else {
        resultSection.innerHTML = 'Form submitted successfully!';
        resultSection.style.color = 'green';
    }
}

// Function to toggle FAQ sections
function toggleFAQ(event) {
    const faqContent = event.target.nextElementSibling;
    faqContent.classList.toggle('collapsed');
}

// Event listeners
document.getElementById('themeToggle').addEventListener('click', toggleTheme);
document.getElementById('form').addEventListener('submit', validateForm);
const faqHeaders = document.querySelectorAll('.faq-header');
faqHeaders.forEach(header => {
    header.addEventListener('click', toggleFAQ);
});