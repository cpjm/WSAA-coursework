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

from github import Github
from config import config as cfg

import os
# had to install the git library for this
# using pip install GitPython 
# info from https://bobbyhadz.com/blog/python-no-module-named-git
from git import Repo


# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["githubkey"]

#response = requests.get(url, auth = ('token', apikey))
#print (response.status_code)
##print (response.json())
#with  open(filename, 'w') as fp:
#    repoJSON = response.json()
#    json.dump(repoJSON, fp, indent=4)

# Following code based on re-usued code and ideas from:-
# https://stackoverflow.com/questions/50071841/how-to-push-local-files-to-github-using-python-or-post-a-commit-via-python
# https://stackoverflow.com/questions/67706647/how-to-add-commit-and-push-a-repository-via-git-python
# https://stackoverflow.com/questions/74857784/how-to-add-python-files-to-a-new-repository-in-github
# https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28
# https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#update-a-file
# https://stackoverflow.com/questions/56548113/use-python-along-with-github-api-to-collect-data-from-a-repo
# https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28

# Test access and list repo names
g = Github(apikey)
#for repo in g.get_user().get_repos():
# print(repo.name)

# Open my git repository
#url = 'https://github.com/cpjm/WSAA-coursework/tree/main/assignments/Topic05%20Authentication/'
#url = 'https://github.com/cpjm/WSAA-coursework/tree/main/assignments/Topic05-Authentication/'
url = 'https://github.com/cpjm/WSAA-coursework/'
filename = "assignments/Topic05-Authentication/testfile.txt"

#repo = Repo(url)
#repo in g.get_user().get_repo('https://github.com/cpjm/WSAA-coursework')
#repo = g.get_user().get_repo(url)

print("**********Get Current Repos**********")
user = g.get_user()
user.login
print(user.login)
print("**********Get Current Repos - 1**********")
#repo = g.get_repo('http://api.github.com/repos/cpjm/WSAA-coursework/assignments/Topic05-Authentication')
repo = user.get_repo('WSAA-coursework')
print("**********Get Current Repos - 2**********")
repo.name
print(repo.name)
print("********Get the Repo Topics**************")

# Fetch latest changes
#origin = repo.remotes.origin
#origin.fetch()

# Checkout to master branch
repo.git.checkout('/assignments/Topic05-Authentication/testfile.txt')

# Replace text
# with help from https://stackoverflow.com/questions/4128144/replace-string-within-file-contents
#
file_path = os.path.join(url, filename)
with open(file_path, 'r') as file:
        file_data = file.read()

file_data = file_data.replace('Andrew', 'Ciaran')

with open(file_path, 'w') as file:
    file.write(file_data)

# Stage changes
repo.index.add([filename])

# Commit changes
repo.index.commit("Replace all instances of 'Andrew' with 'Ciaran'")
print("Changes have been committed")

# Push changes
origin.push()
print("Changes have been pushed")