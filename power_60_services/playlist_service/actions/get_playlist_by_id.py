import json
from ..services.playlist_mongo_service import PlaylistMongoService

class GetPlaylistById:
    def __init__(self):
        self.playlist_mongo_service = PlaylistMongoService()

    def main(self, get_playlist_by_id_req: json):
        playlist_id = get_playlist_by_id_req["playlist_id"]

        playlist = self.playlist_mongo_service.get_playlist_by_id(playlist_id)
        return playlist

# # Test code
# if __name__ == "__main__":
#     get_playlist_by_id_req = {
#         "playlist_id": "5f5e7c0f6a4d7d5b7f5b0b2e"
#     }

#     playlists = GetPlaylistById().main(get_playlist_by_id_req)
#     print(playlists)
