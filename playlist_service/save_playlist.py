import json
from playlist_mongo_service import PlaylistMongoService

class SavePlaylist:
    def __init__(self):
        self.playlist_mongo_service = PlaylistMongoService()

    def main(self, save_playlist_req: json):
        video_urls = save_playlist_req['video_urls']
        transition_video_url = save_playlist_req['transition_video_url']

        # Save the playlist as an array of strings
        playlist = self.insert_transition_video(video_urls, transition_video_url)
        return self.save(playlist)

    def insert_transition_video(self, video_urls, transition_video_url):
        playlist = []
        for video_url in video_urls:
            playlist.append(video_url)
            playlist.append(transition_video_url)
        
        playlist.pop(playlist.__len__() - 1)
        return playlist

    def save(self, playlist):
        playlistDoc = {
            "name": "Test Playlist",
            "playlist": playlist
        }

        return self.playlist_mongo_service.save(playlistDoc)

# Test code
if __name__ == "__main__":
    save_playlist_req = {
        "transition_video_url": "https://www.youtube.com/watch?v=95L_kFa8Rb4",
        "video_urls": [
            'https://www.youtube.com/watch?v=Pqbl3gbj_kQ',
            'https://youtu.be/MljSdI-_Lls?si=l520wUc-KHIKXd1o',
            'https://youtu.be/tcAwvku-LEo?si=D_gNq8QRqKkyeTCJ'
        ]
    }

    saved_playlist = SavePlaylist().main(save_playlist_req)
    print(saved_playlist)