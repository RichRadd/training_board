# main.pyrender_template
from flask import Flask, render_template
from routes import configure_routes

data = {
    "name": "f5 light up", 
    "grade": "V0", 
    "buttons": [
        {"id": "142", "color": "yellow"},
        {"id": "141", "color": "yellow"},
        {"id": "140", "color": "yellow"},
        {"id": "139", "color": "yellow"},
        {"id": "137", "color": "yellow"},
        {"id": "136", "color": "yellow"},
        {"id": "135", "color": "yellow"},
        {"id": "134", "color": "yellow"},
        {"id": "133", "color": "yellow"},
        {"id": "121", "color": "yellow"},
        {"id": "126", "color": "yellow"},
        {"id": "118", "color": "yellow"},
        {"id": "113", "color": "yellow"},
        {"id": "97", "color": "yellow"},
        {"id": "98", "color": "yellow"},
        {"id": "99", "color": "yellow"},
        {"id": "100", "color": "yellow"},
        {"id": "102", "color": "yellow"},
        {"id": "94", "color": "yellow"},
        {"id": "89", "color": "yellow"},
        {"id": "88", "color": "yellow"},
        {"id": "87", "color": "yellow"},
        {"id": "86", "color": "yellow"},
        {"id": "85", "color": "yellow"},
        {"id": "73", "color": "yellow"},
        {"id": "82", "color": "yellow"},
        {"id": "70", "color": "yellow"},
        {"id": "61", "color": "yellow"},
        {"id": "49", "color": "yellow"},
        {"id": "58", "color": "yellow"},
        {"id": "46", "color": "yellow"},
        {"id": "41", "color": "yellow"},
        {"id": "40", "color": "yellow"},
        {"id": "39", "color": "yellow"},
        {"id": "38", "color": "yellow"},
        {"id": "37", "color": "yellow"}
    ]
}


app = Flask(__name__)

if __name__ == "__main__":
    # Convert color names to GRB values
    color_map = {'red': (0, 0, 255), 'green': (255, 0, 0), 'blue': (0, 255, 0), 'yellow': (255, 0 ,255)}
    for button in data['buttons']:
        try:
            button['color'] = color_map[button['color']]
        except KeyError:
            print(f"Error: Color {button['color']} not found in color_map")
            raise
    # Light up the LEDs
    from lightled import set_leds
    print("Setting LEDs...")
    set_leds(data['buttons'])
    print("LEDs set")

    
    configure_routes(app)
    app.run(host='0.0.0.0', port=5000)
