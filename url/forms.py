from flask_wtf import FlaskForm  
from wtforms import validators, StringField
from wtforms.validators import Length



class UrlForm(FlaskForm):
    old = StringField('Title', [
        validators.InputRequired(),
        validators.Length(
            min=4, max=2040, message="Enter proper url")
    ])
    
    def save_url(self, url):
        self.populate_obj(url)
        return url
