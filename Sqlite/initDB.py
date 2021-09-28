import sqlite3


def InitRepository():
    uri = 'repository/db.videos'
    query = """CREATE TABLE videos (id INTEGER PRIMARY KEY AUTOINCREMENT,
        path_file TEXT,
        status TEXT,
        current_progress INTEGER,
        faces_count INTEGER)
    """

    with sqlite3.connect(uri) as connect:
        connect.execute(query)
        return "1"
