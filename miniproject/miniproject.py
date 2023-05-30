#!/usr/bin/env python3

# find out your zodiac sign
print("What\'s your Zodiac sign?")


def main():
    # ask for birthday
    print("Enter Month and Day that you were born.")
    zodiac_sign = ""

    while zodiac_sign == "":
        # gets birth month of user and lowercase
        month = input("Month(july, november, etc): ")
        month = month.lower()
        # gets birthday of user
        day = int(input("Day: "))

        # compares birthday to zodiac signs
        if (month == "january" and day < 20) or (month == "december" and day > 21):
            zodiac_sign = "Capricorn"
        elif (month == "january" and day > 19) or (month == "february" and day < 19):
            zodiac_sign = "Aquarius"
        elif (month == "february" and day > 18) or (month == "march" and day < 21):
            zodiac_sign = "Pisces"
        elif (month == "march" and day > 20) or (month == "april" and day < 20):
            zodiac_sign = "Aries"
        elif (month == "april" and day > 19) or (month == "may" and day < 21):
            zodiac_sign = "Taurus"
        elif (month == "may" and day > 20) or (month == "june" and day < 22):
            zodiac_sign = "Gemini"
        elif (month == "june" and day > 21) or (month == "july" and day < 23):
            zodiac_sign = "Cancer"
        elif (month == "july" and day > 22) or (month == "august" and day < 23):
            zodiac_sign = "Leo"
        elif (month == "august" and day > 22) or (month == "september" and day < 23):
            zodiac_sign = "Virgo"
        elif (month == "september" and day > 22) or (month == "october" and day < 24):
            zodiac_sign = "Libra"
        elif (month == "october" and day > 23) or (month == "november" and day < 22):
            zodiac_sign = "Scorpius"
        elif (month == "november" and day > 21) or (month == "december" and day < 22):
            zodiac_sign = "Sagittarius"

        # print when something went wrong and restart
        else:
            print("Something went wrong please reenter your birthday")

    # prints results for zodiac sign to user
    print(f"Congratulations you\'re a {zodiac_sign}.")


main()
