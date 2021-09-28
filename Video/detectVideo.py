from imageai.Detection import VideoObjectDetection

from Sqlite.query_for_video import updateStatusVideo
from Video.Video import Video


def detectVideo(detector: VideoObjectDetection, path: str, id_video):
    updateStatusVideo("during",id_video)
    video = Video(id_video, path)
    detector.detectObjectsFromVideo(input_file_path=path,
                                    save_detected_video=False,
                                    per_frame_function=video.useEveryFrame, frames_per_second=1,
                                    minimum_percentage_probability=30)
