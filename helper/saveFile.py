import random

from werkzeug.datastructures import FileStorage


def saveFileForForm(file: FileStorage) -> str:
    try:
        file_name = str(random.randint(0, 100000)) + ".mp4"
        path_file = "repository/videos/" + file_name
        file.save(path_file)
        return path_file
    except:
        saveFileForForm(file)

def saveFileForBinary(file: bytes):
    try:
        file_name = str(random.randint(0, 100000)) + ".mp4"
        path_file = "repository/videos/" + file_name
        f = open(path_file, 'wb')
        f.write(file)
        f.close()
        return path_file
    except:
        saveFileForBinary(file)
