#!/usr/bin/env python3

def main():

# open dracula.txt
    with open("dracula.txt","r") as foo:
        count = 0
# write all lines with vampire in new file "vampytimes.txt"
        with open("vampytimes.txt", "w") as vampytimes:
    # loop through dracula.txt, print each line!
            for line in foo:
            ## print(line)
# print only lines with vampire

            ##if "vampire" in line:
            ##    print (line)

# print all lines with vampire no matter what case
                if "vampire" in line.lower():
                    print(line)
                    count += 1
                    vampytimes.write(line)
# write all lines with vampire in new file "vampytimes.txt"
        

# count how many lines have vampire
        print("Number of lines with 'vampire': ", count)


main()


