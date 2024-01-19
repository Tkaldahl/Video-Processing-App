import json
import string
from ..services.playlist_mongo_service import PlaylistMongoService

class SearchPlaylists:
    def __init__(self):
        self.playlist_mongo_service = PlaylistMongoService()

    def main(self, search_playlist_req: json):
        # Create a search query
        search_term = search_playlist_req["search_term"]
        search_query = self.build_search_query(search_term)

        return self.playlist_mongo_service.search_playlists(search_query)

    def build_search_query(self, search_term: string):
        search_query = {
            "$text": {
                "$search": search_term
            }
        }

        return search_query

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