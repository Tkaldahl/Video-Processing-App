from flask import Flask, jsonify, request
from video_service.video_controller import VideoController  # replace with your actual video module

app = Flask(__name__)


@app.route('/process_video', methods=['POST'])
def process_video():
    # Call your video processing function here
    process_video_req = request.get_json()
    video_urls = process_video_req.get('video_urls')
    transition_video_url = process_video_req.get('transition_video_url')
    output_path = VideoController().download_and_concatenate(video_urls, transition_video_url)
    return jsonify({'output_path': output_path})

if __name__ == '__main__':
    app.run(debug=True)