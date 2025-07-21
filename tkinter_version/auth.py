#--------------------------auth.py
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

#-------------------------------------------------------------------------------------------------------------------------


#sign Up method for GUI version
    def signup(self,admin_access_code,username,password,first_name,last_name,email,phone):
        admins = admins_file.load()        
        
        # secret code 
        acces_code = "Admin@2025"
        
        if admin_access_code != acces_code:
            return False,"Invalid access code. You are not authorized to register as admin."
        
        if not Validator.admin_access_code_validation(admin_access_code):
            return False,"Invalid access code. You are not authorized to register as admin."  
                  
        self.admin_access_code = admin_access_code
                
        # username
        if any(admin["username"] == username for admin in admins):
            return False, "This username already exists. Please choose another."

        if not Validator.username_validation(username):
            return False,"Invalid username. Must be 3-20 chars, include letters, digits, and special chars."
        
        self.username = username        
        
        # password
        if not Validator.password_validation(password):
            return False,"Invalid password. Must be 6–20 chars, include letters, digits, and special chars."
        
        self.password = password
        
        # first name
        if not Validator.first_name_validation(first_name):
            return False,"Invalid first name. Must be 2–30 chars. Please enter A-Z "
        
        self.first_name = first_name
        
        # last name 
        if not Validator.last_name_validation(last_name):
            return False, "Invalid last name. Must be 2–30 chars. Please enter A-Z "
        
        self.last_name = last_name
        
        # email
        if any(em["email"] == email for em in admins):
            return False,"This Email already exists. Please choose another."
        
        if not Validator.email_validation(email):
            return False, "Invalid Email entry"
        
        self.email = email
             
        # phone
        if any(ph["phone"] == phone for ph in admins):
            return False, "This phone number already exists. Please choose another."
            
        if not Validator.phone_validation(phone):
            return False,"Phone number is not valid. Make sure it includes the country code and only digits."
        
        self.phone = phone

        #save
        admins.append(self.to_dict())
        admins_file.save(admins)
        return True,"Admin registered successfully!"




    #login method
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


    #login method for GUI version
    def login(username , password):
        admins = admins_file.load()

        matched_admin = next((admin for admin in admins if admin["username"] == username),None)

        if matched_admin and matched_admin["password"] == password:
            return True,matched_admin
        else:
            return False, None
            


                
                