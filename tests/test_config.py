from flask import current_app
from flask_testing import TestCase

from MyApp import create_app
app = create_app()


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.development.Config')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'you-will-never-guess')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        # self.assertTrue(
        #     app.config['SQLALCHEMY_DATABASE_URI'] ==
        #     'mysql+pymysql://root:wxx1512@localhost:3306/learning_flask'
        # )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.testing.Config')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'you-will-never-guess')
        self.assertTrue(app.config['DEBUG'])
        # self.assertTrue(
        #     app.config['SQLALCHEMY_DATABASE_URI'] ==
        #     'mysql+pymysql://root:wxx1512@localhost:3306/learning_flask'
        # )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.production.Config')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'you-will-never-guess')
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])
