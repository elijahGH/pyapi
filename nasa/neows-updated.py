#!/usr/bin/python3
import requests

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    neodata = requests.get(NEOURL + startdate + "&" + nasacreds).json()

    for x in neodata["near_earth_objects"].keys():
        print("============")
        print(x)
        print("============")
        for aster in neodata["near_earth_objects"][x]:
            print(f"Asteroids name is {aster['name']}")
            print(f"Magnitude is {aster['absolute_magnitude_h']}")
            print(f"Estimated diameter (in meter) is {aster['estimated_diameter']['meters']['estimated_diameter_max']}")

if __name__ == "__main__":
    main()

