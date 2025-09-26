// This file contains helper functions that perform common tasks such as calculating totals, formatting strings, and toggling content. These functions can be reused throughout the main.js file.

function calculateTotal(numbers) {
    let total = 0;
    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }
    return total;
}

function formatString(str) {
    return str.trim().toLowerCase();
}

function toggleVisibility(elementId) {
    const element = document.getElementById(elementId);
    if (element.style.display === "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}

function isEven(number) {
    return number % 2 === 0;
}