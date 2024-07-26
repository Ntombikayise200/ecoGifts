// JavaScript for List Crafter Landing Page

// Function to validate form inputs
function validateForm() {
    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;
    const email = document.getElementById('email').value;
    const paymentMethod = document.getElementById('paymentMethod').value;
    const creditCardNumber = document.getElementById('creditCardNumber').value;
    const expiryDate = document.getElementById('expiryDate').value;
    const cvv = document.getElementById('cvv').value;

    if (!name || !address || !email || !paymentMethod || !creditCardNumber || !expiryDate || !cvv) {
        alert('Please fill out all fields.');
        return false;
    }
    // Add further validation checks as needed
    return true;
}

// Function to submit the form
function submitForm(event) {
    event.preventDefault(); // Prevent default form submission
    if (validateForm()) {
        // Normally, you would send the data to the server here
        alert('Form submitted successfully! Check your email for activation instructions.');
        // Redirect to the activation instructions page or perform other actions
    }
}

// Add event listener to the form
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('trialForm');
    if (form) {
        form.addEventListener('submit', submitForm);
    }
});