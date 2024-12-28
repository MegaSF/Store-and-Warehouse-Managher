# Evan Rhea      # 11-24-2024
# Inventory management System (classes)
import json
 
class Product:
    def __init__(self, cost, name, quantity, type):
        self.cost = cost
        self.name = name
        self.quantity = quantity
        self.type = type

    def ProductInfo(self):
        print(f"    RHEATECH SHOP INVENTORY")
        print("-"*30)
        print(f"NAME:   {self.name}")
        print(f"COST:   ${self.cost:.2f}")
        print(f"QUANTITY:   {self.quantity}")



class Location:
    def __init__(self, type, product_count):
        self.type = type
        self.product_count = product_count
        



class Store(Location):
    def __init__(self, type, product_count):
        super().__init__(type, product_count)

    def PrintStore(self):
        print(f"    RHEATECH STORE")
        print("-"*30)
        print(f"TYPE:   {self.type}")
        print(f"INVENTORY:  {self.product_count}")



class Warehouse(Location):
    def __init__(self, type, product_count):
        super().__init__(type, product_count)

    def PrintWarehouse(self):
        print(f"    RHEATECH WAREHOUSE")
        print("-"*30)
        print(f"TYPE:   {self.type}")
        print(f"INVENTORY:  {self.product_count}")

