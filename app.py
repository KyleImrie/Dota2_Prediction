from io import BytesIO

import numpy as np

from flask import Flask, request, json
import boto3

BUCKET_NAME = 'ds-dota-bucket'
WIN_RATES = 'hero_win_rate.json'
MODEL = 'test.model'

app = Flask(__name__)

dev = boto3.session.Session()
s3_bucket = dev.resource('s3').Bucket(BUCKET_NAME)


@app.route('/', methods=['POST'])
def index():
    # Parse request body for model input
    body_dict = request.get_json(silent=True)
    raw_data = body_dict['data']
    processed_data = _process_data(raw_data)

    # Load model
    model = _load_model()

    parameters = np.array(model['parameters'])
    offset = np.array(model['offset'])

    # Make prediction
    prediction = _sigmoid(np.dot(processed_data, parameters) + offset)
    # Respond with prediction result
    result = {'prediction': prediction.tolist()}

    return json.dumps(result)


def _process_data(data):
    buf = BytesIO()
    s3_bucket.download_fileobj(Key=WIN_RATES, Fileobj=buf)
    win_rates = json.loads(buf.getvalue())

    radiant_win_rates = [_get_win_rate(hero, win_rates) for hero in data[:5]]
    dire_win_rates = [_get_win_rate(hero, win_rates) for hero in data[5:]]

    return sorted(radiant_win_rates) + sorted(dire_win_rates)


def _get_win_rate(hero, win_rates):
    try:
        return win_rates[str(hero)]
    except KeyError:
        return 0.50


def _load_model():
    buf = BytesIO()
    s3_bucket.download_fileobj(Key=MODEL, Fileobj=buf)
    model = json.loads(buf.getvalue())
    return model


def _sigmoid(z):
    return 1/(1+np.exp(z))


if __name__ == '__main__':
    # listen on all IPs
    app.run(host='0.0.0.0')
