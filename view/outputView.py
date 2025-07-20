import sys, os
sys.path.append(os.getcwd())
import tkinter as tk


class OutputView(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        self.winfo_toplevel().title("密碼生成與管理")
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        # 說明
        self.text = tk.Label(
            self, 
            text = "你的新密碼",
            width = 60,
            anchor = "s"
        )
        self.text.grid(
            row = 0,
            column = 0, 
            sticky = tk.N,
            pady = (50, 0),
            columnspan = 2
        )
        # password 顯示
        self.passwordText = tk.Entry(
            self, 
        )
        self.passwordText.insert(0, "password")
        self.passwordText.grid(
            row = 1,
            column = 0, 
            sticky = tk.N,
            pady = (10, 10),
            columnspan = 2
        )
        # 確認按鈕
        self.confirmButton = tk.Button(
            self, 
            text = "確認"
        )
        self.confirmButton.grid(
            row = 2,
            column = 0, 
            padx=(0, 5),
            pady=(0, 50), 
            sticky = tk.E
        )
        # 更換按鈕
        self.changeButton = tk.Button(
            self, 
            text = "更換"
        )
        self.changeButton.grid(
            row = 2,
            column = 1, 
            padx=(5, 0),
            pady=(0, 50), 
            sticky = tk.W,
        )

    
if __name__ == "__main__":
    root = tk.Tk()
    app = OutputView(master=root, controller=None)
    root.mainloop()