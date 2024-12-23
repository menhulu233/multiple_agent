from flask import Flask
from flask_cors import CORS


def init_cors(app: Flask):
    CORS(app)
