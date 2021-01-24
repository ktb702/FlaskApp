from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#must use the classes defined in wtforms
class AddTaskForm(FlaskForm):
    title = StringField('Task: ', validators=[DataRequired()]) #Title will be the label, validates that the form field is not empty
    submit = SubmitField('Submit')

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete')

