import requests
from flask import Flask
from werkzeug.wrappers import Request, Response
import json
import numpy as np
import pickle
from sklearn.ensemble import GradientBoostingRegressor


app = Flask(__name__)

model_filename="models/houses_model.pkl"
model = pickle.load(open(model_filename, "rb"))

valid_data_filename = "models/valid_X.pkl"
valid_X = pickle.load(open("models/valid_X.pkl", "rb"))

valid_predict_filename = "models/valid_y.pkl"
valid_y = pickle.load(open("models/valid_y.pkl", "rb"))

model_valid = np.array_equiv(valid_y, model.predict(valid_X))

def __process_input(request_data: str) -> np.array:
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    assert len(parsed_body.shape) in (1, 2)
    assert parsed_body.shape[-1] == 13
    return parsed_body

@app.route("/predict", methods=["POST"])
def predict() -> str:
    if model_valid == False:
        return json.dumps({"error": "Model validation failed."}), 400
    else:
        try:
            input_params = __process_input(request.data)
            predictions = model.predict(input_params)
            return json.dumps({"predicted_prices": predictions.tolist()}), 200
        except (KeyError, json.JSONDecodeError, AssertionError):
            return json.dumps({"error": "CHECK INPUT"}), 400
        except:
            return json.dumps({"error": "PREDICTION FAILED"}), 500

if __name__ == '__main__':
    app.run(port = 5000, debug=False)
#port = int(os.getenv('PORT'))
