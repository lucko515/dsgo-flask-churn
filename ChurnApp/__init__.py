import os
import pickle

dir_path = os.path.dirname(os.path.realpath(__file__))

# Third party libraries
from flask import Flask


from flask import render_template

model = None
model_reason = None
scaler = None




# Flask app setup
def app_setup():
    global model
    global model_reason
    global scaler

    # Add administrative views here
    app = Flask(__name__)

    # Register assets handler
    # from scooby.utils import assets
    app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

    with open(dir_path + "/models/churn_prediction.pickle", "rb") as f:
        model = pickle.load(f)

    with open(dir_path + "/models/reason_prediction.pickle", "rb") as f:
        model_reason = pickle.load(f)

    with open(dir_path + "/models/scaler.pickle", "rb") as f:
        scaler = pickle.load(f)

    # Register API endpoints
    from ChurnApp.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

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
