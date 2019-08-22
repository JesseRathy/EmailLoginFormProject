from mongoengine import *

import datetime

class Users(Document):
    email = StringField(unique=True, required=True, max_length=200)
    username = StringField(unique=True, required=True, max_length=50)
    password = StringField(required=True, max_length=50)
    created = DateTimeField(default=datetime.datetime.now)
    meta = {'collection': "Users"}
