const form = document.getElementById('gameForm');
const instructionsDiv = document.getElementById('instructions');

form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent the page from reloading

    // Get user inputs
    const players = document.getElementById('players').value;
    const complexity = document.getElementById('complexity').value;

    try {
        // Send a POST request to the backend
        const response = await fetch('http://127.0.0.1:5000/get-game', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                number_of_players: players,
                complexity: complexity,
            }),
        });

        const data = await response.json();

        if (data.success) {
            // Display the instructions
            instructionsDiv.innerText = data.instructions;
        } else {
            instructionsDiv.innerText = `Error: ${data.error}`;
        }
    } catch (error) {
        instructionsDiv.innerText = `Error: ${error.message}`;
    }
});
