#
# Ciaran Moran
# G00426050@atu.ie
# Topic04 Reading apis in the wild
# Assignment: Assignment 03 
# Description: Write a program that retrieves the dataset for the 
#              "exchequer account (historical series)" from the CSO, and stores it into 
#              a file called "cso.json".
#
import requests
import json

#This is the CSO JSON URL for FIQ02 - Exchequer Account (Historical Series)
url= " https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

# This function will retrieve all the data in JSON format from CSO.ie for the url
def getAll():
    response = requests.get(url)
    return response.json()

# This will write the JSON results out to file cso.json
if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)
    fp.close()
    