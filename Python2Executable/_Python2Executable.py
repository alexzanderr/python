

# IMPORTS
from Python2Executable.imports import *

# HISTORY OF COMPILED PROJECTS
from Python2Executable.history import (
    PrintHistoryProjects,
    all_projects,
    CheckExistenceOfProject,
    UpdateLastProject
)

# BUILD
from Python2Executable.build import PyinstallerScript

# BEGINNING VALIDATION
from Python2Executable.validation import is_valid_extension

# COPY
from Python2Executable.transfer import (
    CopyProjectToPythonApplications,
    remote_location_template,
    shortcuts_location_folder
)

# NSIS
from Python2Executable.nsis import (
    GenerateNSIScript,
    CompileNSIScript
)

# DELETE
from Python2Executable.delete import DeleteBuildAndDistFromProjectLocation


__appname__ = "Python2Executable"
__version__ = "0.0.2"
__author__  = "alexzander"


auto_prompt_message = f"""choose your project:
[<enter> ({enter_symbol}) activates manual mode]
{left_arrow_3_green_bold} """

manual_prompt_message = f"""[enter your python file or spec file] or [drag and drop]:
[<enter> ({enter_symbol}) activates auto mode]
{left_arrow_3_green_bold} """


# current project main logger
logger_Python2Executable = logging.getLogger("Python2Executable")
logger_Python2Executable.setLevel(logging.INFO)
logger_Python2Executable.addHandler(stream_handler_Python2Executable) # for print
logger_Python2Executable.addHandler(file_handler_Python2Executable) # for file

logger_Python2Executable.info(f"logger_Python2Executable has format style:\n{formatter_Python2Executable.datefmt}")


def ProjectBuild(
    python_file,
    project_folder,
    project_name,
    remote_location,
    auto
):
    # pyinstaller build
    PyinstallerScript(python_file, project_folder, project_name)

    # move files to remote location
    # and create shortcut of exe
    CopyProjectToPythonApplications(
        project_folder,
        project_name,
        remote_location
    )

    # generate nsi script
    nsis_script_path = GenerateNSIScript(remote_location, project_name)
    # compile nsi script into executable installer
    CompileNSIScript(nsis_script_path, remote_location)

    UpdateLastProject(
        python_file,
        project_folder,
        project_name
    )
    logger_Python2Executable.info(f"project: {project_name} was compiled successfully")

    result = DeleteBuildAndDistFromProjectLocation(project_folder)
    if result == True:
        logger_Python2Executable.info(f"successfully deleted dist and build folder from:\n{project_folder}")
    else:
        logger_Python2Executable.info(f"something went wrong in deletetion of dist and build:\n{result}")

    open_folder(remote_location)
    logger_Python2Executable.info(f"remote location opened:\n{remote_location}")

    open_folder(shortcuts_location_folder)
    logger_Python2Executable.info(f"shortcuts folder opened:\n{shortcuts_location_folder}")





def FailSafeSystem():
    _enter_ = green_bold("<enter>")
    _yes_ = green_bold("y")
    _no_ = red_bold("n")
    proceed = input(f"\nproceed to {yellow_bold('BUILD')}?\n[{_yes_}(es) and {_enter_} | {_no_}(o)]:\n{left_arrow_3_green_bold} ")
    if proceed != "y" and proceed != "":
        return False

    if proceed == "":
        proceed = input(f"\npress {_enter_} again to confirm\n[anything alse will {red_bold('cancel')} the build]\n[in case you pressed by mistake]:\n{left_arrow_3_green_bold} ")
        if proceed != "":
            return False

    return True


def app_title():
    print_green_bold(__appname__)
    print_green_bold("=" * len(__appname__))
    print()


def Python2Executable():
    auto = True
    while 1:
        try:
            clearscreen()
            app_title()

            if auto:
                # automatic choice
                PrintHistoryProjects()
                choice = input(auto_prompt_message)
                try:
                    choice = int(choice)
                except ValueError:
                    if choice == "":
                        auto = False
                        continue
                else:
                    if 1 <= choice <= len(all_projects):
                        # print(all_projects[choice - 1])
                        print(f"\nproject number [ {red_bold(choice)} ] {yellow('selected')}:")
                        print(f"\tname: {yellow(all_projects[choice - 1].project_name)}")
                        print(f"\tlocation: {cyan_underlined(all_projects[choice - 1].project_folder)}")
                        print(f"\tpython: {green_underlined(all_projects[choice - 1].python_file)}")

                        action = FailSafeSystem()
                        if action == False:
                            continue

                        # starting point in time
                        before = time()

                        # python file path
                        python_file = all_projects[choice - 1].python_file
                        # project folder path (where python file is located)
                        project_folder = all_projects[choice - 1].project_folder
                        # project name
                        project_name = all_projects[choice - 1].project_name
                        # location where builded project will be copied
                        remote_location = remote_location_template.safe_substitute(
                            project_name=project_name
                        )

                        del choice

                        ProjectBuild(
                            python_file,
                            project_folder,
                            project_name,
                            remote_location,
                            auto
                        )

                        # end
                        duration = time() - before
                        duration = fixed_set_precision_str(duration, 2)
                        print(f"execution time: [ {yellow_bold(duration)} ] second(s)")

                        del duration
                    else:
                        continue
            else:
                # manual insertion of file
                auto = True
                python_file = input(manual_prompt_message)
                if python_file == "":
                    continue

                if not os.path.isfile(python_file):
                    auto = False
                    continue

                if not is_valid_extension(python_file):
                    auto = False
                    continue

                action = FailSafeSystem()
                if action == False:
                    continue

                del choice

                # starting point in time
                before = time()

                # path
                project_folder = os.path.dirname(python_file)
                # name
                project_name = os.path.basename(project_folder)
                # location where builded project will be copied
                remote_location = remote_location_template.safe_substitute(
                    project_name=project_name
                )

                # history.py
                CheckExistenceOfProject(python_file, project_folder, project_name)

                ProjectBuild(
                    python_file,
                    project_folder,
                    project_name,
                    remote_location,
                    auto
                )

                # end
                duration = time() - before
                duration = fixed_set_precision_str(duration, 2)
                print(f"execution time: [ {yellow_bold(duration)} ] second(s)")

                del duration

        except KeyboardInterrupt:
            print("\n")
            print_yellow_bold(__appname__)
            print(f"application {red_bold('closed')} from [ {red_bold(KeyboardInterrupt.__name__)} ]")
            break

        except BaseException as error:
            logger_Python2Executable.exception("exception!!!!!!!!!")
            print_red_bold(type(error))
            print_red_bold(error)

            print()
            pauseprogram()


        # no errors, build was successful
        else:
            print()
            pauseprogram()



if __name__ == '__main__':
    Python2Executable()