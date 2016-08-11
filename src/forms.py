from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class LoginForm(Form):
    user = StringField('user', validators=[DataRequired()])
