
from pathlib import Path
from core.aesthetics import *
from core.json__ import (
    read_json_from_file,
    write_json_to_file
)
import os
import sys


cwd = Path(os.getcwd())
print(f"cwd: {cwd}")

def check_if_inside_git_repo(cwd: Path):
    dirname = cwd.parents[0]
    #  print(type(dirname)) posixPath
    while dirname.as_posix() != "/":
        if (dirname / ".git").exists():
            return dirname.absolute().as_posix()

        dirname = dirname.parents[0]
        print(dirname)
    #  while "/" in cwd.parents:
    #  if cwd.parents.
    return False

result = check_if_inside_git_repo(cwd)
if result:
    print(f"git repo already existent at:\n{result}")
    print("aborted")
    sys.exit(0)


credentials_json_path = "/home/alexzander/Alexzander__/programming/python3/ManageGithubAccount/credentials.json"
credentials_json = read_json_from_file(credentials_json_path)
token = credentials_json["token"]
username = credentials_json["username"]

repo_name = cwd.name
#  print(repo_name)
dotgit_folder = cwd / ".git"

if dotgit_folder.exists():
    print(".git exists | aborted")
    sys.exit(0)

from core.datetime__ import get_current_datetime

commands = [
    "git init",
    "git add .",
    f"git commit -m \"{get_current_datetime()}\"",
    f"git remote add origin https://{username}:{token}@github.com/{username}/{repo_name}.git",
    "git push -f origin master"
]



decision = input("are you sure? [y/n]:\n>>> ")
if decision != "y" and decision != "":
    print("aborted")
    sys.exit(0)


for command in commands:
    print_yellow_bold(command)
    os.system(command)

print("done")

