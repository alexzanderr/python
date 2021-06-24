

from Python2Executable.imports import *



def DeleteBuildAndDistFromProjectLocation(project_folder):
    """ removes dist and build from project

    Args:
        project_folder ([str] or [pathlib.Path]): [
            path to python project that is compiled
        ]

    Raises:
        TypeError: [
            when type of @project_folder is not: [str] or [pathlib.Path]
        ]
    """
    if type(project_folder) not in [str, Path]:
        raise TypeError(f"{project_folder} should be 'str' or 'Path' object.")

    try:
        if isinstance(project_folder, Path):
            build = project_folder / "build"
            dist = project_folder / "dist"

        elif isinstance(project_folder, str):
            projfol = Path(project_folder)

            build = projfol / "build"
            dist = projfol / "dist"

        delete_folder(build, verbose=True)
        delete_folder(dist, verbose=True)

    except Exception as error:
        print(f"error: {error}")
        return str(error)

    # success
    return True