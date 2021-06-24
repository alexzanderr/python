

from PyPIAutoUpload.imports import *


logger_Upload = Loggerr(
    name="upload.py",
    file_handler=file_handler_PyPIAutoUpload,
    stream_handler=stream_handler_PyPIAutoUpload
)

upload_commands_list = [
    "python -m pip install --user --upgrade setuptools wheel",
    "python setup.py sdist bdist_wheel",
    "python -m pip install --user --upgrade twine",
    "python -m twine upload --verbose dist/*"
]

def UploadPackageToPyPI(package_name, uploaded_package_folder, version):
    cwd = os.getcwd()
    try:
        os.chdir(uploaded_package_folder)
        for command in upload_commands_list:
            logger_Upload.info(f"\nexecuting command: {blue_bold(command)}\n")
            os.system(command)

        logger_Upload.info("package: {} | version: {} was uploaded to pypi successfully!".format(package_name, green_bold(version)))

    except Exception as err:
        logger_Upload.exception("error {} in UploadPackageToPyPI()".format(type(err)))

    os.chdir(cwd)



if __name__ == '__main__':
    f = r"D:\Alexzander__\programming\python\PyPIAutoUpload\uploaded\package_bitcoin"
    n = "bitcoin-test"
    v = "0.0.9"
    UploadPackageToPyPI(n, f, v)
    