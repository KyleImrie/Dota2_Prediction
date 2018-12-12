import numpy as np

from flask import Flask, request, json
import boto3
from sklearn.externals import joblib

BUCKET_NAME = 'ds-dota-bucket'
MODEL_FILE_NAME = 'logistic_model.pkl'

app = Flask(__name__)

dev = boto3.session.Session(profile_name='kyle')
s3_bucket = dev.resource('s3').Bucket(BUCKET_NAME)


@app.route('/', methods=['POST'])
def index():
    # Parse request body for model input
    body_dict = request.get_json(silent=True)
    data = np.array(body_dict['data']).reshape(1, -1)

    # Load model
    model = load_model(MODEL_FILE_NAME)

    # Make prediction
    prediction = model.predict(data).tolist()
    # Respond with prediction result
    result = {'prediction': prediction}

    return json.dumps(result)


def load_model(key):
    with open('model.pkl', 'wb') as data:
        s3_bucket.download_fileobj(key, data)

    model = joblib.load('model.pkl')

    return model


if __name__ == '__main__':
    # listen on all IPs
    app.run(host='0.0.0.0')
