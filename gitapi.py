import getpass
from github import Github

# First create a Github instance:

user = input("Github Username: ")
pw = getpass.getpass("Password: ")

# using username and password
g = Github(user, pw)

# or using an access token
#g = Github("fa9aff87f25bf654509cabc6748346b685906eed")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
