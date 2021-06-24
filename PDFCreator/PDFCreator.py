
import os
import sys
from PIL import Image
from core.development import *
from core.system import *

def HasImageExtension(filename):
    ext = filename.split(".")[1]
    image_extensions = ["jpg", "jpeg", "png", "JPG", "JPEG", "PNG"]
    if ext in image_extensions:
        return True
    return False

def PythonPrintToPDF(images_paths, PDFName):
    print("PythonPrintToPDF: processing...")

    if type(images_paths) == list:
        folder_path = images_paths[0].split("\\")
        folder_path = "\\".join(folder_path[:len(folder_path) - 1])
        ImagesArray = [Image.open(img).convert("RGB") for img in images_paths]

        print("merging photo(s) into pdf...")

        ImagesArray[0].save(folder_path + f"\\{PDFName}.pdf", save_all=True, append_images=ImagesArray[1:])
        location = folder_path

    elif type(images_paths) == str:
        if os.path.isdir(images_paths):
            pdf_path = images_paths + "\\{}.pdf".format(PDFName)

            if os.path.isfile(pdf_path):
                print("warning: pdf already existent.")
                os.remove(pdf_path)
                print("Existent pdf was deleted.")

            del pdf_path

            photos = [file for file in os.listdir(images_paths) if os.path.isfile(images_paths + "\\" + file) and HasImageExtension(file)]

            if photos == []:
                raise ValueError("folder has no photos.")

            imgs = [images_paths + "\\" + p for p in photos]
            ImagesArray = [Image.open(img).convert("RGB") for img in imgs]

            print("merging photo(s) into pdf...")

            ImagesArray[0].save(images_paths + f"\\{PDFName}.pdf", save_all=True, append_images=ImagesArray[1:])
            location = images_paths

        elif os.path.isfile(images_paths):
            folder_path = images_paths.split("\\")
            folder_path = "\\".join(folder_path[:len(folder_path) - 1])
            image = Image.open(images_paths).convert("RGB")

            print("merging photo(s) into pdf...")

            image.save(folder_path + f"\\{PDFName}.pdf")
            location = folder_path

    PDFName += ".pdf"
    print("pdf with name {} created successfully.".format(PDFName))
    location += "\\" + PDFName

    print("located on: {}".format(location))
    os.system(location)

def app():
    script_arguments = sys.argv
    if len(script_arguments) >= 2:
        print(script_arguments)
        images_path = script_arguments[1]

        pdf_name = "pdf-of-this-folder"
        if len(script_arguments) == 3:
            pdf_name = script_arguments[2]
            if ".pdf" in pdf_name:
                raise ValueError("pdf_name should not have extension, just name please.")

        PythonPrintToPDF(images_path, pdf_name)
    else:
        while 1:
            clearscreen()
            IntroductionMessage("PDFCreator application\ninsert path of images to convert to pdf")

            user_input = input("enter the path of the images to create pdf:\n>>> ")
            if user_input == "exit":
                break
            elif user_input == "":
                continue

            pdf_name = input("enter the name of the pdf:\n>>> ")
            try:
                PythonPrintToPDF(user_input, pdf_name)
                break
            except Exception as error:
                print(error)

if __name__ == "__main__":
    app()