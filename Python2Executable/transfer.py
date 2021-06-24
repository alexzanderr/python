
from Python2Executable.imports import *


logger_Copy = logging.getLogger("transfer.py")
logger_Copy.setLevel(logging.INFO)
logger_Copy.addHandler(file_handler_Python2Executable)
logger_Copy.addHandler(stream_handler_Python2Executable)

shortcuts_location_folder = "D:{sep}Alexzander__{sep}PythonApplicationsShortcuts".format(sep=os.path.sep)
logger_Copy.info(f"shortcuts remote location:\n{shortcuts_location_folder}")

remote_location_template = Template("D:${sep}Alexzander__${sep}PythonApplications${sep}${project_name}")
remote_location_template = Template(remote_location_template.safe_substitute(sep=os.path.sep))

exe_ignore = [
    "build",
    "dist",
    "__pycache__",
    "*.spec",
    ".idea",
    ".vscode"
]
logger_Copy.info("exe ignore:\n{}".format("\n\t".join(exe_ignore)))


def PrepareProjectContents(
    project_folder: str,
    project_name: str,
    remote_location: str
):
    """
        we need everything from  'project_folder/dist/{project_name}'

        and everything from @project_folder except
            build
            __pycache__
            *.spec
            .idea
            .vscode
    """
    project_contents = gather_relatives(project_folder, __ignore=exe_ignore)
    logger_Copy.info("project contents generated")

    # for pj in project_contents:
    #     print(pj)

    dist_folder = os.path.join(project_folder, "dist", project_name)
    dist_contents = gather_relatives(dist_folder)
    logger_Copy.info("dist contents generated")


    # for dt in dist_contents:
    #     print(dt)

    # source
    source_full_paths = [project_folder + project_content for project_content in project_contents]
    source_full_paths.extend([dist_folder + dist_content for dist_content in dist_contents])
    logger_Copy.info("source full paths generated")

    # destination
    destination_full_paths = [remote_location + project_content for project_content in project_contents]
    destination_full_paths.extend([remote_location + dist_content for dist_content in dist_contents])
    logger_Copy.info("destination full paths generated")

    return source_full_paths, destination_full_paths



def CopyProjectToPythonApplications(
    project_folder: str,
    project_name: str,
    remote_location: str
):
    """
        this moves every content from @project_folder to
        remote location: D:\\Alexzander__\\PythonApplications\\{project_name}

        and creates shortcut of executable
    """

    source, destination = PrepareProjectContents(project_folder, project_name, remote_location)

    # for s in source:
    #     print(s)

    # for d in destination:
    #     print(d)
    # return

    copy_content(
        source,
        destination,
        __print=True
    )
    logger_Copy.info(f"contents from:\n{project_folder}\ncopied to remote_location:\n{remote_location}")

    exe = os.path.join(remote_location, project_name + ".exe")
    create_shortcut(
        exe,
        shortcuts_location_folder
    )
    logger_Copy.info(f"shortcut of exe:\n{exe}\ngenerated")



if __name__ == '__main__':
    p = "D:/Alexzander__/programming/python/Python2Executable"
    p = "D:/Alexzander__/programming/python/PyPI_AutoUpload"
    p = "D:/Alexzander__/programming/python/Timer"
    p = "D:/Alexzander__/programming/python/PDFCreator"
    p = p.replace("/", os.path.sep)
    CopyProjectToPythonApplications(p)
    pass