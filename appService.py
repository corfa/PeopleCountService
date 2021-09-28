import os

from dotenv import load_dotenv

from Sqlite.initDB import InitRepository
from Sqlite.query_for_service import GetDataForReport, addVideo
from Sqlite.query_for_video import updateStatusVideo
from helper.createResponseReport import createReport
from helper.saveFile import saveFileForForm, saveFileForBinary

from flask import Flask, request
from flask_restx import Resource, Api

# выполнить если нету базы данных
#InitRepository()

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


class BodyVideo(Resource):
    def post(self):
        file = request.data
        if file is None:
            return {"error": "not valid data"}, 400
        try:
            path_file = saveFileForBinary(file)
            id_video = addVideo(path_file, "loaded")
            return {"id": id_video}
        except Exception as e:
            return {"error": str(e)}, 501


class PostVideo(Resource):
    def post(self):
        file = request.files.get("video")
        if file is None:
            return {"error": "not valid data"}, 400
        try:
            path_file = saveFileForForm(file)
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
api.add_resource(BodyVideo, "/processing/body")

if __name__ == '__main__':
    app.run(host="localhost", port=int(os.getenv('PORT', 8000)), debug=True)
