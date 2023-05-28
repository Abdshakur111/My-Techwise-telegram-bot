// script.js
window.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registration-form');
    const trackingIdInput = document.getElementById('tracking-id');
    const registerBtn = document.getElementById('register-btn');
    const countdownDiv = document.getElementById('countdown');
    const remainingDays = document.getElementById('remaining-days');
    const earnings = document.getElementById('earnings');
    const issueReportingForm = document.getElementById('issue-reporting');
    const issueText = document.getElementById('issue-text');
    const reportBtn = document.getElementById('report-btn');

    registerForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const trackingId = trackingIdInput.value.trim();
        if (trackingId) {
            // Implement your logic to register the user with the tracking ID
        }
    });

    issueReportingForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const issue = issueText.value.trim();
        if (issue) {
            // Implement your logic to report the issue
        }
    });

    // Function to update the countdown and earnings
    function updateCountdown() {
        // Implement your logic to update the countdown and earnings
    }

    // Update the countdown and earnings every second
    setInterval(updateCountdown, 1000);
});
