
# current project
from ProjectBuilder import templates

# python
from pathlib import Path
import shutil

# core
from core import json__
from core import aesthetics

# this relative import only works if you import this __file__
# from .templates import imports_py_template

project_current_folder = Path(".")
tests_folder = Path("tests")
# making sure it exists
if not tests_folder.exists():
    tests_folder.mkdir()
else:
    # clearing existent contents
    shutil.rmtree(tests_folder)
    # creating for the first time
    tests_folder.mkdir()


def generate_project(project_name: str, destination=None):
    if destination:
        if isinstance(destination, Path):
            project_folder = destination / project_name
        elif isinstance(destination, str):
            project_folder = Path(destination) / project_name
    else:
        project_folder = tests_folder / project_name

    # create the folder of project
    project_folder.mkdir(exist_ok=True)

    __init__py = project_folder / "__init__.py"
    __init__py.write_text(templates.__init__py_template)

    imports_py = project_folder / "imports.py"
    imports_py.write_text(templates.imports_py_template.safe_substitute(
        project_name=project_name
    ))

    main_file = project_folder / f"_{project_name}.py"
    main_file.write_text(templates.main_py_template.safe_substitute(
        project_name=project_name
    ))

    TestingProject_py = project_folder / "TestingProject.py"
    TestingProject_py.write_text(templates.TestingProject_py_template.safe_substitute(
        project_name=project_name
    ))

    logs_folder = project_folder / "logs"
    logs_folder.mkdir(exist_ok=True)

    icons_folder = project_folder / "icons"
    icons_folder.mkdir(exist_ok=True)


if __name__ == '__main__':
    import sys
    program_arguments = sys.argv
    print("Program Arguments:")
    json__.pretty_print(program_arguments)

    # got the project name
    if len(program_arguments) == 2:
        project_name = program_arguments[1]

        aesthetics.print_red_bold(project_name)

        generate_project(project_name)

        print(f"project: {project_name}\ngenerated under: {tests_folder.absolute()}\n")


    # got the project name and location
    elif len(program_arguments) == 3:
        project_name = program_arguments[1]
        destination = program_arguments[2]

        aesthetics.print_red_bold(project_name)
        aesthetics.print_red_bold(destination)

        generate_project(project_name, destination)

        print(f"project: {project_name}\ngenerated under: {destination}\n")
