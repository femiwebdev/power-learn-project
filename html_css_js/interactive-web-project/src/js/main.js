// main.js

// Function to capture user input and display results
function captureInput() {
    const userInput = document.getElementById('userInput').value;
    const resultSection = document.getElementById('result');
    
    // Decision making using if/else statements
    if (userInput.trim() === '') {
        resultSection.innerHTML = 'Please enter a value.';
    } else {
        resultSection.innerHTML = `You entered: ${userInput}`;
    }
}

// Function to process multiple inputs
function processInputs() {
    const inputs = document.querySelectorAll('.inputField');
    const results = [];
    
    // Loop through inputs and collect values
    inputs.forEach(input => {
        if (input.value.trim() !== '') {
            results.push(input.value);
        }
    });
    
    // Display results
    console.log('Processed Inputs:', results);
    document.getElementById('resultsList').innerHTML = results.join(', ');
}

// Event listeners for buttons
document.getElementById('captureButton').addEventListener('click', captureInput);
document.getElementById('processButton').addEventListener('click', processInputs);