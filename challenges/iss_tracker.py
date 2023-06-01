#!/usr/bin/env python3
"""
Program that tracks international space station (iss)
"""

import requests
import datetime

# website
URL="http://api.open-notify.org/iss-now.json"


def main():
    resp= requests.get(URL).json()
    print(resp, "\n\n")
    
    # gets latitude and longitude
    long= resp['iss_position']['longitude']
    lat= resp['iss_position']['latitude']
    ts= resp['timestamp']
    ts= datetime.datetime.fromtimestamp(ts)

    # displays current location with lat and long
    print(f"CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {ts}")
    print(f"Lon: {long}")
    print(f"Lat: {lat}")



main()

