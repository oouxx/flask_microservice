from flask_testing import TestCase
from MyApp import db
from MyApp import create_app
app = create_app()


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.testing.Config')
        return app

    def setUp(self):
        from MyApp.models import User
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
