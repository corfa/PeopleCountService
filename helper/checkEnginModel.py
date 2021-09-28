import os

import requests


def check_engin_model():
    if os.path.exists('engineModel/yolo.h5') is False:
        url = "https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5/"
        r = requests.get(url)
        print("start download engine")
        with open("engineModel/yolo.h5", "wb") as code:
            code.write(r.content)