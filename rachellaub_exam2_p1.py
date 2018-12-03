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
    """
    print(password)


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
