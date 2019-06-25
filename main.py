from pymongo import MongoClient
from tkinter import *
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client.Login_db
collection = db.Login

def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="OK", command=screen3.destroy).pack()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Failed")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=screen4.destroy).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Failed")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=screen5.destroy).pack()

def user_already_exist():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Failed")
    screen6.geometry("150x100")
    Label(screen6, text="Username Not Available").pack()
    Button(screen6, text="OK", command=screen6.destroy).pack()

def register_user():
    print("working")

    username_info = username.get()
    password_info = password.get()
    user = collection.find_one({"username": username_info})
    if user:
        user_already_exist()
    else:
        post = {"username": username_info, "password": password_info, "time_created": f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'}
        post_id = collection.insert_one(post).inserted_id
        if post_id is not None:
            Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()
        else:
            Label(screen1, text="Registration Failed", fg="red", font=("calibri", 11)).pack()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    user = collection.find_one({"username": username1})
    if user:
        if user["password"] == password1:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Login and Register App")
    Label(text="Login and Register App", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    screen.mainloop()

main_screen()