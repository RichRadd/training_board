# routes.py
from flask import render_template, request, jsonify
from configurations import get_configurations, save_configurations, is_unique_name

def configure_routes(app):
    @app.route('/')
    def index():
        rows = 12
        cols = 20
        return render_template('index.html', rows=rows, cols=cols)

    @app.route('/save_configuration', methods=['POST'])
    def save_configuration():
        try:
            data = request.json
            configurations = get_configurations()

            # Check if the name is unique
            if not is_unique_name(data['name'], configurations):
                return jsonify({'error': 'Configuration name must be unique.'}), 400

            configurations.append(data)
            save_configurations(configurations)
            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/get_configurations')
    def get_configurations_route():
        try:
            configurations = get_configurations()
            return jsonify(configurations)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/get_configuration/<config_name>', methods=['GET'])
    def get_configuration(config_name):
        try:
            print("Getting configurations...")
            configurations = get_configurations()
            print("Configurations:", configurations)
            configuration = next((config for config in configurations if config['name'] == config_name), None)
            print("Configuration:", configuration)
            if configuration:
                # Convert color names to GRB values
                color_map = {'red': (0, 255, 0), 'green': (255, 0, 0), 'blue': (0, 0, 255), 'yellow': (255, 255, 0)}
                reverse_color_map = {(0, 255, 0): 'red', (255, 0, 0): 'green', (0, 0, 255): 'blue', (255, 255, 0): 'yellow'}
                for button in configuration['buttons']:
                    try:
                        button['color'] = color_map[button['color']]
                    except KeyError:
                        print(f"Error: Color {button['color']} not found in color_map")
                        raise
                # Light up the LEDs
                from lightled import set_leds
                print("Setting LEDs...")
                set_leds(configuration['buttons'])
                print("LEDs set")
                # Convert GRB values back to color names
                for button in configuration['buttons']:
                    button['color'] = reverse_color_map[button['color']]
                print("Returning configuration:", configuration)  # Print the configuration before returning it
                return jsonify(configuration)
            else:
                return jsonify({'error': 'Configuration not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500