from room import *

health = 1 # placeholder for now, until player class is made

while health > 0:
    action = input("Command? ")
    if action in "s":
        searchcode = input("Code to search? ")
        while searchcode not in codes:
            searchcode = input("Code? ")
        print(f"Code found at >>  {searchcode}  <<")
