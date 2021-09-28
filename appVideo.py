import os
from threading import Thread

from dotenv import load_dotenv

from Sqlite.query_for_video import getData
from Video.detectVideo import detectVideo
from helper.checkEnginModel import check_engin_model
from model.VideoModel import VideoModel
print("appVideo started!")
load_dotenv()
check_engin_model()
model = VideoModel(os.getenv('PATH_ENGINEMODEL', 'engineModel/yolo.h5'))
detect = model.getDetect()
while True:
    mass_video = getData()
    if len(mass_video) == 1:
        flag = True
        t1 = Thread(target=detectVideo, args=(detect, mass_video[0][1], mass_video[0][0]))
        t1.start()
        t1.join()

    if len(mass_video) >= 2:
        t1 = Thread(target=detectVideo, args=(detect, mass_video[0][1], mass_video[0][0]))
        t2 = Thread(target=detectVideo, args=(detect, mass_video[1][1], mass_video[1][0]))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
