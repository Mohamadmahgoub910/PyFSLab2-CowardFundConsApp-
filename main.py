from registration import *
from login import *


def main_menu():
    while True:
        print("-------- Main Menu ----------")

        choice = int(input("""
        1: Register
        2- LogIn
        3- Exit
        """))

        if choice == 1:
            register()
        elif choice == 2:
            login_menu()
        elif choice == 3:
            exit()


main_menu()

#1234@MAa