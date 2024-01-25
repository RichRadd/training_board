# routes.py
from flask import render_template, request, jsonify
from configurations import get_configurations, save_configurations, is_unique_name

def configure_routes(app):
    @app.route('/')
    def index():
        rows = 10
        cols = 10
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
            configurations = get_configurations()
            configuration = next((config for config in configurations if config['name'] == config_name), None)
            if configuration:
                return jsonify(configuration)
            else:
                return jsonify({'error': 'Configuration not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
