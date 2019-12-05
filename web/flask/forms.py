from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import InputRequired, Length

# TODO Validate on length
# TODO Validate on no characters is numerical fields
# TODO Use selectorfield, datefield, etc.

class EditBookForm(FlaskForm):
    id = IntegerField('Id', validators=[InputRequired()], render_kw={'readonly': True})
    name = StringField('Name', validators=[InputRequired(message='Name is required'), Length(max=5, min=3)])
    price = DecimalField('Price', places=2)
    isbn = IntegerField('ISBN', validators=[InputRequired(message='ISBN is required'), Length(max=5, min=3)])
    submit = SubmitField('Save')

class DeleteBookForm(FlaskForm):
    submit = SubmitField('Delete')