import requests
from flask import Flask
from werkzeug.wrappers import Request, Response
import json
import numpy as np
import pickle
model_filename="models/houses_model.pkl