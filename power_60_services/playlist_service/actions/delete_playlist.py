import json
import string
from ..services.playlist_mongo_service import PlaylistMongoService

class DeletePlaylist:
    def __init__(self):
        self.playlist_mongo_service = PlaylistMongoService()

    def main(self, delete_playlist_req: json):
        playlist_id: string = delete_playlist_req["playlist_id"]
        return self.playlist_mongo_service.delete_playlist(playlist_id)

# Test code
if __name__ == "__main__":
    print("DeletePlaylist")