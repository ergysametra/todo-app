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
    def test_read_tasks(self):
        response = self.client.get(url_for('read_task'))
        self.assert200(response)
    def test_update_task_get(self)
        response = self.client.get(url_for('update_task', id=1))
        
class TestRead(TestBase):
    
    def test_read_tasks(self):
        response = self.client.get(url_for("home"))
        self.assertIn("Test the application", str(response.data))
    def tst_read_home_tasks(self):
        response = self.client.get(url_for('read_tasks'))
        self.assertIn(b"Run unit tests", response.data)
        

class TestCreate(TestBase):

    def test_create_task(self):
        response = self.client.post(
            url_for("create_task"),
            data={"description": "Testing create functionallity"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionallity", response.data)
        
 class TestUpdate(TestBase):
    response =self.client.post(
        url_for('update_task', id=1),
        data={"description": "Testing update funcionality"},
        follow_redirects=True
    )
    self.assertIn(b"Testing update functionallity", response.data)  
    
   def test_complete_task(self:
     response =self.client.get(url_for('complete_task', id=1), follow_redirects=True)
     self.assertEqual(Tasks.query.get(1).completed, True)
                          
                          
 class TestDelete(Testbase):
    
    def test_delete_task(self:
        response =self.client.get(
            url_for('delete_task', id=1),
            follow_redirects=True
             )
        self.assertIn(b"Run unit tests", response.data

    
