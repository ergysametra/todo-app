from flask_testing import TestCase
from application import app, db
from application.models import Tasks
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all() # create table schema
        db.session.add(Tasks(description="Run unit tests"))
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assert200(response)

    def test_create_task_get(self):
        response = self.client.get(url_for("create_task"))
        self.assert200(response)
    
        
class TestRead(TestBase):
    
    def test_read_home_tasks(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Run unit tests", response.data)
        

class TestCreate(TestBase):

    def test_create_task(self):
        response = self.client.post(
            url_for("create_task"),
            data={"description": "Testing create functionallity"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionallity", response.data)
        
