document.getElementById('checkButton').addEventListener('click', function() {
    const sourceAccount = document.getElementById('sourceAccount').value;
    const destinationAccount = document.getElementById('destinationAccount').value;
    const destinationCountry = document.getElementById('destinationCountry').value;
    const paymentCurrency = document.getElementById('paymentCurrency').value;
    const approximatePayment = document.getElementById('approximatePayment').value;

    // Make an API call to the Python server
    fetch('/api/check', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            sourceAccount,
            destinationAccount,
            destinationCountry,
            paymentCurrency,
            approximatePayment
        }),
    })
    .then(response => response.json())
    .then(data => {
        const response = document.getElementById('response');
        if (data.status === 'success') {
            response.innerHTML = `<span class="success">${data.message}</span>`;
        } else {
            response.innerHTML = `<span class="error">${data.message}</span>`;
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});