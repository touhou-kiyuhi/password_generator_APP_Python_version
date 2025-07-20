import sys, os
sys.path.append(os.getcwd())
from logic.main_methods.initialize_json.initializationOfJson import Initialization_Of_Json
from logic.main_methods.password_generator.passwordGenerator import Password_Generator
from logic.main_methods.update_json.UpdateOfJson import Update_Of_Json


class Main:
    def __init__(self):
        self.init = None
        self.generator = None
        self.update = None
        
    def initialization(self, user, password):
        self.init = Initialization_Of_Json()
        self.init.setupAccountJson(user, password)
        self.init.backupPasswordsJson(password)

    def password_generator(self, passwordLength):
        self.generator = Password_Generator()
        self.generator.password = passwordLength
        # password = self.generator.password
        # print(password)

    def update_json(self, new_password, backupLimit=3):
        self.update = Update_Of_Json(backupLimit)
        self.update.updateAccountJson(new_password)
        self.update.updateBackupJson(new_password)

def main():
    m = Main()
    # Initialization
    user = "Test_TT.User"
    password = "abcdeABCDE1234"
    m.initialization(user, password)

    # Passwords Generator
    passwordLength = 20
    m.password_generator(passwordLength)

    # To update the .json of the account and passwords_backup because we save them in json file
    password = "edcbaEDCBA4321"
    m.update_json(password)


if __name__ == "__main__":
    main()