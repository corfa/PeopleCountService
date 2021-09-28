from imageai.Detection import VideoObjectDetection


class VideoModel:
    def __init__(self,path_model):
        self.video_detector = VideoObjectDetection()
        self.video_detector.setModelTypeAsYOLOv3()
        self.video_detector.setModelPath(path_model)
        self.video_detector.loadModel()

    def getDetect(self):
        return self.video_detector
