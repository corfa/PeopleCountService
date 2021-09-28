import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()


def getData() -> list:
    uri = os.getenv('PATH_SQLITE', 'repository/db.videos')
    query = """SELECT id,path_file FROM videos WHERE status='loaded'"""
    with sqlite3.connect(uri) as connect:
        res = connect.execute(query)
    return res.fetchall()


def updateStatusVideo(status: str, video_id: int):
    uri = os.getenv('PATH_SQLITE', 'repository/db.videos')
    query = """UPDATE videos SET status=? WHERE id=?"""
    with sqlite3.connect(uri) as connect:
        connect.execute(query, (status, video_id))


def updateVideo(video_id: int, percent: int, faces_found: int):
    uri = os.getenv('PATH_SQLITE', 'repository/db.videos')
    query = """UPDATE videos SET current_progress=?,faces_count=? WHERE id=?"""
    with sqlite3.connect(uri) as connect:
        connect.execute(query, (percent, faces_found, video_id))


def GetStatus(id_video: int) -> str:
    uri = os.getenv('PATH_SQLITE', 'repository/db.videos')
    query = """SELECT status FROM videos WHERE id=?"""
    with sqlite3.connect(uri) as connect:
        return connect.execute(query, (id_video,)).fetchone()[0]
