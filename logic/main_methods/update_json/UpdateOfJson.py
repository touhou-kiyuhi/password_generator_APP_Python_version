import sys, os
sys.path.append(os.getcwd())
from logic.json_classes.settings.jsonSettings_abstract import JsonSettings


class Update_Of_Json(JsonSettings):
    def __init__(self, backupLimit=3):
        super().__init__()
        self.accountData = self.jsonController.jsonReader(self.ACCOUNT_PATH)
        self.backupData = self.jsonController.jsonReader(self.PASSWORDS_BACKUP_PATH)

        self.backupLimit = backupLimit

    def updateAccountJson(self, new_password):
        self.accountData["account"]["password"] = new_password
        # json writer
        self.jsonController.jsonWriter(self.ACCOUNT_PATH, self.accountData)
        # json viewer
        data = self.jsonController.jsonReader(self.ACCOUNT_PATH)
        self.jsonController.jsonViewer(data)

    def updateBackupJson(self, new_password):
        dataExistedFlag = self.checkNew_passwordInBackupDataPasswordsList(new_password)
        if dataExistedFlag:
            print("the password exists in the self.backupData")
        else:
            # 最後備份的密碼為空時，覆蓋
            if self.backupData["account_passwords"][self.backupData["length"]-1]["password"] == "":
                self.backupData["account_passwords"][self.backupData["length"]-1]["password"] = new_password
            else:
                # 超過備份的限制數量，刪除第一筆，更改序位
                if self.backupData["length"] == self.backupLimit:
                    for i in range(self.backupData["length"]):
                        self.backupData["account_passwords"][i]["number"] = i - 1
                    self.backupData["account_passwords"].pop(0)
                    self.backupData["length"] -= 1
                new_data = {
                    "number": len(self.backupData["account_passwords"]),
                    "password": new_password
                }
                self.backupData["account_passwords"].append(new_data)
                self.backupData["length"] += 1 
            # json writer
            self.jsonController.jsonWriter(self.PASSWORDS_BACKUP_PATH, self.backupData)
            # json viewer
            data = self.jsonController.jsonReader(self.PASSWORDS_BACKUP_PATH)
            self.jsonController.jsonViewer(data)

    def checkNew_passwordInBackupDataPasswordsList(self, new_password):
        dataExistedFlag = False
        for i in range(self.backupData["length"]):
            if new_password == self.backupData["account_passwords"][i]["password"]:
                dataExistedFlag = True
                return dataExistedFlag
        return dataExistedFlag


def main(new_password):
    update = Update_Of_Json()
    update.updateAccountJson(new_password)
    update.updateBackupJson(new_password)
    

if __name__ == "__main__":
    new_password = "edcbaEDCBA4321"
    main(new_password)