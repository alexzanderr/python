

# project
from Python2Executable.imports import *


logger_Pyinstaller = logging.getLogger("build.py")
logger_Pyinstaller.setLevel(logging.INFO)
logger_Pyinstaller.addHandler(file_handler_Python2Executable)
logger_Pyinstaller.addHandler(stream_handler_Python2Executable)


excceed_recursion_line = "import sys; sys.setrecursionlimit(sys.getrecursionlimit() * 5)\n"

pyinstaller_recursion_error = "A RecursionError (maximum recursion depth exceeded) occurred."

pyinstaller_script_python_template = Template(
    "pyinstaller.exe --noconfirm --onedir --distpath=${distpath}${sep}dist --workpath=${workpath}${sep}build --specpath=${specpath} --icon=${icon_path} --name=${executable_name} ${python_file_path}"
)
pyinstaller_script_python_template = Template(
    pyinstaller_script_python_template.safe_substitute(sep=os.path.sep)
)

pyinstaller_script_spec_template = Template(
    "pyinstaller.exe --noconfirm --distpath=${distpath}${sep}dist --workpath=${workpath}${sep}build --specpath=${specpath} ${spec_file_path}"
)
pyinstaller_script_spec_template = Template(
    pyinstaller_script_spec_template.safe_substitute(sep=os.path.sep)
)


def PyinstallerScript(
    file: str,
    project_folder: str,
    project_name: str
):
    """ takes python file of spec file for building """

    #
    project_build_logs_path = os.path.join(project_folder, "build_logs")
    if not os.path.exists(project_build_logs_path):
        os.makedirs(project_build_logs_path)

    build_logs_folder_items = os.listdir(project_build_logs_path)
    if len(build_logs_folder_items) > 10:
        for item in build_logs_folder_items:
            os.remove(os.path.join(project_build_logs_path, item))

    del build_logs_folder_items

    # creating a log file for the builded project itself
    # located in <project_folder>
    current_datetime = get_current_datetime(__format="%d.%m.%Y__%H_%M_%S")
    file_handler_BuildedProject = logging.FileHandler(
        os.path.join(project_build_logs_path, f"build_{current_datetime}.log")
    )
    file_handler_BuildedProject.setLevel(20)
    file_handler_BuildedProject.setFormatter(formatter_Python2Executable)
    del current_datetime, project_build_logs_path

    # adding this file handler to pyinstaller logger
    logger_Pyinstaller.addHandler(file_handler_BuildedProject)

    # this is the Python2Executable project path
    cwd = os.getcwd()
    # not the builded project path

    logger_Pyinstaller.info(f"current working dir:\n{cwd}\n(Python2Executable project)")
    logger_Pyinstaller.info(f"project folder path:\n{project_folder}")
    logger_Pyinstaller.info(f"project folder name:\n{project_name}")

    # name plus extension
    file_name = os.path.basename(file)
    logger_Pyinstaller.info(f"file name:\n{file_name}\npath:\n{project_folder}")

    # python file
    if file.endswith(".py") or file.endswith(".pyw"):
        logger_Pyinstaller.info(f"in function:\n{PyinstallerScript.__name__}()\nparam @file:\n{file}\nis a python file")

        # try with icons
        icon_file_path = os.path.join(project_folder, "icons", "exec.ico")

        if not os.path.exists(icon_file_path):
            # try with assets
            icon_file_path = os.path.join(project_folder, "assets", "icons", "exec.ico")

            if not os.path.exists(icon_file_path):
                logger_Pyinstaller.info("icon for project doesnt exist. aborted.")
                raise core.exceptions.NotFoundError(f"icon: {icon_file_path} doesnt exist!")

        # pyinstaller --noconfirm --onedir --distpath=${distpath}/dist --workpath=${workpath}/build --specpath=${specpath} --icon=${icon_path} --name=${executable_name} ${python_file_path}
        __script = pyinstaller_script_python_template.safe_substitute(
            distpath=project_folder,
            workpath=project_folder,
            specpath=project_folder,
            icon_path=icon_file_path,
            executable_name=project_name,
            python_file_path=file
        )

    # spec file
    elif file.endswith(".spec"):
        logger_Pyinstaller.info(f"param @file:\n{file}\nis a spec file")

        # pyinstaller.exe --noconfirm --distpath=${distpath}/dist --workpath=${workpath}/build --specpath=${specpath} ${spec_file_path}
        __script = pyinstaller_script_spec_template.safe_substitute(
            distpath=project_folder,
            workpath=project_folder,
            specpath=project_folder,
            spec_file_path=file
        )

    del file

    logger_Pyinstaller.info("created pyinstaller script:\n{}".format(__script))
    logger_Pyinstaller.info(f"waiting for script:\n{yellow_bold(__script)}\nto finish...\n")

    # process object
    process = subprocess.Popen(
        __script,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    _, process_output = process.communicate()
    logger_Pyinstaller.info("got the process output, processing ...")

    # mega string of output
    process_output = process_output.decode("utf-8")
    logger_Pyinstaller.info("decoding to utf-8")
    logger_Pyinstaller.info("deleting \\r's")
    process_output = process_output.replace("\r", "")

    # list
    logger_Pyinstaller.info("spliting by \\n")
    process_output_lines = process_output.split("\n")


    # logging everything (not colored)
    for line in process_output_lines:
        logger_Pyinstaller.info(line)
    logger_Pyinstaller.info("logged every line of pyinstaller build")


    # this will be printed colored
    process_output_lines_colored = process_output_lines.copy()

    # modifying colors of the text and reformatting
    for i, line in enumerate(process_output_lines_colored):
        line_items = line.split()

        if "completed successfully" in line:
            line = line.replace("completed successfully", green("completed successfully"))

        if "INFO" in line:
            line = line.replace("INFO", f"[ {yellow('INFO')} ]")

        if "EXE" in line:
            line = line.replace("EXE", red_bold("EXE"))

        for j, line_item in enumerate(line_items):
            if is_valid_path(line_item):
                line = line.replace(line_item, cyan(line_item))

        process_output_lines_colored[i] = line

    logger_Pyinstaller.info("process output modified and colored")


    # keep this. is important (printing what i promised)
    logger_Pyinstaller.info("printing colored output...")
    for line in process_output_lines_colored:
        print(line)
    logger_Pyinstaller.info("printed every colored line of pyinstaller build")


    # trying to find recursion error message
    # because pyinstaller doesnt raise error, just tells message (stupid)
    logger_Pyinstaller.info("trying to find [recursion error]...")
    result = process_output.find(pyinstaller_recursion_error)
    if result != -1: # found the message -> means error
        logger_Pyinstaller.info("found [recursion error]!")

        # pyinstaller exceeded recursion limit -> PLAN B

        # open .spec file and insert,
        # import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)
        # at the beginning, programatically

        spec_file = os.path.join(project_folder, project_name + ".spec")
        if not os.path.exists(spec_file):
            logger_Pyinstaller.info("spec file doesnt exist")
            raise core.exceptions.NotFoundError(spec_file)


        logger_Pyinstaller.info(f"opening for read...\n{spec_file}")
        with open(spec_file, "r+", encoding="utf-8") as spec_read:
            spec_file_lines = spec_read.readlines()
            spec_file_lines.insert(0, excceed_recursion_line)
        logger_Pyinstaller.info("spec file contents read")

        logger_Pyinstaller.info(f"opening for write...\n{spec_file}")
        with open(spec_file, "w+", encoding="utf-8") as spec_write:
            spec_write.truncate(0)
            spec_write.writelines(spec_file_lines)
            del spec_file_lines
        logger_Pyinstaller.info("spec file contents updated")

        logger_Pyinstaller.info("line:\n{}\ninserted in spec file".format(excceed_recursion_line))

        # redoing everything recursivelly
        logger_Pyinstaller.info(f"recalling function:\n{PyinstallerScript.__name__}()\nrecursivelly with param @file:\n{spec_file}")
        PyinstallerScript(spec_file, project_folder, project_name)

    else:
        logger_Pyinstaller.info("[recursion error] NOT FOUND (good)")
        logger_Pyinstaller.info("pyinstaller completed")
        logger_Pyinstaller.info(f"project_folder:\n{project_folder}\nwas made exe")

        # exited with code=0
        logger_Pyinstaller.info(f"function\n{PyinstallerScript.__name__}()\breturned True")
        logger_Pyinstaller.info("build.py worked")

    return True






if __name__ == '__main__':
    python_file = r"D:\Alexzander__\programming\python\Python2Executable\simulate\simple_package\main.py"
    project_folder = r"D:\\Alexzander__\\programming\\python\\Python2Executable\\simulate\\simple_package"
    project_name = "simple_package"

    PyinstallerScript(python_file, project_folder, project_name)

    # pyinstaller.exe --noconfirm --onedir --distpath=D:\\Alexzander__\\programming\\python\\Python2Executable\\simulate\\simple_package/dist --workpath=D:\\Alexzander__\\programming\\python\\Python2Executable\\simulate\\simple_package/build --specpath=D:\\Alexzander__\\programming\\python\\Python2Executable\\simulate\\simple_package --icon=D:\\Alexzander__\\programming\\python\\Python2Executable\\simulate\\simple_package\icons\exec.ico --name=simple_package D:\Alexzander__\programming\python\Python2Executable\simulate\simple_package\main.py
