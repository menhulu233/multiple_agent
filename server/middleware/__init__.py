from flask import Flask

from middleware.cors import init_cors


def init_middleware(app:Flask):
    init_cors(app)
