import AccountCreation as Acc

autoCancel = 4
accounts = []


def sign_in(actualUser,actualPass):
    global autoCancel
    while (autoCancel > 0):
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

actualUser = "Test123"
actualPass = "Password123"

#if
accounts = Acc.CreateAccount(accounts)
#accounts = Acc.CreateAccount(accounts)
Acc.SaveAccountFile(accounts,"test")
loadedList = Acc.LoadAcccountFile('test')
for item in loadedList:
    print(item)

    ##TODO:
    ## Change this Tuple mess into a 2-dictionary system:
    ## One large dictionary made up of smaller dictionaries, where each new dictionary's
    ## key is the email associated with the account; then have username and password fields
    ## in each dictionary. The account creation function can take care of this, or you can make another
    ## function to turn this stuff into dictionaries and insert it (probably a little more work but better in the end)
    ## Your choice.







