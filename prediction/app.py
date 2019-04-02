from io import BytesIO

import numpy as np

from flask import Flask, request, json
import boto3

BUCKET_NAME = 'ds-dota-bucket'
MODEL = 'test.model'

app = Flask(__name__)

dev = boto3.session.Session()
s3_bucket = dev.resource('s3').Bucket(BUCKET_NAME)


@app.route('/', methods=['POST'])
def index():
    # Parse request body for model input
    body_dict = request.get_json(silent=True)
    data = np.array(body_dict['data']).reshape(1, -1)

    # Load model
    model = _load_model(MODEL)

    parameters = np.array(model['parameters'])
    offset = np.array(model['offset'])

    # Make prediction
    prediction = _sigmoid(np.dot(data, parameters) + offset)
    # Respond with prediction result
    result = {'prediction': prediction.tolist()}

    return json.dumps(result)


def _load_model(key):
    buf = BytesIO()
    s3_bucket.download_fileobj(Key=key, Fileobj=buf)
    model = json.loads(buf.getvalue())
    return model


def _sigmoid(z):
    return 1/(1+np.exp(z))


if __name__ == '__main__':
    # listen on all IPs
    app.run(host='0.0.0.0')
