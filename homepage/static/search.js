document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const searchResultsContainer = document.getElementById('search-results');

    searchForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission
        const query = searchInput.value.trim();

        // Make an AJAX request to the Django backend
        fetch(`/search/?query=${query}`)
            .then(response => response.json())
            .then(data => {
                // Clear previous search results
                searchResultsContainer.innerHTML = '';

                // Display new search results
                data.forEach(result => {
                    const resultElement = document.createElement('div');
                    resultElement.textContent = result.name; // Assuming 'name' is the field you want to display
                    searchResultsContainer.appendChild(resultElement);
                });
            })
            .catch(error => {
                console.error('Error fetching search results:', error);
            });
    });
});
