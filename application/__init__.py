from flask import Flask
from flask_cors import CORS
from index import app

app = Flask(__name__)
CORS(app)
