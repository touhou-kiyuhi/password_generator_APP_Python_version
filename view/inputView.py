import sys, os
sys.path.append(os.getcwd())
import tkinter as tk


class InputView(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        self.winfo_toplevel().title("密碼生成與管理")
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        # 按鈕
        self.resetButton = tk.Button(
            self, 
            text = "重置"
        )
        self.resetButton.grid(
            row = 0,
            column = 0, 
            sticky = tk.E,
            padx = (150, 5),
            pady = (50, 5)
        )
        # 說明
        self.text = tk.Label(
            self, 
            text = "輸入 user name 、 password",
            anchor = "s"
        )
        self.text.grid(
            row = 0,
            column = 1, 
            sticky = tk.W,
            padx = (5, 150),
            pady = (50, 5)
        )
        # 輸入資料 user, password
        # user name 
        self.userNameText = tk.Label(
            self, 
            text = "user name"
        )
        self.userNameText.grid(
            row = 1,
            column = 0, 
            sticky = tk.E,
            pady = (5, 5)
        )
        self.userName = tk.Entry(
            self, 
        )
        self.userName.grid(
            row = 1,
            column = 1, 
            sticky = tk.W,
            pady = (5, 5)
        )
        # password
        self.passwordText = tk.Label(
            self, 
            text = "password"
        )
        self.passwordText.grid(
            row = 2,
            column = 0, 
            sticky = tk.E,
            pady = (5, 10)
        )
        self.password = tk.Entry(
            self, 
        )
        self.password.grid(
            row = 2,
            column = 1, 
            sticky = tk.W,
            pady = (5, 10)
        )
        # 按鈕
        self.submitButton = tk.Button(
            self, 
            text = "送出"
        )
        self.submitButton.grid(
            row = 3,
            column = 0, 
            sticky = tk.N,
            pady=(0, 50), 
            columnspan = 2
        )

    
if __name__ == "__main__":
    root = tk.Tk()
    app = InputView(master=root, controller=None)
    root.mainloop()