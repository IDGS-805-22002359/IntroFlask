from wtforms import Form, StringField, SubmitField, FieldList, RadioField, SelectField, IntegerField, PasswordField, EmailField
from flask_wtf import FlaskForm

class Alumno(Form):
    
    matricula = StringField('Matrícula')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('Email')
    password = PasswordField('Contraseña')
    