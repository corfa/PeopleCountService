import os
import threading
import time
from threading import Thread

from dotenv import load_dotenv

from Sqlite.query_for_video import getData
from Video.detectVideo import detectVideo
from helper.checkEnginModel import check_engin_model
from model.VideoModel import VideoModel

load_dotenv()
check_engin_model()
model = VideoModel(os.getenv('PATH_ENGINEMODEL', 'engineModel/yolo.h5'))
number_of_threads = int(os.getenv('number_of_possible_video_streams', 3))
detect = model.getDetect()

while True:
    mass_video = getData()
    if len(mass_video) != 0:
        if threading.active_count() < number_of_threads:
            videoThread = Thread(target=detectVideo, args=(detect, mass_video[0][1], mass_video[0][0]))
            videoThread.start()
            time.sleep(3)
