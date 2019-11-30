from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EditBookForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    price = StringField('Price')
    isbn = StringField('ISBN', validators=[DataRequired()])
    submit = SubmitField('Save')