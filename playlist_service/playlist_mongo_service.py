from utilities.mongo_service import MongoService

class PlaylistMongoService:
    mongo_service = MongoService()
    mongo_service.connectToClient()
    mongo_service.connectToCollection("repo", "playlists")

    def get_all_playlists(self):
        get_all_query = {}
        return self.mongo_service.search(get_all_query)
    
    def save(self, playlist):
        return self.mongo_service.save(playlist)

# # Test code
# if __name__ == "__main__":
#     playlist_mongo_service = PlaylistMongoService()
#     playlists = playlist_mongo_service.get_all_playlists()
#     print(playlists)
