from flask import Flask, request
import json
import numpy as np
import pickle
import os


app = Flask(__name__)

model_filename="models/houses_model.pkl"
modelfile = open(model_filename, "rb")
model = pickle.load(modelfile)
modelfile.close()

valid_data_filename = "models/valid_X.pkl"
valid_Xfile = open(valid_data_filename, "rb")
valid_X = pickle.load(valid_Xfile)
valid_Xfile.close()

valid_predict_filename = "models/valid_y.pkl"
valid_yfile = open(valid_predict_filename, "rb")
valid_y = pickle.load(valid_yfile)
valid_yfile.close()

model_valid = np.array_equiv(valid_y, model.predict(valid_X))


def __process_input(request_data: str) -> np.array:
    '''Changes input list into an numpy array.'''
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    assert len(parsed_body.shape) in (1, 2)
    assert parsed_body.shape[-1] == 13
    if len(parsed_body.shape) == 1:
        return parsed_body.reshape(1, -1)
    else:
        return parsed_body


@app.route("/validation", methods=["GET"]) 
def validation() -> str:
    '''Checks if deployed model makes the same prediction as in training environment.'''
    if model_valid is True:
        return json.dumps({"validation": "Model deployment works as expected."}), 200
    else:
        return json.dumps({"error": "Model deployment does not work as expected."}), 400


@app.route("/predict", methods=["POST"])
def predict() -> str:
    '''Returns house price predictions in a json format.'''
    try:
        input_params = __process_input(request.data)
        predictions = model.predict(input_params)
        return json.dumps({"predicted_prices": predictions.tolist()}), 200
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except:
        return json.dumps({"error": "PREDICTION FAILED"}), 500
        

if __name__ == '__main__':
    app.run(port=int(os.getenv('PORT')), debug=False)
