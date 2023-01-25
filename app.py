#Les importations des packages 
from flask import Flask
from flask_cors import CORS,cross_origin

app = Flask(__name__)

#Pour appliquer le cors sur l'appllication
CORS(app)