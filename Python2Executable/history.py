

from Python2Executable.imports import *

logger_History = logging.getLogger("history.py")
logger_History.setLevel(logging.INFO)
logger_History.addHandler(file_handler_Python2Executable)
logger_History.addHandler(stream_handler_Python2Executable)

cwd = os.getcwd()
all_projects_json_path = os.path.join(cwd, "projects_history", "all_projects.json")
last_project_json_path = os.path.join(cwd, "projects_history", "last_project.json")


all_projects_json = read_json_from_file(all_projects_json_path)
logger_History.info(f"all projects json read from:\n{all_projects_json_path}")
last_project_json = read_json_from_file(last_project_json_path)
logger_History.info(f"last project json read from:\n{last_project_json_path}")


class ProjectSpecs(object):
    """
    example of input

    "project_folder": "D:/Alexzander__/programming/python/Python2Executable",
    "python_file": "D:/Alexzander__/programming/python/Python2Executable/Python2Executable.py",
    "icon_file": "D:/Alexzander__/programming/python/Python2Executable/icons/exec.ico",

    "project_name": "Python2Executable",
    "dist_path": "D:/Alexzander__/programming/python/Python2Executable/dist",
    "work_path": "D:/Alexzander__/programming/python/Python2Executable/build",
    "spec_path": "D:/Alexzander__/programming/python/Python2Executable"
    """
    def __init__(self, project_folder, python_file, icon_file,
                 project_name, dist_path, work_path, spec_path):

        # these 3 are important for __str__
        self.python_file = python_file
        self.project_folder = project_folder
        self.icon_file = icon_file

        self.project_name = project_name
        self.dist_path = dist_path
        self.work_path = work_path
        self.spec_path = spec_path


    def __str__(self):
        representation  = f"  --> project-name: {yellow(self.project_name)}\n"
        representation += f"  --> project-folder: {yellow(self.project_folder)}\n"
        representation += f"  --> python-file: {blue(self.python_file)}\n"
        representation += f"  --> icon-file: {green(self.icon_file)}\n"
        return representation


    def __dict__(self):
        return {
            "project_folder": self.project_folder,
            "python_file": self.python_file,
            "icon_file": self.icon_file,
            "project_name": self.project_name,
            "dist_path": self.dist_path,
            "work_path": self.work_path,
            "spec_path": self.spec_path
        }


all_projects = [
    ProjectSpecs(*_dict.values()) for _dict in all_projects_json
]
logger_History.info(f"all projects list with:\n{ProjectSpecs.__name__} objects\ncreated")


def PrintHistoryProjects():
    for index, project in enumerate(all_projects, start=1):
        print(f"[ {yellow_bold(index)} ]:")
        print(project)
        print()


def CheckExistenceOfProject(
    python_file: str,
    project_folder: str,
    project_name: str
):
    found = False
    for project in all_projects:
        if project.python_file == python_file:
            found = True
            logger_History.info(
                f"project: {project.project_name}\nfrom path: {project.project_folder}\nwith python file: {python_file}\nis already in database"
            )
            break

    if not found:
        logger_History.info(f"project:\n{project_folder}\nnot found in database")
        # example
        # D:/Alexzander__/programming/python/Python2Executable/Python2Executable.py

        logger_History.info(f"adding project:\n{project_folder}...")

        icon_file = project_folder + "/icons/exec.ico"
        # here should be python_file, but already exists
        dist_path = project_folder + "/dist"
        work_path = project_folder + "/build"

        # adding a new project to the existing list
        project = ProjectSpecs(
            project_folder = project_folder,
            python_file = python_file,
            icon_file = icon_file,
            project_name = project_name,
            dist_path = dist_path,
            work_path = work_path,
            spec_path = project_folder
        )

        all_projects.append(project)
        logger_History.info(f"all_projects list updated with:\n{project_folder}")
        all_projects_json.append(project.__dict__())
        logger_History.info(f"all_projects json updated with:\n{project_folder}")

        del project
        # new project is added to database
        write_json_to_file(all_projects_json, all_projects_json_path)
        logger_History.info(f"project:\n{project_folder}\nadded to database")


def UpdateLastProject(
    python_file: str,
    project_folder: str,
    project_name: str
):
    """
        writes a json with the last project used in build
    """
    write_json_to_file(
        ProjectSpecs(
                project_folder = project_folder,
                python_file = python_file,
                icon_file = os.path.join(project_folder, "icons", "exec.ico"),
                project_name = project_name,
                dist_path = os.path.join(project_folder, "dist"),
                work_path = os.path.join(project_folder, "build"),
                spec_path = project_folder
        ).__dict__(),
        last_project_json_path
    )


if __name__ == '__main__':
    # CheckExistenceOfProject(r"D:\Alexzander__\programming\python\PythonInteractive\PythonIteractive.py")
    pass
