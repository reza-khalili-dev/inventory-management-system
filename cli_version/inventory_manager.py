#-----------------------Inventory_manager
from database import File_manager
from product import Product
from utils import Validator
import math


products_file = File_manager("products.json")


class Inventory_manager:
    
    def add_product(self):

        while True:  
            products = products_file.load() 
            
            #code
            while True:
                code = input("Enter product code (or type 'back' to cancel): ")
                if code.lower() == "back":
                    print("Add Product canceled.")
                    return False
                if any(p["code"] == code for p in products):
                    print("Product with this code already exists.")
                elif not Validator.p_code_validation(code):
                    print("Invalid product code.")
                else:
                    print("Valid product code.")
                    break
            
            #name
            while True:
                name = input("Enter product name (or type 'back' to cancel)")
                if name.lower() == "back":
                    print("Add Product canceled.")
                    return False
                if not Validator.p_name_validation(name):
                    print("Invalid product name.")
                else:
                    print("valid Product name.")
                    break
                
            #price
            while True:
                price = input("Enter product price (or type 'back' to cancel)")
                if price.lower() == "back":
                    print("Add Product canceled.")
                    return False
                if not Validator.p_price_validation(price):
                    print("Invalidm product price.")
                else:
                    price = float(price)
                    print("Valid product price")
                    break                   
                
            #quantity
            while True:
                quantity = input("Enter product quantity (or type 'back' to cancel)")
                if quantity.lower() == "back":
                    print("Add Product canceled.")
                    return False
                if not Validator.P_quantity_validation(quantity):
                    print("Invalid product quantity.")
                else:
                    quantity = int(quantity)
                    print("Valid product quantity.")
                    break
            
            #category
            while True:
                category = input("Enter product category (or type 'back' to cancel)")
                if category.lower() == "back":
                    print("Add Product canceled.")
                    return False
                if not Validator.p_category_validation(category):
                    print("Invalid product category.")
                else:
                    print("Valid product category.")
                    break
            
            #description
            while True:
                description = input("Enter product description (or type 'back' to cancel)")
                if description.lower() == "back":
                    print("Add Product canceled.")
                    return False
                if not Validator.p_description_validation(description):
                    print("Invalid product description.")
                else:
                    print("Valid product description.")
                    break
     
            product = Product(code,name,price,quantity,category,description)
            products.append(product.to_dict())
            products_file.save(products)
            
            print("Product created.")
            return True
        
    #remove product
    def remove_product(self):
        while True:
            products = products_file.load()

            while True:
                code = input("Enter code to remove product (or type 'back' to cancel): ")
                if code.lower() == "back":
                    print("Remove Product canceled.")
                    return False
                if not Validator.p_code_validation(code):
                    print("Invalid product code.")
                else:
                    print("Valid product code.")
                    break

            product = next((p for p in products if p["code"] == code), None)

            if product:
                products.remove(product)
                products_file.save(products)
                print("Product removed successfully.")
                return True
            else:
                print("Product not found.")
    #edit product
    def edit_product(self):
        while True:
            products = products_file.load()
            while True:
                code = input("Enter code to Edit product (or type 'back' to cancel): ")               
                if code.lower() == "back":
                    print("Edit Product canceled.")
                    return False
                if not Validator.p_code_validation(code):
                    print("Invalid product code.")
                else:
                    print("Valid product code.")
                    break
                
            product = next((p for p in products if p["code"] == code),None)
            if not product:
                print("Product not found.")
                continue
            print(f"\nSelect Product: \nCode:{product["code"]}\nName:{product["name"]}\nPrice:{product["price"]}\nQuantity:{product["quantity"]}\nCategory:{product["category"]}\nDescription:{product["description"]}")
            
            field = input("\nWhich field do you want to edit? (name / price / quantity / category / description):").lower()
            if field not in ["name", "price", "quantity", "category","description"]:
                print("Invalid field.")
                continue
            new_value = input(f"Enter new value for {field}: ")
            if field == "price":
                if not new_value.isdigit():
                    print(f"{field.capitalize()} must be a number.")
                    continue
                new_value = int(new_value)
            if field == "quantity":
                if not new_value.isdigit():
                    print(f"{field.capitalize()} must be a number.")
                    continue
                new_value = float(new_value)

            product[field] = new_value              
            products_file.save(products)
            print("Product edit successfully.")
            return True
        
        

    def search_product(self):
        products = products_file.load()
        while True:
            while True:
                code = input("Enter code to Edit product (or type 'back' to cancel): ")
                if code.lower() == "back":
                    print("Search Product canceled.")
                    return False
                if not Validator.p_code_validation(code):
                    print("Invalid product code.")
                else:
                    print("Valid product code.")
                    break
            product = next ((p for p in products if p["code"] == code),None)
            if not product:
                print("Product not found.")
                continue
            print(f"\nResault:\nCode:{product["code"]}\nName:{product["name"]}\nPrice:{product["price"]}\nQuantity:{product["quantity"]}\nCategory:{product["category"]}\nDescription:{product["description"]}")

    #report
    def report(self):
        
        while True:
            products = products_file.load()
            if not products:
                print("No product found.")
                return False
        
            option = input("""
                \nInventory Report
                \n
                \n1.Total different products
                \n2.Total quantity of items
                \n3.Total inventory value
                \n4.Show all products
                \n5.Back to main menu
                \nEnter a number to choose an action:""")
            if option == "1":
                print(f"Total different products:{len(products)}")
            elif option == "2":
                total_quantity = sum(int(p["quantity"]) for p in products) 
                print(f"Total quantity of items: {total_quantity}")
            elif option == "3":
                total_value = sum(float(p["price"]) * int(p["quantity"]) for p in products )
                print(f"Total inventory value: {total_value} units")
            elif option == "4":
                print("\n--- Product List ---")
                for p in products:
                    print(f'{p["code"]} | {p["name"]} | Quantity: {p["quantity"]} | Price: {p["price"]}')
            elif option == "5":
                print("Back to main menu.")
                return False
            else:
                print("Invalid choice. Try again.")



            
    
