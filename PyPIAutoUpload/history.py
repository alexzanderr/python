

from PyPIAutoUpload.imports import *

logger_History = Loggerr(
    "history.py",
    file_handler=file_handler_PyPIAutoUpload,
    stream_handler=stream_handler_PyPIAutoUpload
)


cwd = os.getcwd()
all_packages_json_path = os.path.join(cwd, "packages_history", "all_packages.json")
last_package_json_path = os.path.join(cwd, "packages_history", "last_package.json")


all_packages_json = read_json_from_file(all_packages_json_path)
logger_History.info(f"all packages json read from:\n{all_packages_json_path}")

last_package_json = read_json_from_file(last_package_json_path)
logger_History.info(f"last package json read from:\n{last_package_json_path}")


class PackageSpecs(object):
    """
    example of input

    "package-folder": "D:\\Alexzander__\\programming\\python\\core",
    "custom-name": "python-core"
    """
    def __init__(
        self,
        package_name: str,
        package_folder: str,
        custom_name: str
    ):
        self.name = package_name
        self.folder = package_folder
        self.custom_name = custom_name


    def __str__(self):
        representation  = f"  --> package-name: {yellow_bold(self.name)}\n"
        representation += f"  --> package-folder: {cyan(self.folder)}\n"
        representation += f"  --> custom-name: {blue_bold(self.custom_name)}\n"
        return representation


all_packages = [
    PackageSpecs(*_dict.values()) for _dict in all_packages_json
]
logger_History.info(f"all packages list with:\n{PackageSpecs.__name__} objects\ncreated")


def PrintPackagesHistory():
    for index, package in enumerate(all_packages, start=1):
        print(f"[ {yellow_bold(index)} ]:")
        print(package)
        print()


def CheckExistenceOfPackage(
    package_name: str,
    package_folder: str,
    custom_name: str
):
    found = False
    for package in all_packages:
        if package.folder == package_folder:
            found = True
            logger_History.info(
                f"package: {package.name}\n\
                  from path: {package.folder}\n\
                  is already in database"
            )
            break

    if not found:
        logger_History.info(f"package:\n{package_folder}\nnot found in database")
        logger_History.info(f"adding package:\n{package_folder}...")


        # adding a new package to the existing list
        package = PackageSpecs(
            package_name=package_name,
            package_folder=package_folder,
            custom_name=custom_name
        )

        all_packages.append(package)
        logger_History.info(f"all_packages list updated with:\n{package_folder}")
        all_packages_json.append(package.__dict__)
        logger_History.info(f"all_packages json updated with:\n{package_folder}")

        del package
        # new package is added to database
        write_json_to_file(all_packages_json, all_packages_json_path)
        logger_History.info(f"package:\n{package_folder}\nadded to database")


def UpdateLastProject(
    package_name: str,
    package_folder: str,
    custom_name: str
):
    """
        writes a json with the last package used in build
    """
    package = PackageSpecs(
        package_name=package_name,
        package_folder=package_folder,
        custom_name=custom_name
    )
    write_json_to_file(
        package.__dict__,
        last_package_json_path
    )
    logger_History.info(f"last package updated with:\n{package}")



if __name__ == '__main__':
    # PrintPackagesHistory()
    # UpdateLastProject(*all_packages_json[-1].values())
    pass