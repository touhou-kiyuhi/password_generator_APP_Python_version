import sys, os
sys.path.append(os.getcwd())
import tkinter as tk

from view.inputView import InputView
from view.outputView import OutputView
from logic.main import Main as Logic
from logic.json_classes.settings.jsonSettings_abstract import JsonSettings

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logic = Logic()
        self.settings = JsonSettings() 
        self.account = {}
        self.password = ""
        self.passwordLength = 20
        self.backupLimit = 3
        self.jsonDirectory = "json_data"
        self.title("generate and manage passwords")

        self.container = tk.Frame(self)
        self.container.grid(
            row = 0,
            column = 0,
            sticky = "nsew"
        )

        self.frames = {}
        self.inputPage = None
        self.outputPage = None
        self.setFrames()
        self.setInputPage()
        self.setOutputPage()
        self.inputPage.resetButton["command"] = self.reset
        self.inputPage.submitButton["command"] = self.submit
        self.outputPage.confirmButton["command"] = self.confirm
        self.outputPage.changeButton["command"] = self.generate
        self.showFrame("input_view")

    def setFrames(self):
        self.frames["input_view"] = InputView(master=self.container, controller=self)
        self.frames["output_view"] = OutputView(master=self.container, controller=self)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def setInputPage(self):
        self.inputPage = self.frames["input_view"]
        if os.path.exists(self.settings.ACCOUNT_PATH):
            self.account = self.settings.jsonController.jsonReader(self.settings.ACCOUNT_PATH)
            self.inputPage.userName.delete(0, tk.END)
            self.inputPage.password.delete(0, tk.END)
            self.inputPage.userName.insert(0, self.account["account"]["user"])
            self.inputPage.password.insert(0, self.account["account"]["password"])
        

    def setOutputPage(self):
        self.outputPage = self.frames["output_view"]

    # 切換視窗
    def showFrame(self, pageName):
        self.frames[pageName].tkraise()

    def reset(self):
        if os.path.exists(self.settings.ACCOUNT_PATH):
            os.remove(self.settings.ACCOUNT_PATH)
            os.remove(self.settings.PASSWORDS_BACKUP_PATH)
            self.inputPage.userName.delete(0, tk.END)
            self.inputPage.password.delete(0, tk.END)
            self.inputPage.text["text"] = "(初始化成功)\n輸入 user name 、 password"
        else:
            self.inputPage.text["text"] = "(已初始化)]\n輸入 user name 、 password"

    def submit(self):
        if not os.path.exists(self.settings.ACCOUNT_PATH):
            userName = self.inputPage.userName.get()
            password = self.inputPage.password.get()
            if userName == "":
                self.inputPage.text["text"] = "user name 不能空白"
            else:
                # 初始化
                self.logic.initialization(userName, password)
        if os.path.exists(self.settings.ACCOUNT_PATH):
            self.generate()
            # 轉跳到 output 頁面中
            self.showFrame("output_view")

    def confirm(self):
        self.logic.update_json(self.password, self.backupLimit)
        self.inputPage.userName.delete(0, tk.END)
        self.inputPage.password.delete(0, tk.END)
        self.inputPage.userName.insert(0, self.logic.generator.userName)
        self.inputPage.password.insert(0, self.logic.generator.password)
        self.showFrame("input_view")

    def generate(self):
        # 生成密碼
        self.logic.password_generator(self.passwordLength)
        self.password = self.logic.generator.password
        # 清空 outputPage 的 passwordText 後，再填入新生成密碼
        self.outputPage.passwordText.delete(0, tk.END)
        self.outputPage.passwordText.insert(0, self.password)
    
if __name__ == "__main__":
    app = GUI()
    app.mainloop()