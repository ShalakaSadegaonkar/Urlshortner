from flask_wtf import FlaskForm  # , RecaptchaField
from wtforms import validators, StringField
from wtforms.validators import Length
# from wtforms.fields.html5 import URLField


class UrlForm(FlaskForm):
    old = StringField('Title', [
        validators.InputRequired(),
        validators.Length(
            min=4, max=2040, message="Enter proper url")
    ])
    
    def save_url(self, url):
        self.populate_obj(url)
        if not "http" in url.old:
            url.old = "https://" + url.old
        if not "." in url.old:
            url.old = url.old + ".com/"
        return url
