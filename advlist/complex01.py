#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():

    # creates a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # displays list1
    print(list1, "\n")

    # displays list1[1] which should only display arista_eos
    print(list1[1], "\n")

    # creates a new list containing a sinlge item
    list2 = ["juniper"]

    #extends list1 by list2 (combine both lists together into a single list)
    list1.extend(list2)

    # displays list1, which now contains juniper
    print(list1, "\n")
    
    # creates list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # uses the append operation to append list1 by list3
    list1.append(list3)

    # displays the new complex list1
    print(list1, "\n")

    # displays the list of IP addresses
    print (list1[4])

    # display the first item in the list (0th item) - first IP address
    print(list1[4][0])


main()
