from cv2 import cv2

from Sqlite.query_for_video import GetStatus, updateVideo
from Video.exceptions import StatusCancelException


def finding_percentage(colFrame, done):
    return round(done / colFrame * 100)


def countFrame(pathVideo):
    cap = cv2.VideoCapture(pathVideo)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length


class Video:
    def __init__(self, db_id: int, path: str):
        self.people_count = 0
        self.percent_done = 0
        self.colFrame = countFrame(path)
        self.db_id = db_id

    def useEveryFrame(self, frame_number, output_array, output_count):
        status = GetStatus(self.db_id)
        if status == "cancel":
            raise StatusCancelException
        self.percent_done = finding_percentage(self.colFrame, frame_number)
        self.people_count += output_count['person']
        updateVideo(video_id=self.db_id, percent=self.percent_done, faces_found=self.people_count)
