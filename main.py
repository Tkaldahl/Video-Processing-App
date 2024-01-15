import json
from flask import Flask, jsonify, request
from playlist_service.get_all_playlists import GetAllPlaylists
from playlist_service.save_playlist import SavePlaylist
from video_service.video_controller import VideoController
from bson import ObjectId


app = Flask(__name__)


@app.route('/process_video', methods=['POST'])
def process_video():
    
    if request.method == 'POST':
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }

        process_video_req = request.get_data().decode('utf-8')
        process_video_req_json = json.loads(process_video_req)
        video_urls = process_video_req_json['video_urls']
        transition_video_url = process_video_req_json['transition_video_url']
        output_path = VideoController().download_and_concatenate(video_urls, transition_video_url)
        return output_path, 200, response_headers


@app.route('/save_playlist', methods=['POST'])
def save_playlist():
    response_headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    save_playlist_req = request.get_data().decode('utf-8')
    save_playlist_req_json = json.loads(save_playlist_req)
    playlist_id = SavePlaylist().main(save_playlist_req_json)

    return {"playlist_id": playlist_id}, 200, response_headers


@app.route('/get_all_playlists', methods=['POST'])
def get_all_playlists():
    response_headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    playlists = GetAllPlaylists().main()
    return playlists, 200, response_headers

if __name__ == '__main__':
    app.run(debug=True)