#--------------------------utils.py
import re

#this class checks the validity of all inputs
class Validator:
    #admin access validation
    @staticmethod
    def admin_access_code_validation(admin_access_code):
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,20}$'
        return re.fullmatch(pattern,admin_access_code) is not None
    
    #username validation
    @staticmethod
    def username_validation(username):
        pattern = r'^[a-zA-Z][a-zA-Z0-9_-]{3,20}$'
        return re.fullmatch(pattern,username) is not None
    
    #password validation
    @staticmethod
    def password_validation(password):
        pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z\d])[A-Za-z\d\S]{6,20}$'
        return re.fullmatch(pattern, password) is not None
    
    #first name validation
    @staticmethod
    def first_name_validation(first_name):
        pattern = r"^[A-Za-z]{2,50}$"
        return re.fullmatch(pattern,first_name) is not None
    
    #last name validation
    @staticmethod
    def last_name_validation(last_name):
        pattern = r"^[A-Za-z]{2,50}$"
        return re.fullmatch(pattern,last_name) is not None
    
    #email validation
    @staticmethod
    def email_validation(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.fullmatch(pattern,email) is not None

    #phone number validation
    @staticmethod
    def phone_validation(phone):
        pattern = r'^\+?[1-9]\d{7,14}$'
        return re.fullmatch(pattern,phone) is not None
    
    #product code validation
    @staticmethod
    def p_code_validation(code):
        pattern = r"^[A-Za-z0-9_-]{3,15}$"
        return re.fullmatch(pattern,code) is not None
        
    #product name validation
    @staticmethod
    def p_name_validation(name):
        pattern = r"^[A-Za-z0-9\s\-\(\)']{2,50}$"
        return re.fullmatch(pattern,name) is not None
    
    #product price validation
    @staticmethod
    def p_price_validation(price):
        pattern = r"^\d+(\.\d{1,2})?$"
        return re.fullmatch(pattern,price) is not None

    #product quantity validation
    @staticmethod
    def P_quantity_validation(quantity):
        pattern = r"^[1-9]\d*$"
        return re.fullmatch(pattern,quantity) is not None
    
    #product category validation
    @staticmethod
    def p_category_validation(category):
        pattern = r"^[A-Za-z ]{2,30}$"
        return re.fullmatch(pattern,category) is not None
    
    #product description validation
    @staticmethod
    def p_description_validation(description):
        pattern = r"^[A-Za-z0-9.,!?()\- ]{10,200}$"
        return re.fullmatch(pattern,description) is not None

    

    

    
   