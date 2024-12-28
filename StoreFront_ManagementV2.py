# Evan Rhea             12-27-2024

# this is gonna be a re make of the orignial app i made ig lmao
from InventoryClass import *
from LocationMenu import *


RHEA_StoreFront = Store(type="Store", product_count=0)

RHEA_Warehouse = Warehouse(type="Warehouse", product_count=0) 

new_Product = Product(cost=0, name=None, quantity=0, type=None)

StoreInventory = {}
WarehouseInventory = {}

def AddProductStore():
    try:
        new_Product.type = input("Please enter product type:\n")
        new_Product.name = input("Please enter product name:\n")
        new_Product.quantity = int(input("Please enter amount to add:\n"))
        new_Product.cost = float(input("Please enter product price:\n"))
        StoreInventory[new_Product.name] = new_Product.type, new_Product.cost, new_Product.quantity
        print(f"Item added:")
        print()
        new_Product.ProductInfo()
        RHEA_StoreFront.product_count += new_Product.quantity
        print(f"There is/are {RHEA_StoreFront.product_count} product(s) in the store")
    except Exception:
        print("ERROR! Invalid input!")


def ViewStore():
    try:
        for key, value in StoreInventory.items():
            print(f"NAME: {key}, INFO: {value}")
        print(f"There are a total of: {RHEA_StoreFront.product_count} items in the store")
    except Exception:
        print("An error occurred, please try again later...")

def RemoveProductStore():
    try:
        # We prompt user with which specific item to remove so that we don't remove the wrong items
        ItemtoRemove = input("Please select item to remove:\n")
        if ItemtoRemove in StoreInventory:
            RHEA_StoreFront.product_count -= ItemtoRemove[2]
            StoreInventory.pop(ItemtoRemove)
        else:
            print("ERROR! Item does not exist")
    except Exception:
        print("An error occurred, please try again later...")

def SaveStore():
    
    try:
        StoreJSON = json.dumps(StoreInventory)
        with open("StoreInventory.json", "w") as outfile:
            json.dump(StoreJSON, outfile)
            print(f"Success! {RHEA_StoreFront.product_count} item(s) have been saved!")
    except Exception:
        print("An error occurred, please try again later...")

def LoadStore():
    
    try:
        with open("StoreInventory.json") as infile:
            StoreJSON = json.load(infile)
            LoadedData = json.loads(StoreJSON)
            StoreInventory.update(LoadedData)
            RHEA_StoreFront.product_count = sum(item[2] for item in StoreInventory.values())
            print(f"Inventory loaded! There are now {RHEA_StoreFront.product_count} product(s) in the store.")
    except Exception:
        print("An error occurred, please try again later...")


def AddProductWarehouse():
    try:
        new_Product.type = input("Please enter product type:\n")
        new_Product.name = input("Please enter product name:\n")
        new_Product.quantity = int(input("Please enter amount to add:\n"))
        new_Product.cost = float(input("Please enter product price:\n"))
        WarehouseInventory[new_Product.name] = new_Product.type, new_Product.cost, new_Product.quantity
        print(f"Item added:")
        print()
        new_Product.ProductInfo()
    
        
        RHEA_Warehouse.product_count += new_Product.quantity
        print(f"There is/are {RHEA_Warehouse.product_count} product(s) in the warehouse")
    except Exception:
        print("ERROR! Invalid input!")

def ViewWarehouse():
    for key, value in WarehouseInventory.items():
        print(f"NAME: {key}, INFO: {value}")
    print(f"There are a total of: {RHEA_Warehouse.product_count} item(s) in the warehouse")

def RemoveProductWarehouse():
    try:
        # We prompt user with which specific item to remove so that we don't remove the wrong items
        ItemtoRemove = input("Please select item to remove:\n")
        if ItemtoRemove in WarehouseInventory:
            RHEA_Warehouse.product_count -= ItemtoRemove[2]
            WarehouseInventory.pop(ItemtoRemove)
        else:
            print("ERROR! Item does not exist")
    except Exception:
        print("An error occurred, please try again later...")

def SaveWarehouse():
    try:
        WarehouseJSON = json.dumps(WarehouseInventory)
        with open("WarehouseInventory.json", "w") as outfile:
            json.dump(WarehouseJSON, outfile)
            print(f"Success! {RHEA_Warehouse.product_count} item(s) have been saved!")
    except Exception:
        print("An error occured, please try again later...")

def LoadWarehouse():
    
    try:
        with open("WarehouseInventory.json") as infile:
            WarehouseJSON = json.load(infile)
            LoadedData = json.loads(WarehouseJSON)
            WarehouseInventory.update(LoadedData)
            RHEA_Warehouse.product_count = sum(item[2] for item in WarehouseInventory.values())
            print(f"Inventory loaded! There are now {RHEA_Warehouse.product_count} product(s) in the warehouse.")
    except Exception:
        print("An error occured, please try again later...")


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