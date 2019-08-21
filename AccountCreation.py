import re as Regex




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
            valid_email = ValidateEmail(email_to_check)
    while valid_name == False:
            print("Input your desired username: ")
            possible_name = input()
            valid_name = ValidateUser(possible_name)
    while valid_pass == False:
            print("Input your desired password: ")
            possible_pass = input()
            valid_pass = ValidatePass(possible_pass)
    if email_to_check not in account_dict and possible_name not in account_dict:
        user_dict = AccountToDictionary(account_dict,email_to_check,possible_name,possible_pass)
        #account_dict[email_to_check] = user_dict
        #my_tuple = tuple((email_to_check, possible_name, possible_pass))
        #print(my_tuple)
        #account_dict.append(my_tuple)
        return account_dict
# AccountToDictionary
# Description: Takes an account created (usually by CreateAccount, but can be done by other things as well and converts it to a dictionary where the primary key is the e-mail account
# and the secondary keys are the name and password of the users.
# pre: email, name and password have all been created
def AccountToDictionary(account_dict,email,name,pw):

    account_dict['Users'].append({
        'Email' : email,
        'Name' : name,
        'Password': pw
    })
    return account_dict

#def AccountTo

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
