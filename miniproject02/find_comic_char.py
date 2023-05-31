#!/usr/bin/env python3
"""
Author: Nicolas Herrera
A program to find a comic book character and the date they first appeared
"""

def main():
    # open comic-characters data
    with open("comic-characters.csv", "r",errors='replace' ) as comic_char:
        # find comic book character and when they first appeared
        print("Search comic book character and the date when they first appeared")
        character = input(f"Enter name of character:\n")
        for line in comic_char:
            if character in line:
                line = line.split(",")
                name = line[0]
                comic = line[1]
                reality = line[2]
                first_date = line[12] + line[13]
                # gives comment if no data availible for first_date
                if line[12] == "":
                    first_date = "data not found"
                
                print(f"{name}, apart of {comic} in {reality}, first appeared in {first_date}.")
    
if __name__ == "__main__":
    main()



