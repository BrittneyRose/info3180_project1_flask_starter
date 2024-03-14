from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileField, FileAllowed

class AddPropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])
    room_num = StringField('No. of Rooms', validators=[InputRequired()], render_kw={"placeholder": " 3"})
    bathroom_num = StringField('No. of Bathrooms', validators=[InputRequired()], render_kw={"placeholder": " 2"})
    price = StringField('Price', validators=[InputRequired()], render_kw={"placeholder": " 15,000,000"})
    property_type = SelectField('Property Type', validators=[InputRequired()], choices=[('House', 'House'), ('Apartment', 'Apartment')])
    location = StringField('Location', validators=[InputRequired()], render_kw={"placeholder": " 10 Waterloo Rd"})
    file = FileField('Photo', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Photo')])