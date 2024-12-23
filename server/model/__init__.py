from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
db = SQLAlchemy()


def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/mydatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁用对模型修改的监控
    db.init_app(app)  # 初始化db实例
    migrate = Migrate(app, db)  # 初始化Flask-Migrate
