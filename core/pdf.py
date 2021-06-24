
"""
    core/pdf.py

    helpful with pdfs

    author: @alexzander
"""


# python
import os
from string import ascii_letters, digits, punctuation

# 3rd party
import pdfplumber # pip install pdfplumber
from PIL import Image # pip install Pillow
from PyPDF2.merger import PdfFileMerger # pip install pypdf2

# core package (pip install python-core)
from core.system import *
from core.aesthetics import ConsoleColored, underlined


def has_image_extension(img):
    ext = img.split(".")[1]
    image_extensions = ["jpg", "jpeg", "png", "JPG", "JPEG", "PNG"]
    if ext in image_extensions:
        return True
    return False


def get_text_from_pdf(__pdfpath: str):
    human_readable_chars = ascii_letters + digits + punctuation
    human_readable_chars = list(human_readable_chars) + ["\n", "\t", " "]

    __pdftext = ""
    with pdfplumber.open(__pdfpath) as pdf:
        for page in pdf.pages:
            modified_text = ""
            for char in page.extract_text():
                if char in human_readable_chars:
                    modified_text += char
            __pdftext += modified_text
    return __pdftext


def python_print_to_pdf(images_paths, PDFName):
    """
        alludes to: 'microsoft print to pdf' XDD
    """
    print("PythonPrintToPDF: processing...")

    # list with different paths with images
    if type(images_paths) == list:
        folder_path = images_paths[0].split("\\")
        folder_path = "\\".join(folder_path[:len(folder_path) - 1])
        ImagesArray = [Image.open(img).convert("RGB") for img in images_paths]

        print(ConsoleColored("merging photo(s) into pdf...", "yellow", bold=1))

        ImagesArray[0].save(folder_path + f"\\{PDFName}.pdf", save_all=True, append_images=ImagesArray[1:])
        location = folder_path

    # string parameter
    elif type(images_paths) == str:

        # folder with images
        if os.path.isdir(images_paths):
            pdf_path = images_paths + "\\{}.pdf".format(PDFName)

            if os.path.isfile(pdf_path):
                print(ConsoleColored("warning: pdf already existent.", "red", bold=1))
                os.remove(pdf_path)
                print(ConsoleColored("Existent pdf was deleted.", "red", bold=1))

            del pdf_path

            photos = [file for file in os.listdir(images_paths) if os.path.isfile(images_paths + "\\" + file) and has_image_extension(file)]

            if photos == []:
                raise ValueError(ConsoleColored("folder has no photos.", "red", bold=1))

            imgs = [images_paths + "\\" + p for p in photos]
            ImagesArray = [Image.open(img).convert("RGB") for img in imgs]

            print(ConsoleColored("merging photo(s) into pdf...", "yellow", bold=1))

            ImagesArray[0].save(images_paths + f"\\{PDFName}.pdf", save_all=True, append_images=ImagesArray[1:])
            location = images_paths

        # only one image
        elif os.path.isfile(images_paths):
            folder_path = images_paths.split("\\")
            folder_path = "\\".join(folder_path[:len(folder_path) - 1])
            image = Image.open(images_paths).convert("RGB")

            print(ConsoleColored("merging photo(s) into pdf...", "yellow", bold=1))

            image.save(folder_path + f"\\{PDFName}.pdf")
            location = folder_path

    PDFName += ".pdf"
    successfully = ConsoleColored("successfully", "green", bold=1)
    print("pdf with name {} created {}.".format(ConsoleColored(PDFName, "cyan", bold=1, underlined=1), successfully))
    location += "\\" + PDFName

    print("located on: {}".format(ConsoleColored(location, "yellow", bold=1, underlined=1)))
    os.system(location)


def PDFsMerger(pathx: str, pathy: str, dest_folder: str):
    merger = PdfFileMerger()
    merger.append(pathx)
    merger.append(pathy)

    name_pathx = pathx.split("\\")[-1].split(".")[0]
    name_pathy = pathy.split("\\")[-1].split(".")[0]

    merger.write("{}\\{}_{}_merged.pdf".format(dest_folder, name_pathx, name_pathy))
    merger.close()


if __name__ == '__main__':
    # bitcoin_pdf = r"D:\Alexzander__\documents\bitcoin.pdf"
    # text = get_text_from_pdf(bitcoin_pdf)
    # text = "\n\n".join(text.split("\n"))
    # print(text)
    # with open(os.path.dirname(bitcoin_pdf) + "\\bitcoin.pdf.txt", "w+", encoding="utf-8") as f:
    #     f.truncate(0)
    #     f.write(text)
    pass