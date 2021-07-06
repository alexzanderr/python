

import os
from github import Github

from core.aesthetics import *
from core.json__ import (
    read_json_from_file,
    write_json_to_file
)
import requests
from string import Template

credentials_json_path = "credentials.json"
credentials_json = read_json_from_file(credentials_json_path)
token = credentials_json["token"]
username = credentials_json["username"]

client_github = Github(token)

# Then play with your Github objects:
for repo in client_github.get_user().get_repos():
    print(repo.name)


def create_github_repo(new_repo_name: str):
    """
        creates a repo for the first time 
        using curl implementation
    """
    curl_command_template = Template(
        "curl -H \"Authorization: token ${token}\" --data '{\"name\":\"${repo_name}\"}' https://api.github.com/user/repos"
    )
    curl_command = curl_command_template.safe_substitute(
        token=token,
        repo_name=new_repo_name
    )
    print_yellow_bold(curl_command)
    os.system(curl_command)


def delete_github_repo(repo_name: str):
    """
        deletes a repo using curl implementation
    """
    curl_command_template = Template(
        "curl -X DELETE -H 'Authorization: token ${token}' https://api.github.com/repos/${username}/${repo_name}" 
    )
    curl_command = curl_command_template.safe_substitute(
        token=token,
        username=username,
        repo_name=repo_name
    )
    print_yellow_bold(curl_command)
    os.system(curl_command)


if __name__ == "__main__":
    #  create_github_repo("repo-from-cli")
    delete_github_repo("repo-from-cli")

    





