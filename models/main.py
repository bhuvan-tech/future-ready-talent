# installing libraries flask, scikit-learn, pandas, pickle-mixin
import os

import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
data = pd.read_csv("Cleaned_House_data.csv")
pipe = pickle.load(open("Linearregressionmodel.pk1", 'rb'))


@app.route('/')
def ml():
    locations = sorted(data['location'].unique())
    return render_template('ml.html', locations=locations)


@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bathroom')
    tsqf = request.form.get('tqsf')

    print(location, bhk, bath, tsqf)
    input= pd.DataFrame([[location,tsqf,bath,bhk]], columns=['location', 'tsqf', 'bath', 'bhk'])
    prediction= pipe.predict(input)[0] * 1e5
    return str(np.round(prediction,2))


if __name__ == '__main__':
    port= os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)
