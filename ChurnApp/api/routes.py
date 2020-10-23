
from ChurnApp.api import bp
from ChurnApp.utils.utils import model_loader
import ChurnApp

import numpy as np
from flask import request, jsonify


@bp.route("/v1/predict", methods=['POST'])
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

    model_loader()

    for key in data.keys():
        try:
            entry = int(request.form[key])
        except:
            entry = 0

        data[key] = entry

    data = np.array(list(data.values())).reshape(1, -1)

    scaled_values = ChurnApp.scaler.transform(data)
    churn_prediction = ChurnApp.model.predict(scaled_values)

    churn_reason = [[]]
    if churn_prediction[0] == 1:
        churn_reason = ChurnApp.model_reason.predict_proba(scaled_values)

    return jsonify({"churn_prediction": "No" if churn_prediction[0] == 0 else "Yes", "churn_reason": list(churn_reason[0])})

