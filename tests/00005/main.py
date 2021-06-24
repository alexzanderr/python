

import os
import ctypes
from string import ascii_uppercase, ascii_lowercase

def GetDriveLetterName(drive_letter: str):
    """
        gets drive name by parsing l
    """
    if not isinstance(drive_letter, str):
        raise TypeError(drive_letter)

    if len(drive_letter) == 1:
        drive_letter = drive_letter.lower()
        if not drive_letter in ascii_lowercase:
            raise ValueError(f"drive letter doesnt contain letters: {drive_letter}")

        drive_letter = f"{drive_letter}:\\"

    elif len(drive_letter) > 1:
        if not os.path.isdir(drive_letter):
            raise NotADirectoryError(drive_letter)


    kernel32 = ctypes.windll.kernel32
    volumeNameBuffer = ctypes.create_unicode_buffer(1024)
    fileSystemNameBuffer = ctypes.create_unicode_buffer(1024)

    result = kernel32.GetVolumeInformationW(
        ctypes.c_wchar_p(drive_letter),
        volumeNameBuffer,
        ctypes.sizeof(volumeNameBuffer),
        fileSystemNameBuffer,
        ctypes.sizeof(fileSystemNameBuffer)
    )

    return volumeNameBuffer.value


r = GetDriveLetterName("D:\\")
print(r)
r = GetDriveLetterName("C:\\")
print(r)
r = GetDriveLetterName("C")
print(r)
r = GetDriveLetterName("C")
print(r)
