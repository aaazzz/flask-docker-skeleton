# built-in
import sys
import os
import signal
import logging
import atexit
import flask
from flask_cors import CORS

# initialize our Flask application and pre-trained model
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

@app.route("/", methods=["GET"])
def hello():

    response = {}
    response["message"] = "Hello!"
    return flask.jsonify(response)


if __name__ == "__main__":
    # without uwsgi mode.
    app.run()
