from pymongo import MongoClient
import tkinter
from datetime import datetime
class Login_app():
    def __init__(self):
        root = tkinter.Tk()
        root.geometry("300x250")
        root.title("Login and Register App")
        self.master = root
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.Login_db
        self.collection = self.db.Login
        self.main_window()
        self.master.mainloop()

    def main_window(self):
        tkinter.Label(text="Login and Register App", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
        tkinter.Label(text="").pack()
        tkinter.Button(text="Login", height="2", width="30", command=self.login).pack()
        tkinter.Label(text="").pack()
        tkinter.Button(text="Register", height="2", width="30", command=self.register).pack()

    def login(self):
        self.window1 = tkinter.Toplevel(self.master)
        self.window1.title("Login")
        self.window1.geometry("300x250")
        tkinter.Label(self.window1, text="Please enter details below to login").pack()
        tkinter.Label(self.window1, text="").pack()
        self.username_verify = tkinter.StringVar()
        self.password_verify = tkinter.StringVar()
        tkinter.Label(self.window1, text="Username * ").pack()
        self.username_entry1 = tkinter.Entry(self.window1, textvariable=self.username_verify)
        self.username_entry1.pack()
        tkinter.Label(self.window1, text="").pack()
        tkinter.Label(self.window1, text="Password * ").pack()
        self.password_entry1 = tkinter.Entry(self.window1, textvariable=self.password_verify)
        self.password_entry1.pack()
        tkinter.Label(self.window1, text="").pack()
        tkinter.Button(self.window1, text="Login", width=10, height=1, command=self.login_verify).pack()

    def register(self):
        self.window2 = tkinter.Toplevel(self.master)
        self.window2.title("Register")
        self.window2.geometry("300x250")
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()
        tkinter.Label(self.window2, text="Please enter details below").pack()
        tkinter.Label(self.window2, text="").pack()
        tkinter.Label(self.window2, text="Username * ").pack()
        self.username_entry = tkinter.Entry(self.window2, textvariable=self.username)
        self.username_entry.pack()
        tkinter.Label(self.window2, text="Password * ").pack()
        self.password_entry = tkinter.Entry(self.window2, textvariable=self.password)
        self.password_entry.pack()
        tkinter.Label(self.window2, text="").pack()
        tkinter.Button(self.window2, text="Register", width=10, height=1, command=self.register_user).pack()

    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()
        user = self.collection.find_one({"username": username_info})
        if user:
            self.make_window(title="Failed", text="Username Not Available")
        else:
            post = {"username": username_info, "password": password_info,
                    "time_created": f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'}
            post_id = self.collection.insert_one(post).inserted_id
            if post_id is not None:
                tkinter.Label(self.window2, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()
            else:
                tkinter.Label(self.window2, text="Registration Failed", fg="red", font=("calibri", 11)).pack()
        self.username_entry.delete(0, tkinter.END)
        self.password_entry.delete(0, tkinter.END)

    def login_verify(self):
        username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        self.username_entry1.delete(0, tkinter.END)
        self.password_entry1.delete(0, tkinter.END)
        user = self.collection.find_one({"username": username1})
        if user:
            if user["password"] == password1:
                self.make_window(title="Sucess", text="Login Sucess")
            else:
                self.make_window(title="Failed", text="Password Error")
        else:
            self.make_window(title="Failed", text="User Not Found")

    def make_window(self, text=None, title=None):
        window = tkinter.Toplevel(self.master)
        window.title(title)
        window.geometry("150x100")
        tkinter.Label(window, text=text).pack()
        tkinter.Button(window, text="OK", command=window.destroy).pack()
if __name__ == "__main__":
    Login_app()
