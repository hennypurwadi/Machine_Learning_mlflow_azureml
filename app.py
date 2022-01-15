
import sklearn
import scipy
import numpy as np
import pandas as pd
import csv
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import IsolationForest
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import json
import joblib

app = Flask(__name__)

@app.route("/status")
def status():
    return "success"

@app.route("/", methods=['GET', 'POST'])
def index():
    A1 = request.args.get("A1", None)
    A2 = request.args.get("A2", None)

    #request_value = request.get_json()

    #A1 = int(request_value["A1"])
    #A2 = int(request_value["A2"])

    if A1 != None:
        y_new = predict(A1, A2)
    else:
        y_new = ""

    write(A1, A2, y_new)
    return (
        """<form action="" method="get">
                A1 input: <input type="text" name="A1">
                A2 input: <input type="text" name="A2">
                <input type="submit" value="A1 & A2 input for Predict Fraud or Not">
            </form>"""

        + "y_new: "
        + str(y_new)
    )

@app.route("/json", methods=['GET', 'POST'])
def jsonify():
    request_value = request.get_json()
    return request_value

def write(A1, A2, y_new):
    filedf = "fraud_detector.csv"
    # write new data into csv
    with open(filedf, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([A1, A2, y_new])
        print("file written")

def predict(A1, A2):
    """Predict Fraud or Not Fraud."""
    print("predicting")

    model = joblib.load(open("model.pkl", 'rb'))
    X_new = np.array([A1, A2]).reshape(1, -1)
    y_new = model.predict(X_new)

    y_new[y_new == 1] = 0  # normal
    y_new[y_new == -1] = 1  # possibly fraud

    y_new = (int(y_new))
    return y_new

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True, use_reloader=False)
