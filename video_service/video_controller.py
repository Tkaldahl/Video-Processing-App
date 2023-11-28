import os
import uuid
from youtube_downloader import download_video
from video_concatenator import concatenate_videos
from s3_service import upload_file_obj_to_s3

class VideoController:
    def __init__(self, output_folder='Processed_Videos/'):
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def download_and_concatenate(self, video_urls: list, transition_url):
        downloaded_videos = []
        video_uuid = f"{uuid.uuid4()}"

        transition_video_filename = f"{video_uuid}_transition.webm"
        transition_video_path = os.path.join(self.output_folder, transition_video_filename)
        download_video(transition_url, transition_video_path)
        transition_video = transition_video_path

        # Download videos
        for idx, video_url in enumerate(video_urls):
            video_filename = f"{video_uuid}_source_{idx + 1}.webm"
            video_path = os.path.join(self.output_folder, video_filename)
            download_video(video_url, video_path)
            downloaded_videos.append(video_path)

            # Add the transition between each video. Do not add a transition after the last item.
            if idx == len(video_urls) - 1:
                print(f"{video_url} is the last item.")
            else:
                downloaded_videos.append(transition_video)


        # Concatenate videos
        output_path = os.path.join(self.output_folder, f"{video_uuid}.mp4")
        concatenate_videos(downloaded_videos, output_path)

        print(f"Videos downloaded and concatenated successfully. Output saved to: {output_path}")

        upload_file_obj_to_s3("power-60", output_path, f"processed-videos/{video_uuid}.mp4")
        return output_path

    def _test():
        youtube_video_urls = [
            "https://www.youtube.com/watch?v=Pqbl3gbj_kQ",
            "https://www.youtube.com/watch?v=hYMNFFA7vZE"
        ]

        transition_video_url = "https://www.youtube.com/watch?v=5_jdi3dimas"

        controller = VideoController()

        result = controller.download_and_concatenate(youtube_video_urls, transition_video_url)
        print(result)

if __name__ == "__main__":
    VideoController._test()
