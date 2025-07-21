#--------------------------main.py
from auth import Admin
from inventory_manager import Inventory_manager

class Main:
    def __init__(self):
        pass
                
    #main menu
    def main_menu(self):
        while True:
            admin = Admin()
            option = input("""
                           \nINVENTORY MANAGEMENT SYSTEM
                           \n1.Sign up
                           \n2.Login
                           \n3.Exit program
                           \nEnter a number to choose an action:""")
            if option == "1":
                
                success = admin.sign_up()
                if success:
                    self.admin_menu()
                else:
                    input("Sign-up failed or canceled. Press Enter to return to main menu...")
                    
            elif option == "2":
                success = admin.log_in()
                if success:
                    self.admin_menu()
                else:
                    input("Log-In failed or canceled. Press Enter to return to main menu...")
            elif option == "3":
                print("Exiting program...")
                exit()
            else:
                print("Please enter a correct digit (1 to 3)")
                continue

    #admin menu
    def admin_menu(self):
        while True:
            inventory = Inventory_manager()
            option = input("""
                           \nWELCOME TO INVENTORY MANAGEMENT SYSTEM
                           \n            
                           \n1.ADD Product
                           \n2.Remove Product
                           \n3.Edit Product
                           \n4.Search Product
                           \n5.Report
                           \n6.Exit
                           \nEnter a number to choose an action:""")
            if option == "1":
                success = inventory.add_product()
                if not success:
                    input("ADD Product failed or canceled. Press Enter to return to menu...")
            elif option == "2":
                success = inventory.remove_product()
                if not success:
                    input("Remove Product failed or canceled. Press Enter to return to menu...")
            elif option == "3":
                success = inventory.edit_product()
                if not success:
                    input("Edit Product failed or canceled. Press Enter to return to menu...")
            elif option == "4":
                success = inventory.search_product()
                if not success:
                    input("Search Product failed or canceled. Press Enter to return to menu...")
            elif option == "5":
                success = inventory.report()
                if not success:
                    input("Report failed or canceled. Press Enter to return to menu...")
            elif option == "6":
                print("Exiting program...")
                exit()
                
            else:
                print("Please enter a correct digit (1 to 6)")
                continue



if __name__ == "__main__":
    app = Main()
    app.main_menu()


