from flask import Flask

from router.worker import bp


def init_router(app:Flask):
    app.register_blueprint(bp)
