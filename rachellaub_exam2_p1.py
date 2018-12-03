#!/usr/bin/env python3
"""
Python 2
Creating a secure password
"""
import re


def is_valid_password(password):
    """
    Checks if parameter meets the requirments
    8 char long
    At least one upper and lower case letter
    At least 1 digit
    :param password: Password entered in by user
    """
    counter = 0
    if(len(password)<8):
        print("Your password must be at least 8 chars long.")
    else:
        counter += 1

    if not re.search("[a-z]",password):
        print("Your password must have at least 1 lower case letter.")
    else:
        counter += 1

    if not re.search("[A-Z]",password):
        print("Your password must have at least 1 upper case letter.")
    else:
        counter += 1

    if not re.search("[0-9]",password):
        print("Your password must have at least 1 digit.")
    else:
        counter += 1

    if counter = 4:
        print("Your pair of passwords will work")



def main():
    """
    Test your module
    """
    while True:
        password=input("Enter your password:")
        confirm=input("Re-enter your password:")
        if password == confirm:
            print("Passwords match")
            is_valid_password(password)
            break
        else:
            print("Passwords don't match, try again")
            continue



if __name__ == "__main__":
    main()
    exit(0)
