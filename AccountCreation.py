import re as Regex
import DataBaseSchemaClasses as Schema
import ProgUtilities as Util



# first we're gonna create the general account creation
# then we're gonna grab accounts to check them out and make sure we don't have dupes


# Note to self: might wanna add automatic cutoff to this? After 3-5 attempts stop the program? Obviously this works a lot better in a GUI setting but that shouldn't deter me
# Note again: Might be a good idea to handle the whole Regex check in another function? this function should probably just CREATE accounts, not create and check them. Maybe function for input/output groups too.
# desc: CreateAccount Allows the user to create an 'account' consisting of a Tuple of email, username and password. Note that this only accepts reasonable email addresses (can change to actually send a request later maybe?)
# and a password of any length with at least one numeral and one uppercase letter (should probably have a min size as well)
# pre: dictionary to store in exists, which requires an 'accounts' file to either exist or be created on startup (usually by just creating a blank dictionary)
# post: New dictionary of a single account is added to the dictionary of accounts to be saved an 'accounts' file.
def CreateAccount(account_dict):
    valid_pass = False
    valid_email = False
    valid_name = False
    ## use the email regex for emails
    #while valid_name == False and valid_pass == False and valid_email == False:
    while valid_email == False:
            print("Input your email: ")
            email_to_check = input()
            valid_email = Util.ValidateEmail(email_to_check)
    while valid_name == False:
            print("Input your desired username: ")
            possible_name = input()
            valid_name = Util.ValidateUser(possible_name)
    while valid_pass == False:
            print("Input your desired password: ")
            possible_pass = input()
            valid_pass = Util.ValidatePass(possible_pass)
    if email_to_check not in account_dict and possible_name not in account_dict:
        user_dict = Util.AccountToDictionary(account_dict,email_to_check,possible_name,possible_pass)
        return account_dict

def CreateAccount():
    valid_pass = False
    valid_email = False
    valid_name = False
    ## use the email regex for emails
    # while valid_name == False and valid_pass == False and valid_email == False:
    while valid_email == False:
        print("Input your email: ")
        email_to_check = input()
        valid_email = Util.ValidateEmail(email_to_check)
    while valid_name == False:
        print("Input your desired username: ")
        possible_name = input()
        valid_name = Util.ValidateUser(possible_name)
    while valid_pass == False:
        print("Input your desired password: ")
        possible_pass = input()
        valid_pass = Util.ValidatePass(possible_pass)
    if email_to_check not in Schema.Users.objects.filter(email=email_to_check) and possible_pass not in Schema.Users.objects.filter(email=possible_name):
        database_doc = Util.AccountToMongoDocument(email_to_check,possible_name,possible_pass)
        return database_doc



