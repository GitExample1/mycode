#!/usr/bin/env python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()
    
    ## user input a start and end date
    S_date= input("Enter a start date to begin.(ex.2019-11-11): ")
    E_date= input("Enter a end date.(ex.2019-12-12): ")

    ## update the date below, if you like
    startdate = "start_date="+S_date

    ## the value below is not being used in this
    ## version of the script
    enddate = "end_date="+E_date

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

