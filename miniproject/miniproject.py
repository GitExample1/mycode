#!/usr/bin/env python3

#zodiac sign
print("What\'s your Zodiac sign?")

# ask for birthday
print("Enter Month and Day that you were born.")
month = input("Month(e.g. july, november, etc): ")
day = int(input("Day: "))
zodiac_sign = ""
# compare zodiac signs
if (month == "january" and day < 20) or (month == "december" and day > 21):
    zodiac_sign = "Capricorn"

print(month, day)
print(zodiac_sign)

# print answer
