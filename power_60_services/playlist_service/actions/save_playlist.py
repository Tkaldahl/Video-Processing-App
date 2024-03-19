import json
import string
from ..services.playlist_mongo_service import PlaylistMongoService
from ..models.playlist_doc import YTVideoMetadata

class SavePlaylist:
    def __init__(self):
        self.playlist_mongo_service = PlaylistMongoService()

    def main(self, save_playlist_req: json):
        playlist_id = save_playlist_req["_id"]
        playlist = save_playlist_req["playlist"]
        transition_video = save_playlist_req["transition_video"]
        # playlist = self.insert_transition_video(video_urls, transition_video_url)

        playlist_name = save_playlist_req["playlist_name"]
        return self.save(playlist_id, playlist_name, playlist, transition_video)

    # def insert_transition_video(self, video_urls, transition_video_url):
    #     playlist = []
    #     for video_url in video_urls:
    #         playlist.append(video_url)
    #         playlist.append(transition_video_url)
        
    #     playlist.pop(playlist.__len__() - 1)
    #     return playlist

    def save(self, playlist_id: string, playlist_name: string, playlist: YTVideoMetadata, transition_video: YTVideoMetadata):
        playlistDoc = {
            "_id": playlist_id,
            "name": playlist_name,
            "playlist": playlist,
            "transition_video": transition_video
        }

        return self.playlist_mongo_service.save(playlistDoc)

# Test code
if __name__ == "__main__":
    save_playlist_req = {
        "playlist_name": "Save Playlist Test",
        "transition_video_url": "https://www.youtube.com/watch?v=95L_kFa8Rb4",
        "video_urls": [
            "https://www.youtube.com/watch?v=Pqbl3gbj_kQ",
            "https://youtu.be/MljSdI-_Lls?si=l520wUc-KHIKXd1o",
            "https://youtu.be/tcAwvku-LEo?si=D_gNq8QRqKkyeTCJ"
        ]
    }

    saved_playlist = SavePlaylist().main(save_playlist_req)
    print(saved_playlist)