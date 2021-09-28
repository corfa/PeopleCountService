import random

from werkzeug.datastructures import FileStorage


def saveFile(file: FileStorage) -> str:
    try:
        file_name = str(random.randint(0, 100000)) + ".mp4"
        path_file = "repository/videos/" + file_name
        file.save(path_file)
        return path_file
    except:
        saveFile(file)
