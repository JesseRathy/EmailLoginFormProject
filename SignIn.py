import AccountCreation as Acc
import os.path as path
auto_cancel = 4
account_dict = {}
account_dict['Users'] = []

def sign_in(actualUser,actualPass):
    global auto_cancel
    while (auto_cancel > 0):
        print("What is your Username?")
        givenUser = input()
        print("What is your Password?")
        givenPass = input()
        if (validation(actualUser,givenUser,
            actualPass,givenPass) == True):
            #We'll just echo A true or false thing here
            print("Welcome to the Program!")
            return
        else:
            print("Please Try again!")
            autoCancel  = autoCancel - 1

# this makes it easy to change validation if you want; don't have to go
# into the sign_in code to do it, just change this piece of the code
# This makes it easy to change it across all sign-ins if you use the validation
# to validate
def validation(UAct,UGiven,PAct,PGiven):
    if (UAct == UGiven and PAct == PGiven):
        return True
    else:
        return False

if path.isfile('test.json'):
    account_dict = Acc.LoadAcccountFile('test')
#account_dict = Acc.CreateAccount(account_dict)
#accounts = Acc.CreateAccount(accounts)
Acc.SaveAccountFile(account_dict,"test")
account_dict = Acc.LoadAcccountFile('test')
#HOW TO LOOK FOR SPECIFIC EMAILS
for key,val in account_dict.items():
       for i in val:
           print(i["Email"])
           #do whatever else you need I guess

    ##TODO:
    ## Change this Tuple mess into a 2-dictionary system:
    ## One large dictionary made up of smaller dictionaries, where each new dictionary's
    ## key is the email associated with the account; then have username and password fields
    ## in each dictionary. The account creation function can take care of this, or you can make another
    ## function to turn this stuff into dictionaries and insert it (probably a little more work but better in the end)
    ## Your choice.







