
import os
from tkinter import filedialog, Tk
from PyPDF2.merger import PdfFileMerger
from core.system import *
from core.development import *

def PDFsMerger(pathx: str, pathy: str, dest_folder: str):
    merger = PdfFileMerger()
    merger.append(pathx)
    merger.append(pathy)

    name_pathx = pathx.split("\\")[-1].split(".")[0]
    name_pathy = pathy.split("\\")[-1].split(".")[0]

    merger.write("{}\\{}-{}_merged.pdf".format(dest_folder, name_pathx, name_pathy))
    merger.close()

def app():
    while 1:
        clearscreen()
        IntroductionMessage("PDFMerger application\ninsert 2 pdfs and merge them")

        pdf_1 = input("[enter the path for pdf 1] or [DRAG AND DROP the pdf 1]:\n>>> ")
        if not os.path.isfile(pdf_1):
            print("repeat.")

        pdf_2 = input("\n[enter the path for pdf 2] or [DRAG AND DROP the pdf 2]:\n>>> ")
        if not os.path.isfile(pdf_2):
            print("repeat.")

        print("choose destination folder:\n")
        window = Tk()
        # window.withdraw()

        destination_folder = filedialog.askdirectory()
        print(destination_folder)

        PDFsMerger(pdf_1, pdf_2, destination_folder)
        print("pdfs merged successfully!")



if __name__ == '__main__':
    app()