import json as JSON
import os.path as path
import DataBaseSchemaClasses as Schema
import ProgUtilities as Util


def SaveDataBaseDocument(user_document):
    result = user_document.save()
    return result.email

def GrabAllDBDocuments():
    all_users =Schema.Users.objects.all()
    return all_users

def GrabUserDBDocumment(email):
    our_user = Schema.Users.objects(email=email)
    return our_user

def DeleteUser(email):
    our_user = Schema.Users.objects(email=email).delete()
    return our_user

def ChangePassword(email):
    valid_pass = False
    while valid_pass == False:
        print("Input your desired password: ")
        possible_pass = input()
        valid_pass = Util.ValidatePass(possible_pass)
    Schema.Users.objects(email=email).update(set__password=possible_pass)


def ChangeUserName(email):
    valid_name = False
    while valid_name == False:
        print("Input your desired username: ")
        possible_name = input()
        valid_name = Util.ValidateUser(possible_name)
    Schema.Users.objects(email=email).update(set__username=possible_name)

# Note to self: This is probably not the best implementation; not really worried about that for the concerns of just kinda seeing how a system like this works in action, though.
# desc: SaveAccountFile saves the current state of the account_list to the existing 'accounts' file. This should only be done once currently (at the end of program operation) but should hopefully be extensible to save during the
# operation after major changes to the list, in case the program has an error and must recover.
# pre: list is not null and exists, file given by 'file_name' must also exist
# post: current state of the list of accounts is saved to the file with the name given by file_name.
def SaveAccountFile(account_list, file_name):
    if path.isfile(file_name + '.json'):
        LoadAcccountFile(file_name)
        with open(file_name + '.json', 'w') as output_file:
            JSON.dump(account_list, output_file)
            output_file.close()
    else:
        with open(file_name + '.json', 'w') as output_file:
            JSON.dump(account_list, output_file)
            output_file.close()


# Note to self: This is probably not the best implementation; not really worried about that for the concerns of just kinda seeing how a system like this works in action, though.
# desc: LoadAccountFile loads the current state of the 'accounts' into a List to be added to. This should only be done once currently (at the start of the program), and could feasibly
# be required to load during weird recovery/corruption states, but I'm not too sure frankly.
# pre: file given by 'file_name' must exist
# post: file given by 'file_name' read into a list, giving us a list to work with, add items to and save when we are finished.
def LoadAcccountFile(file_name):
    with open(file_name + '.json', 'r+') as json_file:
        account = JSON.load(json_file)
        json_file.close()
        return account
