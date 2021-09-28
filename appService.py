import os

from cv2 import FileStorage
from dotenv import load_dotenv
from werkzeug.datastructures import ImmutableMultiDict
from Sqlite.initDB import InitRepository
from Sqlite.query_for_service import GetDataForReport, addVideo
from Sqlite.query_for_video import updateStatusVideo
from helper.createResponseReport import createReport
from helper.saveFile import saveFile

from flask import Flask, request
from flask_restx import Resource, Api

# выполнить если нету базы данных
#InitRepository()

print("appService started!")
app = Flask(__name__)
api = Api(app)
load_dotenv()

class GetVideo(Resource):
    def get(self):
        try:
            mass = GetDataForReport()
            json_videos = createReport(mass)
            return {"videos": json_videos}
        except Exception as e:
            return {"error": str(e)}, 501

#it is test endpoint
class TestPost(Resource):
    def post(self):
        print("done!!!!")
        file = request.data
        f = open('myVideo.mp4', 'wb')
        f.write(file)
        f.close()
        print(type(file))
#it is test endpoint

class PostVideo(Resource):
    def post(self):
        file = request.files.get("")
        if file is None:
            return {"error": "not valid data"}, 400
        try:
            path_file = saveFile(file)
            id_video = addVideo(path_file, "loaded")
            return {"id": id_video}
        except Exception as e:
            return {"error": str(e)}, 501


class CancelVideo(Resource):
    def post(self, video_id):
        try:
            updateStatusVideo("cancel", int(video_id))
            return {}, 200
        except Exception as e:
            return {"error": str(e)}


api.add_resource(CancelVideo, "/processing/video/<int:video_id>/cancel")
api.add_resource(GetVideo, "/processing/video/")
api.add_resource(PostVideo, "/processing/video")
#test
api.add_resource(TestPost, "/processing/test")
#test
if __name__ == '__main__':
    app.run(host="localhost", port=int(os.getenv('PORT', 8000)), debug=True)
