#!/usr/bin/python3
def uppercase(str):
        for c in str:
                    if 'a' <= c <= 'z':  # Check if the character is lowercase
                                    c = chr(ord(c) - 32)  # Convert to uppercase using ASCII
                                            print("{}".format(c), end="")
                                                print()  # Print a new line at the end
