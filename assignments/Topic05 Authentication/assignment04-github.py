#
# Ciaran Moran
# G00426050@atu.ie
# Topic05 Authentication
# Assignment: Assignment 04 
# Description: Write a program in python that will read a file from a repository, 
#           The program should then replace all the instances of the text "Andrew" with your name. 
#           The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).
# Based on re-used code from https://github.com/andrewbeattycourseware/wsaa-course-material/tree/main/code/Topic05-authentication/labs
#
import requests
import json
from config import config as cfg

filename = "repos-private.json"

url = 'https://github.com/cpjm/WSAA-coursework/tree/main/assignments/Topic05%20Authentication'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)
