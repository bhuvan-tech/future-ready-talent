# installing libraries flask, scikit-learn, pandas, pickle-mixin
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
data = pd.read_csv("Cleaned_House_data.csv")


@app.route('/')
def ml():
    locations = sorted(data['location'].unique())
    return render_template('ml.html', locations=locations)


@app.route('/predict', methods=['POST'])
def predict():
    return ""


if __name__ == '__main__':
    app.run(debug=True, port=5001)
