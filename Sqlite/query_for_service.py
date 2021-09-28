import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()


def addVideo(path_file: str, status: str) -> int:
    uri = os.getenv('PATH_SQLITE', 'repository/db.videos')
    query = """INSERT INTO videos (path_file,status,current_progress,faces_count) VALUES (?,?,0,0)"""
    with sqlite3.connect(uri) as connect:
        row = connect.execute(query, (path_file, status))
        return row.lastrowid


def GetDataForReport() -> list:
    uri = os.getenv('PATH_SQLITE', 'repository/db.videos')
    query = """SELECT id,status,current_progress,faces_count FROM videos"""
    with sqlite3.connect(uri) as connect:
        res = connect.execute(query)
    return res.fetchall()
