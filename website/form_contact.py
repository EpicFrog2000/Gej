from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField('Imie', validators=[DataRequired('Nazwa nie może być pusta')])
    email = "tasarz_norbert@wp.pl"
    subject = StringField('Temat', validators=[DataRequired('Temat nie może być pusty')])
    message = TextAreaField('Wiadomość', validators=[DataRequired('Wiadomość nie może być pusta')])
    submit = SubmitField("Wyślij")