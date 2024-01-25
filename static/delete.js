document.getElementById('delete-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var configDropdown = document.getElementById('config-dropdown');
    var selectedConfig = configDropdown.value;

    if (!selectedConfig) {
        alert('Please select a configuration to delete.');
        return;
    }

    // Send a request to the server to delete the selected configuration
    fetch(`/delete_configuration/${encodeURIComponent(selectedConfig)}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        alert('Configuration deleted successfully.');
        loadConfigurations();
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Load configurations on page load
loadConfigurations();