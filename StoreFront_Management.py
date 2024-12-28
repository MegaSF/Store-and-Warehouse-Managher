#Evan Rhea              #11-24-2024

from InventoryClass import *
from LocationMenu import *
 
# START OF STORE [TODO] TASKS

# Phase 1
# [DONE] (TODO: Create Objects to use product and location classes)

# Phase 2 -> Store
# [DONE] (TODO: Create a base ionventory and ability to add products)

# Phase 3 -> Store
# [DONE] (TODO: Create view/remove functionality for products)

# Phase 4 -> Store
# [DONE] (TODO: Create ability to save inventory for later adjustments (and by extension loading old inventory) via JSON method)

# Phase 5 -> Store
# [DONE] (TODO: Document code (and clean it up))

# END OF STORE [TODO] TASKS

# Phase 6 -> Warehouse
# [DONE] (TODO: Create a base ionventory and ability to add products)

# Phase 7 -> Warehouse
# [DONE] (TODO: Create view/remove functionality for products)

# Phase 8 -> Warehouse
# [DONE] (TODO: Create ability to save inventory for later adjustments (and by extension loading old inventory) via JSON method)

# Phase 9 -> Warehouse
# [DONE] (TODO: Document code (and clean it up))


# Create object to use store class so we can adjust item count and know what type of location we're adjusting
RHEA_StoreFront = Store(type="Store", product_count=0)


RHEA_Warehouse = Warehouse(type="Warehouse", product_count=0) 

# New product object - use as an outline for adding any new product
new_Product = Product(cost=0, name=None, quantity=0, type=None)

# Empty dict so we have something to track our inventory, makes for easy info display
StoreInventory = {}
WarehouseInventory = {}

running = True
while running:
    MainMenu = input("Welcome, would you like to access [STORE] or [WAREHOUSE] information or [QUIT]:\n").strip().upper()

# Start of [STORE] section
    if MainMenu =="STORE":
        StoreMenu()
        StoreOpt = input("> ").strip().upper()
        if StoreOpt == "NEW":
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

        elif StoreOpt == "VIEW":
            try:
                for key, value in StoreInventory.items():
                    print(f"NAME: {key}, INFO: {value}")
                    print(f"There are a total of: {RHEA_StoreFront.product_count}")
            except Exception:
                print("An error occurred, please try again later...")

        elif StoreOpt == "REMOVE":
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

        #Typical JSON load/save gimmicks for these next two sections
        # # We do this as a means of transferring inventory data if we need to track
        # # or if we need to transfer to a new store
        elif StoreOpt == "SAVE":
            try:
                StoreJSON = json.dumps(StoreInventory)
                with open("StoreInventory.json", "w") as outfile:
                    json.dump(StoreJSON, outfile)
                    print(f"Success! {RHEA_StoreFront.product_count} item(s) have been saved!")
            except Exception:
                print("An error occurred, please try again later...")

        elif StoreOpt == "LOAD":
            try:
                with open("StoreInventory.json") as infile:
                    StoreJSON = json.load(infile)
                    StoreInventory = json.loads(StoreJSON)
                    RHEA_StoreFront.product_count = sum(item[2] for item in StoreInventory.values())
                    print(f"Inventory loaded! There are now {RHEA_StoreFront.product_count} product(s) in the store.")
            except Exception:
                print("An error occurred, please try again later...")

# End of [STORE] section    

# Start of [WAREHOUSE] section
    
    elif MainMenu == "WAREHOUSE":
        WarehouseMenu()
        WarehouseOPT = input("> ").strip().upper()
        if WarehouseOPT == "NEW":
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
                print(f"There is/are {RHEA_Warehouse.product_count} product(s) in the store")
            except Exception:
                print("ERROR! Invalid input!")


        elif WarehouseOPT == "VIEW":
            for key, value in WarehouseInventory.items():
                print(f"NAME: {key}, INFO: {value}")

        elif WarehouseOPT == "REMOVE":
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

        #Typical JSON load/save gimmicks for these next two sections
        # # We do this as a means of transferring inventory data if we need to track
        # # or if we need to transfer to a new store
        elif WarehouseOPT == "SAVE":
            try:
                WarehouseJSON = json.dumps(WarehouseInventory)
                with open("WarehouseInventory.json", "w") as outfile:
                    json.dump(WarehouseJSON, outfile)
                    print(f"Success! {RHEA_Warehouse.product_count} item(s) have been saved!")
            except Exception:
                print("An error occured, please try again later...")

        elif WarehouseOPT == "LOAD":
            try:
                with open("WarehouseInventory.json") as infile:
                    WarehouseJSON = json.load(infile)
                    WarehouseInventory = json.loads(WarehouseJSON)
                    RHEA_Warehouse.product_count = sum(item[2] for item in WarehouseInventory.values())
                    print(f"Inventory loaded! There are now {RHEA_Warehouse.product_count} product(s) in the warehouse.")
            except Exception:
                print("An error occured, please try again later...")
# End of [WAREHOUSE] section    

    elif MainMenu == "QUIT":
        running = False

    else:
        pass