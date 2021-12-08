from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    description = StringField("Task Description", validators=[DataRequired()])
    submit = SubmitField("Add Task")

