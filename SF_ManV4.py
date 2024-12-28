from Functions import *
def main():
    running = True
    while running:
        MainMenu = input("Welcome, would you like to access:\n[STORE]\n[WAREHOUSE]\n[QUIT]\n> ").strip().upper()

        if MainMenu == "STORE":
            StoreMenu()
            StoreOpt = input(">>> ").strip().upper()
            action = store_actions.get(StoreOpt)
            if action:
                action()
            else:
                print("Error, action does not exist!")

        elif MainMenu == "WAREHOUSE":
            WarehouseMenu()
            WarehouseOpt = input(">>> ").strip().upper()
            action = warehouse_actions.get(WarehouseOpt)
            if action:
                action()
            else:
                print("Error, action does not exist!")
        elif MainMenu == "QUIT":
            print("Thank you, please come again")
            running = False

        else:
            print("Error, invalid input, please select [STORE] [WAREHOUSE] or [QUIT]")

if __name__ == "__main__":
    main()