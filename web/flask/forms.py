from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired

class EditBookForm(FlaskForm):
    # TODO Validate on length
    # TODO Validate on no characters is numerical fields
    # TODO Use selectorfield, datefield, etc.
    id = IntegerField('Id', validators=[DataRequired()], render_kw={'readonly': True})
    name = StringField('Name', validators=[DataRequired()])
    price = DecimalField('Price', places=2)
    isbn = IntegerField('ISBN', validators=[DataRequired()])
    submit = SubmitField('Save')

class DeleteBookForm(FlaskForm):
    id = IntegerField('Id', render_kw={'readonly': True})
    name = StringField('Name', render_kw={'readonly': True})
    submit = SubmitField('Delete')