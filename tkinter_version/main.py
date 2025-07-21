import tkinter as tk
from tkinter import messagebox
from auth import Admin
from product import Product
from inventory_manager import Inventory_manager

from utils import Validator
from database import File_manager



#main win
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("600x600")


def open_login_window():
    #login window 
    login_win = tk.Toplevel(root)
    login_win.title("Login")
    login_win.geometry("350x250")

    #tags and entries
    tk.Label(login_win,text="Username:").pack(pady=5)
    username_entry = tk.Entry(login_win)
    username_entry.pack(pady=5)
    
    tk.Label(login_win,text="Password:" ).pack(pady=5)
    password_entry = tk.Entry(login_win,show="*")
    password_entry.pack(pady=5)

    #check login function
    def check_login():
        username = username_entry.get()
        password = password_entry.get()
        
        success = Admin.login(username , password)

        if success:
            login_win.destroy()
            open_dashboard()

        else:
            tk.messagebox.showerror("Login Failed, Invalid username or password.")
            

    #buttons
    tk.Button(login_win,text="Login",font="Helvetica",command=check_login).pack(pady=5)
    tk.Button(login_win,text="Cancel",font="Helvetica",command=login_win.destroy).pack(pady=5)





#sign Up function
def open_signup_window():

    #sign up window
    signup_win = tk.Toplevel(root)
    signup_win.title("Sign Up")
    signup_win.geometry("400x600")


    #tags and entries
    
    # security code 
    tk.Label(signup_win,text="Security code:").pack(pady=5)
    security_code_entry = tk.Entry(signup_win)
    security_code_entry.pack(padx=5)
    
    # username
    tk.Label(signup_win,text="Username:").pack(pady=5)
    username_entry = tk.Entry(signup_win)
    username_entry.pack(pady=5)
    
    # password 
    tk.Label(signup_win,text="Password:").pack(pady=5)
    password_entry = tk.Entry(signup_win,show="*")
    password_entry.pack(pady=5)
    
    # fist name
    tk.Label(signup_win,text="First name:").pack(pady=5)
    first_name_entry = tk.Entry(signup_win)
    first_name_entry.pack(pady=5)

    # last name 
    tk.Label(signup_win,text="Last name:").pack(pady=5)
    last_name_entry = tk.Entry(signup_win)
    last_name_entry.pack(pady=5)

    # email 
    tk.Label(signup_win,text="Email:").pack(pady=5)
    email_entry = tk.Entry(signup_win)
    email_entry.pack(pady=5)
    
    # phone 
    tk.Label(signup_win,text="Phone:").pack(pady=5)
    phone_entry = tk.Entry(signup_win)
    phone_entry.pack(pady=5)
    
    
    #check sign up function
    def check_signup():
        
        admin_access_code = security_code_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()

        success = Admin().signup(admin_access_code,username,password,first_name,last_name,email,phone)

        if success:
            tk.messagebox.showinfo("sign up Successful, Welcome.")
            signup_win.destroy()
            open_dashboard()
        else:
            tk.messagebox.showerror("sign up Failed Invalid username or password.")
 
    # buttons
    tk.Button(signup_win,text="Sign Up",font="Helvetica",command=check_signup).pack(pady=5)
    tk.Button(signup_win,text="Cancel",font="Helvetica",command=signup_win.destroy).pack(pady=5)
       
#sugn up and login button
title_lable = tk.Label(root,text="Welcome to Inventory Management System", font=("Helvetica", 16))
title_lable.pack(pady=20)

login_button = tk.Button(root,text="Login",width=20 , height=2, command=open_login_window)
login_button.pack(pady=10)

signup_button = tk.Button(root,text="Sign Up",width=20, height=2, command=open_signup_window)
signup_button.pack(pady=10)



#dashboard
def open_dashboard():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Dashboard")

    
    # label and buttons
    tk.Label(root,text="Inventory Dashboard",font=("Helvetica", 16)).pack(pady=20)
    
    # command ham baraye hameye button ha gozashte shavad
    tk.Button(root,text="Add Product",width=40, command=open_add_product).pack(pady=10)
    tk.Button(root,text="Remove Product",width=40,command=open_remove_product ).pack(pady=10)
    tk.Button(root,text="Edit Product",width=40,command=open_edit_product ).pack(pady=10)
    tk.Button(root,text="Search Product",width=40,command=open_search_product).pack(pady=10)
    tk.Button(root,text="Log out",width=40,command=logout).pack(pady=10)


#add product
def open_add_product():
    for widget in root.winfo_children():
        widget.destroy()
    
    root.title("ADD Product")
    
    # main label 
    tk.Label(root,text="ADD Product",font=("Helvetica",16)).pack(pady=20)
    
    # entries and labels
    tk.Label(root,text="Code:",font="Helvetica").pack(pady=5)
    code_entry = tk.Entry(root)
    code_entry.pack(pady=5)
    
    tk.Label(root,text="Product name:",font="Helvetica").pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    tk.Label(root,text="Price:",font="Helvetica").pack(pady=5)
    price_entry = tk.Entry(root)
    price_entry.pack(pady=5)
    
    tk.Label(root,text="Quantity",font="Helvetica").pack(pady=5)
    quantity_entry = tk.Entry(root)
    quantity_entry.pack(pady=5)
    
    tk.Label(root,text="Category:",font="Helvetica").pack(pady=5)
    category_entry = tk.Entry(root)
    category_entry.pack(pady=5)
    
    tk.Label(root,text="Description:",font="Helvetica").pack(pady=5)
    description_entry = tk.Entry(root)
    description_entry.pack(pady=5)
    
    
    # check
    def check_add_Product():
        code = code_entry.get()
        name = name_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()
        category = category_entry.get()
        description = description_entry.get()

        success = Inventory_manager().add_product_gui(code,name,price,quantity,category,description)
        
        if success:
            tk.messagebox.showinfo("ADD Product Successful.")
            open_dashboard()
        else:
            tk.messagebox.showinfo("ADD Product Failed.")

    
    # buttons
    tk.Button(root,text="ADD Product",width=20,font="Helvetica",command=check_add_Product).pack(pady=5)
    tk.Button(root,text="Cancele",width=20,font="Helvetica",command=open_dashboard).pack(pady=5)
    
# remove product
def open_remove_product():
    for widget in root.winfo_children():
        widget.destroy()

    
    root.title("Remove product")

    # main label 
    tk.Label(root,text="Remove product",font=("Halvetica",16)).pack(pady=5)
    
    # entries and labels
    tk.Label(root,text="Product code:",font="Halvetica").pack(pady=5)
    product_code_entry = tk.Entry(root)
    product_code_entry.pack(pady=5)
    
    # check
    def check_remove_product():
        code = product_code_entry.get()

        success = Inventory_manager().remove_product_gui(code)

        if success:
            tk.messagebox.showinfo("Remove Product Successful.")
            open_dashboard()
        else:
            tk.messagebox.showinfo("Remove Product Failed.")
    
    # buttons 
    tk.Button(root,text="Remove Product",width=20,font="Helvetica",command=check_remove_product).pack(pady=5)
    tk.Button(root,text="Cancele",width=20,font="Helvetica",command=open_dashboard).pack(pady=5)

# edit Product    
def open_edit_product():
    for widget in root.winfo_children():
        widget.destroy()
    
    root.title("Edit product")

    tk.Label(root,text="Edit Product",font=("Halvetica",16)).pack(pady=20)

    # label and entries
    tk.Label(root,text="Product code:",font="Halvetica").pack(pady=5)
    product_code_entry = tk.Entry(root)
    product_code_entry.pack(pady=5)

    tk.Label(root,text="Field to Edit (name / price / quantity / category / description):",font="Halvetica").pack(pady=5)
    product_field_entry = tk.Entry(root)
    product_field_entry.pack(pady=5)

    tk.Label(root,text="New Product value:",font="Halvetica").pack(pady=5)
    product_new_value_entry = tk.Entry(root)
    product_new_value_entry.pack(pady=5)
    
    
    
    def check_edit_product():
        code = product_code_entry.get()
        field = product_field_entry.get().lower()
        new_value = product_new_value_entry.get()

        success = Inventory_manager().edit_product_gui(code,field,new_value)
        
        if success:
            tk.messagebox.showinfo("Edit Product Successful")
            open_dashboard()
        else:
            tk.messagebox.showerror("Edit product Failed")
            
    # buttons
    tk.Button(root,text="Edit Product", width=20,font="Halvetica",command=check_edit_product).pack(pady=5)
    tk.Button(root,text="Cancele", width=20,font="Halvetica",command=open_dashboard).pack(pady=5)

#search and report product
def open_search_product():
    for widget in root.winfo_children():
        widget.destroy()
    
    root.title("Search product")

    tk.Label(root,text="Search Product",font=("Halvetica",16)).pack(pady=20)

    # label and entries
    tk.Label(root,text="Product code:",font="Halvetica").pack(pady=5)
    product_code_entry = tk.Entry(root)
    product_code_entry.pack(pady=5)
    
    def check_search_product():
        code = product_code_entry.get()

        success = Inventory_manager().search_product_gui(code)
        
        if success:
            search_product_win = tk.Toplevel(root)
            search_product_win.title("Search Product")
            tk.Label(search_product_win,text="Product Information",font=("Halvetica",12)).pack(pady=10)
            search_product_win.geometry("400x600")
            
            # labels for information
            tk.Label(search_product_win,font=("Halvetica"),text=f"code: {success["code"]}").pack(pady=5)
            tk.Label(search_product_win,font=("Halvetica"),text=f"Name: {success["name"]}").pack(pady=5)
            tk.Label(search_product_win,font=("Halvetica"),text=f"Price: {success["price"]}").pack(pady=5)
            tk.Label(search_product_win,font=("Halvetica"),text=f"Quantity: {success["quantity"]}").pack(pady=5)
            tk.Label(search_product_win,font=("Halvetica"),text=f"Category: {success["category"]}").pack(pady=5)
            tk.Label(search_product_win,font=("Halvetica"),text=f"Description: {success["description"]}").pack(pady=5)
            
        else:
            tk.messagebox.showerror("Search product Failed")

    tk.Button(root,text="Search Product", width=20,font="Halvetica",command=check_search_product).pack(pady=5)
    tk.Button(root,text="Cancele", width=20,font="Halvetica",command=open_dashboard).pack(pady=5)
    

# log out
def logout():
    for widget in root.winfo_children():
        widget.destroy()
    
    root.title("Inventory Management System")
    
    title_lable = tk.Label(root, text="Welcome to Inventory Management System", font=("Helvetica", 16))
    title_lable.pack(pady=20)

    login_button = tk.Button(root, text="Login", width=20, height=2, command=open_login_window)
    login_button.pack(pady=10)

    signup_button = tk.Button(root, text="Sign Up", width=20, height=2, command=open_signup_window)
    signup_button.pack(pady=10)



root.mainloop()