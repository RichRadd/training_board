function circleClick(buttonNumber) {
    var button = document.getElementById('button' + buttonNumber);
    button.classList.toggle('illuminated');
}

function saveConfiguration() {
    var configNameInput = document.getElementById('config-name-input');
    var gradeInput = document.getElementById('grade-input');
    var configName = configNameInput.value.trim();
    var grade = gradeInput.value;
    if (!configName || !grade) {
        alert('Please enter a configuration name and select a grade.');
        return;
    }

    var illuminatedButtons = document.querySelectorAll('.illuminated');
    var illuminatedButtonsArray = Array.from(illuminatedButtons).map(button => {
        return button.id.replace('button', '');
    });

    var configuration = {
        name: configName,
        grade: grade,
        buttons: illuminatedButtonsArray
    };

    // Send the configuration to the server
    fetch('/save_configuration', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(configuration),
    })
    .then(response => response.json())
    .then(data => {
        alert('Configuration saved successfully.');
        loadConfigurations();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function clearGrid() {
    var illuminatedButtons = document.querySelectorAll('.illuminated');
    illuminatedButtons.forEach(button => {
        button.classList.remove('illuminated');
    });
}

function loadConfigurations() {
    // Fetch the list of saved configurations from the server
    fetch('/get_configurations')
        .then(response => response.json())
        .then(data => {
            var configDropdown = document.getElementById('config-dropdown');
            configDropdown.innerHTML = ''; // Clear the existing list

            // Populate the dropdown with saved configurations
            data.forEach(config => {
                var option = document.createElement('option');
                option.value = config.name;
                option.textContent = `${config.grade} - ${config.name}`;
                configDropdown.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function loadConfiguration() {
    var configDropdown = document.getElementById('config-dropdown');
    var selectedConfig = configDropdown.value;

    if (!selectedConfig) {
        alert('Please select a configuration to load.');
        return;
    }

    // Fetch the selected configuration from the server
    fetch(`/get_configuration/${encodeURIComponent(selectedConfig)}`)
        .then(response => response.json())
        .then(data => {
            clearGrid(); // Clear existing illumination
            data.buttons.forEach(buttonNumber => {
                circleClick(buttonNumber); // Illuminate the buttons from the loaded configuration
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Load configurations on page load
loadConfigurations();
