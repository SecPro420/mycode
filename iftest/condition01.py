#!/usr/bin/env python3
# Alta3 Research || Author: RZFeeser@alta3.com
# Check hostname against expected value

## Collect input from user
hostname = input("What value should we set for hostname?\n")

## use the lower method to test if input value matches expected value
if hostname.lower() == "mtg":
    print(f"The hostname was found to be mtg")
    print("hostname matches expected config")
else:
    print("Sorry, the hostname is not valid")

## Always print out to the user
print("Exiting the script")

