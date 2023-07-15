from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


# Sign-up forms
class AddGameForm(FlaskForm):
    # Meta
    steam_id = StringField('Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    release_date = StringField('Release Date', validators=[DataRequired()])
    product_type = StringField('Product Type', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    
    # Images
    link_header = StringField('link_header', validators=[DataRequired()])
    capsule_image = StringField('capsule_image', validators=[DataRequired()])
    capsule_imagev5 = StringField('capsule_imagev5', validators=[DataRequired()])

    # Price
    price = StringField('link_header', validators=[DataRequired()])
    on_sale = BooleanField('on_sale')
    discount_price = StringField('discount_price', validators=[DataRequired()])
    discount_percent =  StringField('discount_percent', validators=[DataRequired()])