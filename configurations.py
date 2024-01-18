# configurations.py
import json

CONFIGURATIONS_FILE = 'configurations.txt'

def get_configurations():
    configurations = []
    try:
        with open(CONFIGURATIONS_FILE, 'r') as file:
            for line in file:
                configuration = json.loads(line)
                configurations.append(configuration)
    except FileNotFoundError:
        pass
    return configurations

def save_configurations(configurations):
    with open(CONFIGURATIONS_FILE, 'w') as file:
        for configuration in configurations:
            file.write(json.dumps(configuration) + '\n')

def is_unique_name(name, configurations):
    return all(config['name'] != name for config in configurations)
