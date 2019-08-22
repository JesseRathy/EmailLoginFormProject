import re as Regex
import DataBaseSchemaClasses as Schema


# AccountToDictionary
# Description: Takes an account created (usually by CreateAccount, but can be done by other things as well and converts it to a dictionary where the primary key is the e-mail account
# and the secondary keys are the name and password of the users.
# pre: email, name and password have all been created
def AccountToDictionary(account_dict,email,name,pw):
    account_dict['Users'].append({
        'email' : email,
        'username' : name,
        'password': pw
    })
    return account_dict

def AccountToMongoDocument(email,username,password):
   our_user =Schema.Users(
        email=email,
       username=username,
       password=password
    )
   return our_user


# Helper functions for validation in account creation (b/c I'm tired of looking at this disasterpiece)
def ValidateEmail(email_to_check):
    valid_email = False
    email_regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not (Regex.match(email_regex, email_to_check)):
        print("This is not a valid email address! Please try again!")
    else:
        valid_email = True
    return valid_email

def ValidateUser(possible_name):
    valid_name = False
    user_regex = "(^[a-zA-Z0-9_.+-]+$)"
    if not (Regex.match(user_regex, possible_name)):
        print("This is not a valid username! Please try again!")
    else:
        valid_name = True
    return valid_name

def ValidatePass(possible_pass):
    has_uppercase = False
    has_number = False
    valid_pass = False
    if not (Regex.search('[A-Z]', possible_pass)):
        print("This password requires a capital letter! Please try again!")
    else:
        has_uppercase = True
    if not (Regex.search('[0-9]', possible_pass)):
        print("This password requires a number! Please try again!")
    else:
        has_number = True
    if (has_uppercase == True and has_number == True):
        valid_pass = True
    return valid_pass