# Evan Rhea         12-28-2024
# Function housing
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
    except Exception as e:
        print("ERROR! Invalid input!")
        print(f"Error msg: {e}")


def ViewStore():
    try:
        for key, value in StoreInventory.items():
            print(f"NAME: {key}, INFO: {value}")
        print(f"There are a total of: {RHEA_StoreFront.product_count} items in the store")
    except Exception as e:
        print("An error occurred, please try again later...")
        print(f"Error msg: {e}")

def RemoveProductStore():
    try:
        # We prompt user with which specific item to remove so that we don't remove the wrong items
        ItemtoRemove = input("Please select item to remove:\n")
        if ItemtoRemove in StoreInventory:
            RHEA_StoreFront.product_count -= StoreInventory[ItemtoRemove][2]
            StoreInventory.pop(ItemtoRemove)
        else:
            print("ERROR! Item does not exist")
    except Exception as e:
        print("An error occurred, please try again later...")
        print(f"Error msg: {e}")

def SaveStore():
    
    try:
        StoreJSON = json.dumps(StoreInventory)
        with open("StoreInventory.json", "w") as outfile:
            json.dump(StoreJSON, outfile)
            print(f"Success! {RHEA_StoreFront.product_count} item(s) have been saved!")
    except Exception as e:
        print("An error occurred, please try again later...")
        print(f"Error msg: {e}")

def LoadStore():
    
    try:
        with open("StoreInventory.json") as infile:
            StoreJSON = json.load(infile)
            LoadedData = json.loads(StoreJSON)
            StoreInventory.update(LoadedData)
            RHEA_StoreFront.product_count = sum(item[2] for item in StoreInventory.values())
            print(f"Inventory loaded! There are now {RHEA_StoreFront.product_count} product(s) in the store.")
    except Exception as e:
        print("An error occurred, please try again later...")
        print(f"Error msg: {e}")


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
    except Exception as e:
        print("ERROR! Invalid input!")
        print(f"Error msg: {e}")

def ViewWarehouse():
    for key, value in WarehouseInventory.items():
        print(f"NAME: {key}, INFO: {value}")
    print(f"There are a total of: {RHEA_Warehouse.product_count} item(s) in the warehouse")

def RemoveProductWarehouse():
    try:
        # We prompt user with which specific item to remove so that we don't remove the wrong items
        ItemtoRemove = input("Please select item to remove:\n")
        if ItemtoRemove in WarehouseInventory:
            RHEA_Warehouse.product_count -= WarehouseInventory[ItemtoRemove][2]
            WarehouseInventory.pop(ItemtoRemove)
        else:
            print("ERROR! Item does not exist")
    except Exception as e:
        print("An error occurred, please try again later...")
        print(f"Error msg: {e}")

def SaveWarehouse():
    try:
        WarehouseJSON = json.dumps(WarehouseInventory)
        with open("WarehouseInventory.json", "w") as outfile:
            json.dump(WarehouseJSON, outfile)
            print(f"Success! {RHEA_Warehouse.product_count} item(s) have been saved!")
    except Exception as e:
        print("An error occured, please try again later...")
        print(f"Error msg: {e}")

def LoadWarehouse():
    
    try:
        with open("WarehouseInventory.json") as infile:
            WarehouseJSON = json.load(infile)
            LoadedData = json.loads(WarehouseJSON)
            WarehouseInventory.update(LoadedData)
            RHEA_Warehouse.product_count = sum(item[2] for item in WarehouseInventory.values())
            print(f"Inventory loaded! There are now {RHEA_Warehouse.product_count} product(s) in the warehouse.")
    except Exception as e:
        print("An error occured, please try again later...")
        print(f"Error msg: {e}")




store_actions = {
    "NEW": AddProductStore,
    "VIEW": ViewStore,
    "REMOVE": RemoveProductStore,
    "SAVE": SaveStore,
    "LOAD": LoadStore
}

warehouse_actions = {
    "NEW": AddProductWarehouse,
    "VIEW": ViewWarehouse,
    "REMOVE": RemoveProductWarehouse,
    "SAVE": SaveWarehouse,
    "LOAD": LoadWarehouse
}