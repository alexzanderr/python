
from github import Github
from core.json__ import (
    read_json_from_file,
    write_json_to_file
)

token_json_path = "token.json"
token_json = read_json_from_file(token_json_path)
token = token_json["token"]

client_github = Github(token)

# Then play with your Github objects:
for repo in client_github.get_user().get_repos():
    print(repo.name)


