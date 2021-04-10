from pathlib import Path
import os

SUBDIRECTORIES = {"DOCUMENTS": ['.pdf', '.rtf', '.txt'],
                  "AUDIO": ['.m4a', '.m4b', '.mp3'],
                  "VIDEOS": ['.mov', '.avi', '.mp4'],
                  "IMAGES": ['.jpg', '.jpeg', '.png']}


def pick_directory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'


# print(pick_directory('.pdf'))


def organize_directory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        # print(filePath)
        filetype = filePath.suffix.lower()
        # print(filetype)
        directory = pick_directory(filetype)
        directoryPath = Path(directory)
        if not directoryPath.is_dir():
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))


organize_directory()
