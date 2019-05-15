from flask import Flask
from flask import render_template, flash, redirect, url_for
from .forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config.default import Config
import os

db = SQLAlchemy()
APP_SETTINGS = os.environ.get("APP_SETTINGS")


def create_app():
    app = Flask(__name__)
    # 环境配置
    # app.config.from_object(APP_SETTINGS)
    app.config.from_object(Config)

    migrate = Migrate(app, db)

    # 安装扩展
    db.init_app(app)
    # 注册blueprint
    from MyApp.view import users_blueprint
    app.register_blueprint(users_blueprint)
    return app
