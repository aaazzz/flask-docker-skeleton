# built-in
import sys
import os
import signal
import logging
import atexit
import flask
from flask import render_template
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
            
def signal_handler():
    """
    Do something before shutdown
    """
    logging.warning("[WARN ]signal handler is called!")
    sys.exit(0)   

# set signal handler
atexit.register(signal_handler)

# ---------------------------------------------------
# Flask app
# ---------------------------------------------------
print("[INFO ] * Flask starting server...")

@app.errorhandler(404)
@app.errorhandler(400)
@app.errorhandler(500)
def error_handler(error):
    """
    abort handler
    """
    try:
        response = flask.jsonify(
            {
            "error": error.description['error']
            }
        )

        return response, error.code
    except: # for default 500 
        response = flask.jsonify(
        {
            "error": "Not found"
        }
    )
        return response, 404

@app.errorhandler(405)
def method_not_allowed(e):
    response = flask.jsonify(
        {
            "error": "Invalid method."
        }
    )
    return response, 405

@app.route("/hello", methods=["GET"])
def hello():
    """Return JSON."""
    response = {}
    response["message"] = "Hello!"
    return flask.jsonify(response)

@app.route('/')
def home():
    """Landing page."""
    return render_template('home.html', title="Jinja Demo Site", description="Smarter page templates with Flask & Jinja.")

if __name__ == "__main__":
    # without uwsgi mode.
    # debug=True to auto reload
    app.run(debug=True, port=5000)
