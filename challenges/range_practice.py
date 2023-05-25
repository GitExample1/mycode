#!usr/bin/env python3 

user_start = int(input("pick a number from 1-100 to start from: "))


for count in range(user_start,0,-1):
    if count == 1:
        b = "bottle"
    else:
        b = "bottles"
    
    first_set = (f"{count} {b} of beer on the wall!")
    print(f"{first_set}\n{first_set} {count} {b} of beer! You take one down, pass it around!")
    
print("No more bottles of beer on the wall!")
