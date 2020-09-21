import flask
from application import db

class Contact(db.Document):
    name = db.StringField(max_length = 50)
    ph_num = db.StringField(max_length = 50)
    address = db.StringField(max_length = 50)
    email = db.StringField(max_length = 30)