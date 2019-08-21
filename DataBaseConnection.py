from pymongo import MongoClient
from mongoengine import *
import DataBaseSchemaClasses as Schema

#=====PYMONGO CONNECTIVITY STUFF STARTS HERE=====
def pymongo_connect():
    # Explicit MongoDB URI call to localhost; can change this to a server if you want.
    client = MongoClient('mongodb://localhost:27017')

    #access the specific DB you want to use:
    db = client['LoginDBTest']

#Test functions to see if the database connects properly. Maybe put in another file or remove later, but until then I think this is a good enough spot for them.
def pymongo_db_test(database):
    users = database.Users
    user_data = {
        'email': 'Test@test.com',
        'username': 'Test',
        'password': 'P455w0rD'
    }
    result = users.insert_one(user_data)
    print('One post: {0}'.format(result.inserted_id))


#=====MONGOENGINE CONNECTIVITY STUFF STARTS HERE=====
def mongoengine_connect():
    connect('LoginDBTest', host='localhost', port=27017)

def mongoengine_db_test():
    User_test = Schema.Users(
        email='Pizza2@gmail.com',
        username='Pizza2',
        password='H3Y Guys'
    )
    User_test.save()
    print(User_test.email)