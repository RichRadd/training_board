# main.py
from flask import Flask, render_template
from routes import configure_routes

app = Flask(__name__)

if __name__ == "__main__":
    configure_routes(app)
    app.run(host='0.0.0.0', port=5000)
