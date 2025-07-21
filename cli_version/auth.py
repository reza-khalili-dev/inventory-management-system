#--------------------------auth.py
import re

from database import File_manager
from utils import Validator

admins_file = File_manager("admins.json")

class Admin:
    def __init__(self,username="",password="",first_name="",last_name="",email="",phone="",admin_access_code=""):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.admin_access_code = admin_access_code


    def to_dict(self):
        return self.__dict__

    #save method
    def sign_up(self):
        while True:
            admins = admins_file.load()
            flag = False
            
            #admin access code
            acces_code = "Admin@2025"
            while True:
                admin_access_code = input("Enter admin access code (or type 'back' to cancel):")
                if admin_access_code.lower() == "back":
                    print("Sign-up canceled.")
                    return False
                if admin_access_code == acces_code and Validator.admin_access_code_validation(admin_access_code):
                    self.admin_access_code = admin_access_code
                    print("Valid access code.")
                    break
                else:
                    print("Invalid access code. You are not authorized to register as admin.")
                    
            #username
            while True:
                username = input("Enter your username (or type 'back' to cancel):")                
                if username.lower() == "back":
                    print("Sign-up canceled.")
                    return False
                if any(admin["username"] == username for admin in admins):
                    print("This username already exists. Please choose another.")
                elif not Validator.username_validation(username):
                    print("Invalid username. Must be 3-20 chars, include letters, digits, and special chars.")
                else:
                    self.username = username
                    print("Valid username.")
                    break               
            #password
            while True:
                password = input("Enter your password (or type 'back' to cancel):")
                if password.lower() == "back":
                    print("Sign-up canceled.")
                    return False
                if not Validator.password_validation(password):
                    print("Invalid password. Must be 6–20 chars, include letters, digits, and special chars.")
                else:
                    self.password = password
                    break               
            #first name
            while True:
                first_name = input("Enter your first name (or type 'back' to cancel):")
                if first_name.lower() == "back":
                    print("Sign-up canceled.")
                    return False
                if not Validator.first_name_validation(first_name):
                    print("Invalid first name. Must be 2–30 chars. Please enter A-Z ")
                else:
                    self.first_name = first_name
                    break

            #last name
            while True:
                last_name = input("Enter your last name (or type 'back' to cancel):")
                if last_name.lower() == "back":
                    print("Sign-up canceled.")
                    return False
                if not Validator.last_name_validation(last_name):
                    print("Invalid first name. Must be 2–30 chars. Please enter A-Z ")
                else:
                    self.last_name = last_name
                    break
                
            #email
            while True:   
                email = input("Enter your Email (or type 'back' to cancel):")
                if email.lower() == "back":
                    print("Sign-up canceled.")
                    return False
                if any(em["email"] == email for em in admins):
                    print("This Email already exists. Please choose another.")
                elif not Validator.email_validation(email):
                    print("Invalid Email.")
                elif email.lower() == "back":
                    print("Sign-up canceled.")
                    return False
                else:
                    self.email = email
                    print("Valid Email")
                    break
            #phone        
            while True:
                phone = input("Enter your phone number (or type 'back' to cancel):")
                if last_name.lower() == "back":
                    print("Sign-up canceled.")
                    return False
                if any(ph["phone"] == phone for ph in admins):
                    phone("This phone number already exists. Please choose another.")
                elif not Validator.phone_validation(phone):
                    print("Phone number is not valid. Make sure it includes the country code and only digits.")
                else:
                    self.phone = phone
                    print("Valid phone number")
                    break
            #save
            admins.append(self.to_dict())
            admins_file.save(admins)
            flag = True

            if flag is True:
                print("Admin created.")
                return True
            else:
                print("Admin not created")
                return False

    #load method
    def log_in(self):
        admins = admins_file.load()

        while True:
            username = input("Enter your username (or type 'back' to cancel): ")
            if username.lower() == "back":
                print("Log-In canceled.")
                return False
            
            matched_admin = next((admin for admin in admins if admin["username"] == username),None)

            if matched_admin:
                password = input("Enter your password (or type 'back' to cancel): ")
                if password.lower() == "back":
                    print("Log-In canceled.")
                    return False
                if matched_admin["password"] == password:
                    print("Welcome to Inventory Management System.")
                    return True
                else:
                    print("Password is not correct.")
            else:
                print("Username is nor correct.")

                
                