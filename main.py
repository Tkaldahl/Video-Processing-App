import json
from flask import Flask, jsonify, request
from video_service.video_controller import VideoController  # replace with your actual video module

app = Flask(__name__)


@app.route('/process_video', methods=['Get', 'POST', 'OPTIONS'])
def process_video():
    print("hello from process_video")
    if (request.method == 'OPTIONS'):
        print("hello from OPTIONS")
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 200, response_headers
    
    if (request.method == 'GET'):
        print("hello from GET")
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 200, response_headers
    
    if (request.method == 'POST'):
        print("hello from POST")
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }

        # process_video_req = request.get_json()
        process_video_req = request.get_data().decode('utf-8')
        process_video_req_json = json.loads(process_video_req)
        video_urls = process_video_req_json['video_urls']
        transition_video_url = process_video_req_json['transition_video_url']
        output_path = VideoController().download_and_concatenate(video_urls, transition_video_url)
        return output_path, 200, response_headers

if __name__ == '__main__':
    app.run(debug=True)