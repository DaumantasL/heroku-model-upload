# heroku-model-upload

A model deployment exercise. This repository is designed to upload a pre-trained model using sklearn's [Boston Houses](https://scipy-lectures.org/packages/scikit-learn/auto_examples/plot_boston_prediction.html) dataset as a Heroku app. It technically does prediction, but being deploy-ready is the point.

# Deployment

To deploy from GitHub, follow [Heroku documentation](https://devcenter.heroku.com/articles/github-integration).

# Webapp requirements

Webapp api tested with the requests and json libraries, but can likely be used by anything that can send json to an url and receive the response.

# Using the webapp

## Deployed model validation

Checks if deployed model predictions match test environment.

 ```
import requests
import json
api_url = 'https://turing-model-deploy.herokuapp.com/validation'
resp = requests.get(api_url, data=json.dumps(testdata))
resp.text
 ```


## Data inputs

Webapp takes json as data input. A dictionary is used to construct the json.

The necessary dictionary key is specific and needs to be "inputs". The dictionary value is a list (any length) of lists (13 items exactly) of float values.

```
from sklearn.datasets import load_boston
import numpy as np
data = load_boston().data
batchsize = 20
data = data[:batchsize].tolist()
data = {'inputs': testdata}
```
 
## Prediction

Use the https://turing-model-deploy.herokuapp.com/predict url and correctly formatted Data inputs (see above), receive a response in json of the form 

```
api_url = 'https://turing-model-deploy.herokuapp.com/predict'
resp = requests.post(api_url, data=json.dumps(testdata))
resp.json()
```
