

def is_valid_extension(python_file: str):
    """ file should end with .py, .spec or .pyw """

    if not python_file.endswith(".py") and \
       not python_file.endswith(".spec") and \
       not python_file.endswith(".pyw"):
       return False
    return True