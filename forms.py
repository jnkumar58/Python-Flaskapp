from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError

class ContactForm(Form):
   name = TextField(" Enter Your Name",[validators.Required("Please enter your name.")])
   color = TextField("Enter Your Favorite Color",[validators.Required("Please enter your Color.")])
   pet = RadioField('Select You Pet', choices = [('Cat','Cat'),('Dog','Dog')],default='Cat')
   resultMessage =""
   result = False
   submit = SubmitField("Send")
