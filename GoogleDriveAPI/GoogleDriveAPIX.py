
# from python
import requests, json, os

# from project
from GoogleDriveAPI.paths import *

# from workspace
from core.aesthetics import *
from core.system import *
from GoogleDriveAPI.project_imports import *
from core.json__ import *
from core.path__ import *
from core.download import *
__path= "https://www.googleapis.com/auth/drive"

googledriveURL = "https://drive.google.com/drive/u/6/"
googledriveAPI_URL  = "https://www.googleapis.com/drive/v3/files/"

POST_URL = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"

headers = {
    "Authorization": "{} {}".format(tokenTYPE, accessTOKEN)
}

def UploadFilesToDrive(files, parentfolderID=googledrive_folderID):
    if type(files) == list:
        responses = []
        for file in files:
            if not os.path.isfile(file):
                raise ValueError

            file_metadata = {
                "name": get_file_name(file),
                "parents": [parentfolderID]
            }

            content = {
                "data": (
                    "metadata", json.dumps(file_metadata),
                    "application/json; charset=UTF-8"
                ),
                "file": open(file, "rb")
            }

            request = requests.post(
                POST_URL,
                headers=headers,
                files=content
            )
            responses.append(request)

        for file in files:
            fancy_file = "[ {} ]".format(file)
            print_yellow_bold(fancy_file)

        print_yellow_bold("all above files were uploaded to google drive at url:")
        print_yellow_bold("\t" + "{}\n".format(googledriveURL + "folders/{}".format(parentfolderID)), underlined=1)
        return responses

    elif type(files) == str:
        if not os.path.isfile(files):
            raise ValueError

        file_metadata = {
            "name": get_file_name(files),
            "parents": [parentfolderID]
        }

        content = {
            "data": ("metadata", json.dumps(file_metadata), "application/json; charset=UTF-8"),
            "file": open(files, "rb")
        }

        request = requests.post(
            POST_URL,
            headers=headers,
            files=content
        )

        print_yellow_bold("[ {} ]".format(files))
        print_yellow_bold("file was uploaded at url:")
        print_yellow_bold("\t" + "{}\n".format(googledriveURL + "folders/{}".format(parentfolderID)), underlined=1)
        return request.text

def CreateFoldersInDrive(name, total=1, parentfolderID=googledrive_folderID):
    resp = requests.get(googledriveAPI_URL, headers=headers)
    if resp.status_code == 200:
        folder_metadata = {
            "name": name,
            "parents": [parentfolderID],
            "mimeType": "application/vnd.google-apps.folder"
        }

        content = {
            "data": ("metadata", json.dumps(folder_metadata), "application/json; charset=UTF-8")
        }

        request = requests.post(
            POST_URL,
            headers=headers,
            files=content
        )
        print_yellow_bold("folder with name '{}' created.\n".format(name))
    else:
        print_red(resp.text)

def PrintFilesFromDrive():
    response = requests.get(googledriveAPI_URL, headers=headers)
    print("response:\n")
    print(response.text)
    print("\n")
    if response.status_code == 200:
        files = json.loads(response.text)["files"]
        print(ConsoleColored("\nall files from drive:\n", "blue", bold=1, underlined=1))
        for f in files:
            name = f["name"]
            if "." in name:
                file_type = ConsoleColored("file", "green", bold=1)
            else:
                file_type = ConsoleColored("folder", "blue", bold=1)
            line = "\t" + yellow_bold(name) + " [ {} ]".format(file_type)
            print(line)
        print()
    else:
        print(response.text)

def DownloadFileFromDrive(fileID):
    url = googledriveAPI_URL + fileID
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.text)

        responseJSON = json.loads(response.text)
        file_extension = responseJSON["name"].split(".")[1]

        file_index = read_json_from_file(downloadsPATH + "index.json")
        file_index = file_index["index"]

        download_file_from_url(url + "?alt=media", downloadsPATH, headers=headers, name="fromgoogledrive{}".format(file_index), extension=file_extension)

        file_index += 1
        write_json_to_file({"index": file_index}, downloadsPATH + "index.json")

        print_yellow_bold("file downloaded successfully.")
    else:
        print_red_bold(response.text)

def DeleteFileFromDrive(fileID):
    response = requests.delete(googledriveAPI_URL + fileID, headers=headers)
    print(response.text)
    if response.status_code == 200:
        print(ConsoleColored("file deleted successfully.", "blue", bold=1))
    else:
        print_red_bold(response.text, "red")

def CreateFilesJSON():
    response = requests.get(googledriveAPI_URL, headers=headers)
    if response.status_code == 200:
        with open(drivePATH + "GoogleDrive.json", "w+", encoding="utf-8") as file:
            file.truncate(0)
            file.write(response.text)
        print("google drive json written to file successfully.")
    else:
        print_red_bold(response.text, "red")

def EmptyTrash():
    response = requests.delete(googledriveAPI_URL + "trash", headers=headers)
    if response.status_code == 200:
        print(response.text)
        print(response.status_code)
    else:
        print_red_bold(response.text, "red")

if __name__ == "__main__":
    # DownloadFileFromGoogleDrive("1uCbizWq6qJl9i8vSl1BH30W5UeEYkIDf")
    # PrintFilesFromDrive()
    # DeleteFileFromDrive("1lpww9k1RBZqvYdIS-oCAYZeqpMR8solZ")
    # CreateFilesJSON()
    # r = requests.get("https://www.googleapis.com/drive/v3/files/generateIds", headers=headers)
    # print(r.text)
    pass
    # TODO update function
    # "PATCH https://www.googleapis.com/upload/drive/v3/files/fileId"
