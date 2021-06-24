
import os
import webbrowser
from core.path__ import *
from core.datetime__ import *
from core.aesthetics import *
from core.winapi__ import windows_notification

if is_abs(__file__):
    sep = get_path_sep(__file__)
    project_folder = sep.join(__file__.split(sep)[:-1])
else:
    project_folder = os.getcwd()

print("\nRepository Folder: {}\n".format(cyan(project_folder)))

current_timedate = get_current_timedate()
commit_message = "{} update | remote method | from CLI".format(current_timedate)

repo_url = "https://github.com/alexzanderr/python372"
repo_git_url = "https://github.com/alexzanderr/python372.git"

sep = "\\"

commands = [
    "rmdir /S /Q {}".format(project_folder + sep + ".git"),
    "git init",
    "git add .",
    "git commit -m \"{}\"".format(commit_message),
    "git remote add origin {}".format(repo_git_url),
    "git push -f origin master"
]

colored_commands = [
    f"{red_bold('rmdir')} /S /Q {cyan(project_folder + sep + '.git')}",
    f"{yellow_bold('git')} init",
    f"{yellow_bold('git')} add .",
    f"{yellow_bold('git')} commit - m \"{green(commit_message)}\"",
    f"{yellow_bold('git')} remote add origin {orange_underlined(repo_git_url)}",
    f"{yellow_bold('git')} push -f origin master"
]

print("The following commands will be executed:")
for c in colored_commands:
    print("\t" + c)

choice = input("\nproceed? [y/n]:\n>>> ")
if choice == "y":
    os.chdir(project_folder)

    print()
    for command, command_colored  in zip(commands, colored_commands):
        print(command_colored)
        os.system(command)

    print_green("\nrepo {} was updated successfully!\n".format(cyan_underlined(repo_url)))

    webbrowser.open(repo_url)

    windows_notification(
        "Github",
        "Repo: alexzander/python372\nUPDATED",
        5,
        "python_logo.ico",
        1
    )