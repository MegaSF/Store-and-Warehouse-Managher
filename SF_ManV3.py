from Functions import *

def main():
     running = True
     while running:
        MainMenu = input("Welcome, would you like to access [STORE] or [WAREHOUSE] information or [QUIT]:\n").strip().upper()
        if MainMenu == "STORE":
            StoreMenu()
            StoreOpt = input("> ").strip().upper()
            if StoreOpt == "NEW":
                AddProductStore()
            elif StoreOpt == "VIEW":
                ViewStore()

                # Complete function and call
            elif StoreOpt == "REMOVE":
                RemoveProductStore()
                # Complete function and call
            elif StoreOpt == "SAVE":
                SaveStore()
                # Complete function and call
            elif StoreOpt == "LOAD":
                LoadStore()
            else:
                print("Error! Invalid option!")

        elif MainMenu == "WAREHOUSE":
            WarehouseMenu()
            WarehouseOpt = input("> ").strip().upper()
            if WarehouseOpt == "NEW":
                AddProductWarehouse()
            elif WarehouseOpt == "VIEW":
                ViewWarehouse()
            elif WarehouseOpt == "REMOVE":
                RemoveProductWarehouse()
            elif WarehouseOpt == "SAVE":
                SaveWarehouse()
            elif WarehouseOpt == "LOAD":
                LoadWarehouse()
            else:
                print("Error, invalid option!")

        elif MainMenu == "QUIT":
            print("Thank you, please come again")
            running = False
        
        else:
            print("Error! Invalid option, please select [STORE] or [WAREHOUSE]")
if __name__ == "__main__":
    main()