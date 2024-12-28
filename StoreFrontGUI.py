# Evan Rhea             12-1-2024
# This file is going to be used to givd my storefront management software a fun user interface!
from Functions import *
import tkinter as tk
from tkmacosx import *


def main():
# Create App Runtime
    Store = tk.Tk()










    QuitButton = Button(Store, text="Quit", command = Store.destroy, bg = 'Red', font='Arial 25')
    QuitButton.place(x = 600, y = 800, width=250, height = 100)

    Store.mainloop()


if __name__ == "__main__":
    main()