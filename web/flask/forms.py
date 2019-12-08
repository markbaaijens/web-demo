from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, BooleanField, RadioField
from wtforms.validators import Length, InputRequired, NumberRange, Required

from enums import BookType

# TODO Use selectorfield, datefield, etc.
# TODO Move validators to a different file: https://exploreflask.com/en/latest/forms.html
# TODO Check for unique name: https://exploreflask.com/en/latest/forms.html

class EditBookForm(FlaskForm):
    id = IntegerField('Id', render_kw={'readonly': True})
    name = StringField('Name')
    price = DecimalField('Price', places=2)
    isbn = IntegerField('ISBN')
    obsolete = BooleanField('Obsolete')
    bookType = IntegerField('Type')
    submit = SubmitField('Save')

    # Not using standard validators like Required b/c they do not show custom message; this is overruled by HTML5
    def validate_name(self, field):
        if field.data == '':  
            raise ValueError('Field is required')
        if len(field.data) > 50:
            raise ValueError('Maximum size is 5 characters')
        pass

    def validate_isbn(self, field):
        if field.data < 1 or field.data > 10000 - 1:
            raise ValueError('Value must be between 1 and 9999')
        pass

class DeleteBookForm(FlaskForm):
    submit = SubmitField('Delete')