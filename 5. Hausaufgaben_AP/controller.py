
import json
import os
import re

class Controller:

    def __init__(self):
        self.breakline = "|------------------------------------------------------------|"

    #region Methods:

    #region Loading JSON Files:

    def load_JSON_registration(self):
        JSONFile = open("JSON_Files/registration.json")
        JSONString = json.load(JSONFile)

        return JSONString

    def load_JSON_Login(self):
        JSONFile = open("JSON_Files/login.json")
        JSONString = json.load(JSONFile)

        return JSONString

    def load_JSON_Users(self):
        JSONFile = open("JSON_Files/existing_users.json")
        JSONString = json.load(JSONFile)

        return JSONString

    #endregion

    def create_new_user(self):
        
        try:
            fileJSON = open("JSON_Files/registration.json","r")
            json_object = json.load(fileJSON)
            fileJSON.close()

            new_User_dic = {"username":json_object['username'],"password":json_object['password']}

            with open("JSON_Files/existing_users.json","r+") as json_file: 
                data = json.load(json_file)
                data.insert(0,new_User_dic)
                json.dump(data, json_file)
            
        except:
            print("\n| Error Message -->> [Could not update the JSON file <existing_users.json>.]|\n"+self.breakline+"\n")
            input()

    def validate_user_creation(self):
        userList = self.load_JSON_Users()
        new_user = self.load_JSON_registration()

        for item in userList:
            if(item['username'] != new_user['username']):
                self.create_new_user()
            else:
                print("\n| Error Message -->> [User Already Exists]|\n"+self.breakline+"\n")
                input()

    def update_JSON_file(self, username, password, email):
        try:
            fileJSON = open("JSON_Files/registration.json","r")
            json_object = json.load(fileJSON)
            fileJSON.close()

            json_object['password'] = password
            json_object['username'] = username
            json_object['email'] = email
            
            fileJSON = open("JSON_Files/registration.json","w")
            json.dump(json_object, fileJSON)
            fileJSON.close()

            self.validate_user_creation()
            print("\n| Information Message -->> [JSON File has been updated]|\n"+self.breakline+"\n")
            input()    
        except:
            print("\n| Error Message -->> [Could not update JSON file. <reigstrations.json>]|\n"+self.breakline+"\n")
            input()

    def load_all_users(self):
        
        userList = self.load_JSON_Users()

        print("\n"+self.breakline+"\n   The following users are registered in the Gaming Centre:    \n"+self.breakline+"\n")
        for item in userList:
            print(item['username'])

    def validate_user(self, username, password):
        
        User = self.load_JSON_Login()
        if(username == str(User["username"]) and password == str(User["password"])):
            return True
        else:
            return False

    #endregion

    def main(self):

        loop = True
        while(loop):
            
            # First Step: Login
            
            print(self.breakline)
            
            print("                  Welcome to the Game Centre\n            Please, enter your username and password:")
            
            print(self.breakline)

            #TODO Create validation for user credentials.

            while(loop):

                # Validating username is not empty.
                username = input("\n      - My Username: ")
                if(username):

                    # Validating password is not empty.
                    password = input("      - My Password: ")
                    if(password):

                        if(self.validate_user(username, password)):

                            while(loop
                            ):

                                print ("\n"+self.breakline+"\n      Welcome back {}. What would you like to do?        \n".format(username)+self.breakline+"\n\n a) Add a new Player\n b) List Players\n c) Exit\n")
                                
                                selected_Option = input("--> Select an option: ")

                                if(selected_Option == "a"):                                    
                                    print("\n"+self.breakline+"\n      What's the new user's nickname and password?        \n"+self.breakline+"\n")
                                    
                                    while(True):
                                        username = input("      - Username: ")
                                        if(re.match(r'^\S{8,16}$',username)):
                                                # Validating password is not empty.
                                            password = input("      - Password: ")
                                            if(re.match(r'^[A-Za-z0-9]{8,16}$',password)): 
                                                if(re.search(r'\d', password)):
                                                    email = input("      - Email: ")
                                                    if(re.match(r'^[A-Za-z0-9]{5,15}\@[A-Za-z0-9]{5,15}\.[a-z]{3}$',email)):
                                                        self.update_JSON_file(username, password, email)
                                                        input("\n --> Press any key to continue!")
                                                    else:
                                                        print(self.breakline+"\n| Error Message -->> [The email you have entered is not valid.]|\n"+self.breakline)
                                                        input("\n --> Press any key to continue!")
                                                else:
                                                    print(self.breakline+"\n| Error Message -->> [Password must contain letters and numbers.]|\n"+self.breakline)
                                                    input("\n --> Press any key to continue!")
                                            else:
                                                print(self.breakline+"\n| Error Message -->> [Password must be at least 8 characters long.]|\n"+self.breakline)
                                                input("\n --> Press any key to continue!")
                                        else:
                                            print(self.breakline+"\n| Error Message -->> [Username cannot have empty spaces and must have at least 8 characters]|\n"+self.breakline)
                                            input("\n --> Press any key to continue!")

                                # Option B: Display a list of the available players.
                                
                                elif(selected_Option == "b"):
                                    
                                    self.load_all_users()
                                    input("\n --> Press any key to continue!")

                                elif(selected_Option == "c"):
                                    if(input("Are you sure you want to exit and logout? (Press 'y' to confirm): ") == 'y'):
                                        loop = False
                                    else:
                                        os.system('cls')        
                                                                

                                else:
                                    print(self.breakline+"\n| Error Message -->> [You have entered an invalid option]|\n"+self.breakline)
                                    input("\n --> Press any key to continue!")

                            # -- End of Menu Loop --

                        else: 
                            print(self.breakline+"\n| Error Message -->> [Wrrong Username or Password]|\n"+self.breakline)
                            input("\n --> Press any key to continue!")
                    else: 
                        print(self.breakline+"\n| Error Message -->> [Password or Username Is Not Valid]|\n"+self.breakline)
                        input("\n --> Press any key to continue!")
                else:
                    print(self.breakline+"\n| Error Message -->> [Password or Username Is Not Valid]|\n"+self.breakline)
                    input("\n --> Press any key to continue!")

            # -- End of Login Loop --

            print("\n"+self.breakline)
        
        # -- End of Login Loop --

if __name__=="__main__":
    Control = Controller()
    Control.main()
    