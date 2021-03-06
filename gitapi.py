import getpass
import json
from github import Github

# First create a Github instance:

user = input("Github Username: ")
pw = getpass.getpass("Password: ")

# using username and password
g = Github(user, pw)

# or using an access token
#g = Github("fa9aff87f25bf654509cabc6748346b685906eed")

repo = g.get_repo("d3/d3")
comCount = 0
commits = {}
for commit in repo.get_commits():
    cname = commit.commit.author.name
    try:
        commits[cname] = commits[cname] + 1
    except:
        commits[cname] = 1

#awful way of doing it (also wrong)
list = {}
list['data'] = []
for name in commits:
    list['data'].append({'name':name,'commits':commits[name]})

with open("data.json", "w") as write_file:
    json.dump(list, write_file)

# Then play with your Github objects:
'''
for repo in g.get_user().get_repos():
    print(repo.name)
    for contrib in repo.get_contributors():
        print("Contributor: " + contrib.login)

    comCount = 0
    commits = {}
    for commit in repo.get_commits():
        cname = commit.commit.author.name
        try:
            commits[cname] = commits[cname] + 1
        except:
            commits[cname] = 1
    print(str(commits) + "\n")
'''