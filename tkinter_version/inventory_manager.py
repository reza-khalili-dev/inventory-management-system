#-----------------------Inventory_manager
from database import File_manager
from product import Product
from utils import Validator


products_file = File_manager("products.json")


class Inventory_manager:

  
    def add_product_gui(self,code,name,price,quantity,category,description):
      
        products = products_file.load()

        # product code
        if any(p["code"] == code for p in products):
            return False, "Product with this code already exists."
            
        if not Validator.p_code_validation(code):
            return False, "Invalid product code."
        
        # product name
        if not Validator.p_name_validation(name):
            return False, "Invalid product name."
        
        # product price
        if not Validator.p_price_validation(price):
            return False, "Invalid product price."
        else:
            price = float(price)
        
        # product quantity
        if not Validator.P_quantity_validation(quantity):
            return False, "Invalid product quantity."
        else:
            quantity = int(quantity)

        # product category
        if not Validator.p_category_validation(category):
            return False, "Invalid product category."

        # product description
        if not Validator.p_description_validation(description):
            return False, "Invalid product description."
        
        # save
        product = Product(code,name,price,quantity,category,description)
        products.append(product.to_dict())
        products_file.save(products)
        return True,"Product created."

    # remove product
    def remove_product_gui(self,code):
        products = products_file.load()

        
        if not Validator.p_code_validation(code):
            return False, "Invalid product code."

        product = next((p for p in products if p["code"] == code), None)

        if product:
            products.remove(product)
            products_file.save(products)
            return True, "Product removed successfully."
        else:
            return False, "Product not found."

    # edit product
    def edit_product_gui(self, code, field, new_value):
        
        products = products_file.load()
        
        if not Validator.p_code_validation(code):
            return False, "Invalid product code."
        
        product = next((p for p in products if p["code"] == code),None)
        
        if not product:
            return False, "Product not found."
        
        if field not in ["name", "price", "quantity", "category","description"]:
            return False, "Invalid field."
            
        if field in ["price", "quantity"]:
            try:
                if field == "price":
                    new_value = float(new_value)
                elif field == "quantity":
                    new_value = int(new_value)
            except ValueError:
                return False, f"{field.capitalize()} must be a number."
        
        
        product[field] = new_value
        # save 
        products_file.save(products)
        return True, "Product updated successfully."
    
    
    # search Product
    def search_product_gui(self,code):
        products = products_file.load()

        if not Validator.p_code_validation(code):
            return False, "Invalid product code."
        
        product = next ((p for p in products if p["code"] == code),None)
        
        if not product:
            return False,"Product not found."
        else:
            return product
        
        
        

