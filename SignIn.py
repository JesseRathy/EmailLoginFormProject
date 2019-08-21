import AccountCreation as Acc
import os.path as path
from pymongo import MongoClient
from mongoengine import *

import datetime
auto_cancel = 4
account_dict = {}
account_dict['Users'] = []

connect('LoginDBTest',host='localhost',port=27017)

#Explicit MongoDB URI call to localhost; can change this to a server if you want.
client = MongoClient('mongodb://localhost:27017')

#access the specific DB you want to use:
db = client['LoginDBTest']

class _Users(Document):
    email = StringField(unique=True,required=True,max_length=200)
    username = StringField(unique=True,required=True,max_length=50)
    password = StringField(required=True,max_length=50)
    created = DateTimeField(default=datetime.datetime.now)

def mongoDBTest(database):
    users = database.Users
    user_data = {
        'email': 'Test@test.com',
        'username': 'Test',
        'password': 'P455w0rD'
    }
    result = users.insert_one(user_data)
    print('One post: {0}'.format(result.inserted_id))

def MongoEngineTest():
    User_test = _Users(
        email='Pizza1@gmail.com',
        username='Pizza1',
        password='F1FTy0n3'
    )
    User_test.save()
    print(User_test.email)




def sign_in(acc_dict):
    global auto_cancel
    while (auto_cancel > 0):
        print("What is your Username?")
        givenUser = input()
        print("What is your Password?")
        givenPass = input()
       # for key,val in acc_dict
        if (validation(acc_dict,givenUser,
            givenPass) == True):
            #We'll just echo A true or false thing here
            print("Welcome to the Program!")
            return
        else:
            print("Please Try again!")
            auto_cancel = auto_cancel - 1

# this makes it easy to change validation if you want; don't have to go
# into the sign_in code to do it, just change this piece of the code
# This makes it easy to change it across all sign-ins if you use the validation
# to validate
def validation(Users,UGiven,PGiven):
    for key,val in Users.items():
        for i in val:
            if i["Name"] == UGiven and i["Password"] == PGiven:
    #if (UAct == UGiven and PAct == PGiven):
                return True
    else:
        return False

#MongoDBTest(db)
MongoEngineTest()
#if path.isfile('test.json'):
#    account_dict = Acc.LoadAcccountFile('test')
#sign_in(account_dict)
#account_dict = Acc.CreateAccount(account_dict)
#accounts = Acc.CreateAccount(accounts)
#Acc.SaveAccountFile(account_dict,"test")
#account_dict = Acc.LoadAcccountFile('test')
#HOW TO LOOK FOR SPECIFIC EMAILS
#for key,val in account_dict.items():
#       for i in val:
#           print(i["Email"])
           #do whatever else you need I guess

    ##TODO:
    ## Change this Tuple mess into a 2-dictionary system:
    ## One large dictionary made up of smaller dictionaries, where each new dictionary's
    ## key is the email associated with the account; then have username and password fields
    ## in each dictionary. The account creation function can take care of this, or you can make another
    ## function to turn this stuff into dictionaries and insert it (probably a little more work but better in the end)
    ## Your choice.







