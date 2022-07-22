from kivy.uix.screenmanager import Screen

import bcrypt
import re

from sqlalchemy import false

import Codered_Sqlalchemy

class Login(Screen):
    pass


class User:
    def __init__(self, init):
        self.init = init
    
    def register(self):
        """use sqlite3 database to store user information"""
        register_screen =  self.init.root.ids.manager.children[0].screens[1]

        name = register_screen.ids["name"].text 
        email = register_screen.ids["email"].text 
        password = register_screen.ids["password"].text 
        confir_pass = register_screen.ids["confir_pass"].text 
        
        if len(str(name.strip())) < 3:
            print("your username must have 3 characters in at least")
            return false
        
        if re.search("[@,#,$]", name):
            print("this name is not allowed")
            return false
        
        if email:
            pass
        
        if len(password.strip()) < 4:
            print("your password must have 4 characters in at least")
            return false 

        if not (password == confir_pass):
            print("your password and confirm password not equal")
            return false


        if Codered_Sqlalchemy.store_user_credential(name, email, password):
            print(f"you have been registered {name}")
        
        else:
            print("error!, everyone has a bad day, contact us coderedteam@codered.org")
    


    def login(self):
        
        login_screen = self.init.root.ids.manager.children[0].screens[0]

        try:
            email = login_screen.ids["email"].text 
            current_password = login_screen.ids["password"].text 

            req = Codered_Sqlalchemy.pull_user_credential(email)#pull hash
        
            hash = req[0]["password"]#the result is dict in list

            if bcrypt.checkpw(bytes(current_password, encoding='utf-8'), hash):
                print("Welcome back!") 
        
            else:
                print("incorret password or username!")
        
        except  IndexError:
            #mean that the email dont exist in our database
            print("incorret password or username!")
        
        except Exception as error:
            print("something went wrong, try again later")
