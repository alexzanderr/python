
import os
from pathlib import Path

main_content_to_backup_path = "main_contents.txt"
main_content_to_backup_file = Path(main_content_to_backup_path)

backup_folder = Path("4backup")
backup_folder.mkdir(exist_ok=True)


def GetMainContents(main_contents=main_content_to_backup_path):
    if isinstance(main_contents, str):
        main_content_to_backup_file = Path(main_contents)
    elif isinstance(main_contents, Path):
        main_content_to_backup_file = Path(main_contents.absolute().as_posix())

    if not main_content_to_backup_file.exists():
        raise FileNotFoundError(main_content_to_backup_file.absolute().as_posix())

    main_content_array = main_content_to_backup_file.read_text().split("\n")

    main_folders_array = []
    main_files_array = []
    for item in main_content_array:
        if os.path.isdir(item):
            main_folders_array.append(item)
        else:
            main_files_array.append(item)

    return main_files_array, main_folders_array