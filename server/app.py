from flask import Flask, jsonify, request

from middleware import init_middleware
from model import init_db
from router import init_router

app = Flask(__name__)
init_router(app)
init_middleware(app)
init_db(app)


if __name__ == '__main__':
    app.run(debug=True)