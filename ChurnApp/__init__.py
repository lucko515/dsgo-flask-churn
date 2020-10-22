import os
import pickle
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))

# Third party libraries
from flask import Flask

from flask import render_template, request, jsonify


with open(dir_path + "/models/churn_prediction.pickle", "rb") as f:
    model = pickle.load(f)

with open(dir_path + "/models/reason_prediction.pickle", "rb") as f:
    model_reason = pickle.load(f)

with open(dir_path + "/models/scaler.pickle", "rb") as f:
    scaler = pickle.load(f)


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


@app.route("/api/v1/predict", methods=['POST'])
def predict():
    data = {'account_length': None,
            'international_plan': None,
            'voice_mail_plan': None,
            'number_vmail_messages': None,
            'total_day_minutes': None,
            'total_day_calls': None,
            'total_day_charge': None,
            'total_eve_minutes': None,
            'total_eve_calls': None,
            'total_eve_charge': None,
            'total_night_minutes': None,
            'total_night_calls': None,
            'total_night_charge': None,
            'total_intl_minutes': None,
            'total_intl_calls': None,
            'total_intl_charge': None,
            'number_customer_service_calls': None,
            }

    for key in data.keys():
        try:
            entry = int(request.form[key])
        except:
            entry = 0

        data[key] = entry

    data = np.array(list(data.values())).reshape(1, -1)

    scaled_values = scaler.transform(data)
    churn_prediction = model.predict(scaled_values)

    churn_reason = [[]]
    if churn_prediction[0] == 1:
        churn_reason = model_reason.predict_proba(scaled_values)

    return jsonify({"churn_prediction": "No" if churn_prediction[0] == 0 else "Yes", "churn_reason": list(churn_reason[0])})


if __name__ == "__main__":
    app.run()
