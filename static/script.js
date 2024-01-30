function circleClick(buttonNumber) {
    var button = document.getElementById('button' + buttonNumber);
    if (button.classList.contains('illuminated-yellow')) {
        button.classList.remove('illuminated-yellow');
        button.classList.add('illuminated-blue');
    } else if (button.classList.contains('illuminated-blue')) {
        button.classList.remove('illuminated-blue');
        button.classList.add('illuminated-red');
    } else if (button.classList.contains('illuminated-red')) {
        button.classList.remove('illuminated-red');
    } else {
        button.classList.add('illuminated-yellow');
    }
}

function confirmSave() {
    var confirmed = confirm('Have you tested the climb, and are happy to save it?');
    if (confirmed) {
        saveConfiguration();
    }
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

    var illuminatedButtonsYellow = document.querySelectorAll('.illuminated-yellow');
    var illuminatedButtonsBlue = document.querySelectorAll('.illuminated-blue');
    var illuminatedButtonsRed = document.querySelectorAll('.illuminated-red');

    if (illuminatedButtonsBlue.length != 2 || illuminatedButtonsRed.length != 1) {
        alert('You must have exactly 2 blue highlights and 1 red highlight.');
        return;
    }

    var illuminatedButtonsArray = Array.from(illuminatedButtonsYellow).map(button => {
        return { id: button.id.replace('button', ''), color: 'yellow' };
    }).concat(Array.from(illuminatedButtonsBlue).map(button => {
        return { id: button.id.replace('button', ''), color: 'blue' };
    })).concat(Array.from(illuminatedButtonsRed).map(button => {
        return { id: button.id.replace('button', ''), color: 'red' };
    }));

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
    var illuminatedButtons = document.querySelectorAll('.illuminated-yellow, .illuminated-blue, .illuminated-red');
    illuminatedButtons.forEach(button => {
        button.classList.remove('illuminated-yellow', 'illuminated-blue', 'illuminated-red');
    });
}

function loadConfigurations() {
    // Fetch the list of saved configurations from the server
    fetch('/get_configurations')
        .then(response => response.json())
        .then(data => {
            var configDropdown = document.getElementById('config-dropdown');
            configDropdown.innerHTML = ''; // Clear the existing list

            // Filter configurations by grade
            var gradeFilter = document.getElementById('grade-filter').value;
            var filteredData = data.filter(config => gradeFilter === "" || config.grade === gradeFilter);

            // Sort configurations alphabetically
            filteredData.sort((a, b) => a.name.localeCompare(b.name));

            // Populate the dropdown with saved configurations
            filteredData.forEach(config => {
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
            data.buttons.forEach(button => {
                var buttonElement = document.getElementById('button' + button.id);
                buttonElement.classList.add('illuminated-' + button.color); // Illuminate the buttons from the loaded configuration
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


function deleteConfiguration() {
    var configDropdown = document.getElementById('config-dropdown');
    var selectedConfig = configDropdown.value;

    if (!selectedConfig) {
        alert('Please select a configuration to delete.');
        return;
    }

    fetch(`/delete_configuration/${encodeURIComponent(selectedConfig)}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Configuration deleted successfully.');
            loadConfigurations();
        } else {
            alert('Error deleting configuration: ' + data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function testConfiguration() {
    var illuminatedButtonsYellow = document.querySelectorAll('.illuminated-yellow');
    var illuminatedButtonsBlue = document.querySelectorAll('.illuminated-blue');
    var illuminatedButtonsRed = document.querySelectorAll('.illuminated-red');

    var illuminatedButtonsArray = Array.from(illuminatedButtonsYellow).map(button => {
        return { id: button.id.replace('button', ''), color: 'yellow' };
    }).concat(Array.from(illuminatedButtonsBlue).map(button => {
        return { id: button.id.replace('button', ''), color: 'blue' };
    })).concat(Array.from(illuminatedButtonsRed).map(button => {
        return { id: button.id.replace('button', ''), color: 'red' };
    }));

    var configuration = {
        buttons: illuminatedButtonsArray
    };

    // Send the configuration to the server
    fetch('/test_configuration', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(configuration),
    })
    .then(response => response.json())
    .then(data => {
       // alert('Configuration tested successfully.');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Load configurations on page load
loadConfigurations();