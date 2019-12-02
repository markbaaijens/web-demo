from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired

class EditBookForm(FlaskForm):
    # TODO Validate on length
    # TODO Use selectorfield 
    # TODO Make field Id readonly
    id = IntegerField('Id', validators=[DataRequired()], render_kw={'readonly': True})
    name = StringField('Name', validators=[DataRequired()])
    price = DecimalField('Price', places=2)
    isbn = IntegerField('ISBN', validators=[DataRequired()])
    submit = SubmitField('Save')