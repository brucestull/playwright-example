"""
Simple Flask app that displays tech gadgets with funny names from JSON data.
"""
import json
from flask import Flask, render_template

app = Flask(__name__)


def load_gadgets():
    """Load gadgets from JSON file."""
    try:
        with open('data/gadgets.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"gadgets": []}


@app.route('/')
def index():
    """Display the gadgets list."""
    data = load_gadgets()
    return render_template('index.html', gadgets=data.get('gadgets', []))


@app.route('/api/gadgets')
def api_gadgets():
    """API endpoint to get gadgets as JSON."""
    from flask import jsonify
    return jsonify(load_gadgets())


if __name__ == '__main__':
    app.run(debug=True, port=5000)
