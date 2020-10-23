import os
import pickle

dir_path = os.path.dirname(os.path.realpath(__file__))

# Third party libraries
from flask import Flask

from flask import render_template

last_loaded_models = None
model = None
model_reason = None
scaler = None

# Flask app setup
def app_setup():

    # Add administrative views here
    app = Flask(__name__)

    # Register assets handler
    # from scooby.utils import assets
    app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

    from ChurnApp.api import bp as api
    app.register_blueprint(api, url_prefix="/api")

    return app


# Create the application
app = app_setup()


# Home/login screen
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/api-call-example", methods=['GET'])
def api_example():
    return render_template("api-example.html")


@app.route("/dashboard-example", methods=['GET'])
def ajax_example():
    return render_template("ajax-example.html")


if __name__ == "__main__":
    app.run()
