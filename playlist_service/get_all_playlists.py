from playlist_mongo_service import PlaylistMongoService

class GetAllPlaylists:
    def __init__(self):
        self.playlist_mongo_service = PlaylistMongoService()

    def main(self):
        playlists = self.playlist_mongo_service.get_all_playlists()
        return playlists

# # Test code
# if __name__ == "__main__":
#     playlists = GetAllPlaylists().main()
#     print(playlists)
