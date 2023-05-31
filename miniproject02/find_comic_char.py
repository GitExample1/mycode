#!/usr/bin/env python3

# imports
import csv

# open comic-characters data
with open("comic-characters.csv", "r") as comic_char:
    # find character comic and when they first appeared
    print("Find character comic and when they first appeared")
    character = input(f"Enter name of character:\n")
    for line in comic_char:

        if character in line:
            line = line.split(",")
            name = line[0]
            comic = line[2]
            first_date = line[12] + line[13]
            print(f"{name}, apart of {comic}, first appeared in {first_date}.")




