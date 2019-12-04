from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired

# TODO Validate on length
# TODO Validate on no characters is numerical fields
# TODO Use selectorfield, datefield, etc.

class ShowBookForm(FlaskForm):
    id = IntegerField('Id', render_kw={'readonly': True})
    name = StringField('Name', render_kw={'readonly': True})
    price = DecimalField('Price', render_kw={'readonly': True})
    isbn = IntegerField('ISBN', render_kw={'readonly': True})

class EditBookForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()], render_kw={'readonly': True})
    name = StringField('Name', validators=[DataRequired()])
    price = DecimalField('Price', places=2)
    isbn = IntegerField('ISBN', validators=[DataRequired()])
    submit = SubmitField('Save')

class DeleteBookForm(FlaskForm):
    id = IntegerField('Id', render_kw={'readonly': True})
    name = StringField('Name', render_kw={'readonly': True})
    submit = SubmitField('Delete')