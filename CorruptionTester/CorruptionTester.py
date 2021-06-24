
import zipfile
import os
from core.system import *
from core.development import *

def app():
    while 1:
        clearscreen()
        IntroductionMessage("CorruptionTester application\nenter only zip files to test corruption")
        while True:
            zipfile_fpath = input("[drag zip file] or [enter path]:\n>>> ")
            if os.path.isabs(zipfile_fpath):
                break
            if not zipfile_fpath.endswith(".zip"):
                print("wrong.")
            os.system("cls")

        zip_file = zipfile.ZipFile(zipfile_fpath)

        print(f"\nVerifying corruption status on: '{zipfile_fpath}' ...\n")
        try:
            result = zip_file.testzip()
            if result is None:
                print_green_bold("Zip file is CLEAN.\n")
            else:
                print_red_bold("Zip file is CORRUPTED.\n")
        except ValueError:
            print_red_bold("Zip file is CORRUPTED.\n")

        pauseprogram()

if __name__ == '__main__':
    app()