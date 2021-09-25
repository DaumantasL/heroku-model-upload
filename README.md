# heroku-model-upload

A model deployment exercise. This repository is designed to upload a pre-trained model using sklearn's [Boston Houses](https://scipy-lectures.org/packages/scikit-learn/auto_examples/plot_boston_prediction.html) dataset as a Heroku app. It technically does prediction, but being deploy-ready is the point.

# Webapp requirements

Webapp api tested with the requests and json libraries, but can likely be used by anything that can send json to an url and receive the response.

# Expected API data input

POST request to https://turing-model-deploy.herokuapp.com/predict. Takes JSON in the following data format:

Single prediction:

 ```
{'inputs': [0.05425, 0.0, 4.05, 0.0, 0.51, 6.315, 73.4, 3.3175, 5.0, 296.0, 16.6, 395.6, 6.29]}
```

Batch:

```
{'inputs': [[0.05188, 0.0, 4.49, 0.0, 0.449, 6.015, 45.1, 4.4272, 3.0, 247.0, 18.5, 395.99, 12.86],
  [0.85204, 0.0, 8.14, 0.0, 0.538, 5.965, 89.2, 4.0123, 4.0, 307.0, 21.0, 392.53, 13.83],
  [9.18702, 0.0, 18.1, 0.0, 0.7, 5.536, 100.0, 1.5804, 24.0, 666.0, 20.2, 396.9, 23.6]]}
```

# Output

POST request to https://turing-model-deploy.herokuapp.com/predict outputs JSON in the following format:

```
{'predicted_prices': [21.69999930887597]}
```


## Deployed model validation

Checks if deployed model predictions match test environment. GET request to https://turing-model-deploy.herokuapp.com/validation

Expected JSON output:
 ```
{"validation": "Model deployment works as expected."}
 ```
