import DataBaseConnection as db_connect
import AccountIO as AccIO
import DataBaseSchemaClasses as Schema
import AccountCreation as Acc
import os.path as path
from mongoengine import *
auto_cancel = 4
account_dict = {}
account_dict['Users'] = []

def sign_in():
    global auto_cancel
    while (auto_cancel > 0):
        print("What is your Username?")
        givenUser = input()
        print("What is your Password?")
        givenPass = input()
       # for key,val in acc_dict
        if (db_validation(givenUser,givenPass) == True):
            #We'll just echo A true or false thing here until we figure out what to do.
            print("Welcome to the Program!")
            return
        else:
            print("Please Try again!")
            auto_cancel = auto_cancel - 1

# this makes it easy to change validation if you want; don't have to go
# into the sign_in code to do it, just change this piece of the code
# This makes it easy to change it across all sign-ins if you use the validation
# to validate
def file_validation(Users,UGiven,PGiven):
    for key,val in Users.items():
        for i in val:
            if i["Name"] == UGiven and i["Password"] == PGiven:
    #if (UAct == UGiven and PAct == PGiven):
                return True
    else:
        return False

def db_validation(UGiven,PGiven):
    try:
        our_user = Schema.Users.objects.get(username=UGiven)
        if our_user.username == UGiven and our_user.password == PGiven:
            return True
        else:
            return False
    except Schema.DoesNotExist:
        print("The User you are trying to access does not exist!")
        return False
    except Schema.MultipleObjectsReturned:
        print("Somehow, Multiple Possible accounts with the same name exist! Please contact an administrator to fix this error!")
        return False
#MongoDBTest(db)
db_connect.mongoengine_connect()
#Test_User = Acc.CreateAccount()
#AccIO.SaveDataBaseDocument(Test_User)
users = AccIO.GrabAllDBDocuments()
for i in users:
    print(i.email + ", " + i.username + "," + i.password)
#AccIO.ChangeUserName("deathgripz@gmail.com")
#AccIO.DeleteUser("Jesse@mail.org")
#db_connect.mongoengine_db_test()
#if path.isfile('test.json'):
#    account_dict = Acc.LoadAcccountFile('test')
sign_in()
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







