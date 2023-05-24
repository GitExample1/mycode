#!/usr/bin/env python3
# Part 1
# create the string hostname
hostname = "MTG"

## test logic with the 'if' statement
## what to do if this statement is found to be true

if hostname == "MTG":
    print ("The hostname was found to be MTG\n")

# Part 2


hostname = input("What value should we set for hostname?")
if hostname == "MTG":
    print("The hostname was found to be MTG")


# Part 3


## Collect input from user
hostname = input("What value should we set for hostname?")

## use the lower method to test if input value matches expected value
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

## Always print out to the user
print("Exiting the script")

