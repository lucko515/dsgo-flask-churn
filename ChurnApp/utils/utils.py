import os
import pickle
import datetime

import ChurnApp
from ChurnApp import dir_path


def model_loader():
    update = False
    if ChurnApp.last_loaded_models is not None:

        if datetime.datetime.fromtimestamp(os.path.getmtime(dir_path + "/models/churn_prediction.pickle")) > ChurnApp.last_loaded_models:
            with open(dir_path + "/models/churn_prediction.pickle", "rb") as f:
                ChurnApp.model = pickle.load(f)
            update = True

        if datetime.datetime.fromtimestamp(os.path.getmtime(dir_path + "/models/reason_prediction.pickle")) > ChurnApp.last_loaded_models:
            with open(dir_path + "/models/reason_prediction.pickle", "rb") as f:
                ChurnApp.model_reason = pickle.load(f)
            update = True

        if datetime.datetime.fromtimestamp(os.path.getmtime(dir_path + "/models/scaler.pickle")) > ChurnApp.last_loaded_models:
            with open(dir_path + "/models/scaler.pickle", "rb") as f:
                ChurnApp.scaler = pickle.load(f)
            update = True

        if update:
            ChurnApp.model_loaded_time = datetime.datetime.now()

    else:
        with open(dir_path + "/models/churn_prediction.pickle", "rb") as f:
            ChurnApp.model = pickle.load(f)

        with open(dir_path + "/models/reason_prediction.pickle", "rb") as f:
            ChurnApp.model_reason = pickle.load(f)

        with open(dir_path + "/models/scaler.pickle", "rb") as f:
            ChurnApp.scaler = pickle.load(f)

        ChurnApp.last_loaded_models = datetime.datetime.now()

