import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
from power_60_services.playlist_service.actions.get_all_playlists import GetAllPlaylists
from power_60_services.playlist_service.actions.get_playlist_by_id import GetPlaylistById
from power_60_services.playlist_service.actions.save_playlist import SavePlaylist
from power_60_services.playlist_service.actions.search_playlists import SearchPlaylists
from power_60_services.playlist_service.actions.delete_playlist import DeletePlaylist
from power_60_services.video_service.video_controller import VideoController



app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/process_video", methods=["POST"])
def process_video():
    
    if request.method == "POST":
        response_headers = {
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        }

        process_video_req = request.get_data().decode("utf-8")
        process_video_req_json = json.loads(process_video_req)
        video_urls = process_video_req_json["video_urls"]
        transition_video_url = process_video_req_json["transition_video_url"]
        output_path = VideoController().download_and_concatenate(video_urls, transition_video_url)
        return output_path, 200, response_headers


@app.route("/save_playlist", methods=["POST", "OPTIONS"])
@cross_origin(supports_credentials=True)
def save_playlist():
    response_headers = {
        'Access-Control-Allow-Methods': 'POST,OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    if (request.method == "OPTIONS"):
        return "", 204, response_headers

    save_playlist_req = request.get_data().decode("utf-8")
    save_playlist_req_json = json.loads(save_playlist_req)
    playlist_id = SavePlaylist().main(save_playlist_req_json)

    return {"playlist_id": playlist_id}, 200, response_headers


@app.route("/get_playlist_by_id", methods=["POST"])
def get_playlist_by_id():
    response_headers = {
        "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    get_playlist_by_id_req = request.get_data().decode("utf-8")
    get_playlist_by_id_req_json = json.loads(get_playlist_by_id_req)

    playlist = GetPlaylistById().main(get_playlist_by_id_req_json)
    return {"playlist": playlist}, 200, response_headers


@app.route("/get_all_playlists", methods=["POST"])
def get_all_playlists():
    response_headers = {
        "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    playlists = GetAllPlaylists().main()
    return {"playlists": playlists}, 200, response_headers

@app.route("/search_playlists", methods=["POST"])
def search_playlists():
    response_headers = {
        "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    search_playlist_req = request.get_data().decode("utf-8")
    search_playlist_req_json = json.loads(search_playlist_req)
    playlists = SearchPlaylists().main(search_playlist_req_json)
    return playlists, 200, response_headers

@app.route("/delete_playlist", methods=["POST"])
def delete_playlist():
    response_headers = {
        "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    delete_playlist_req = request.get_data().decode("utf-8")
    delete_playlist_req_json = json.loads(delete_playlist_req)
    DeletePlaylist().main(delete_playlist_req_json)
    return {}, 200, response_headers

if __name__ == "__main__":
    app.run(debug=True)