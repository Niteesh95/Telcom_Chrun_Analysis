#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, jsonify
import pickle


# loading model to compare predicted values
dv, model_LR = pickle.load(open('LRmodel.bin','rb'))

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform(customer)
    y_pred = float(model_LR.predict_proba(X)[0, 1])
    churn = bool(y_pred > 0.5)
    result = {
            'churn_probability': y_pred,
            'churn': churn
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
