from playlist_service.utilities.mongo_service import MongoService

class PlaylistMongoService:
    mongo_service = MongoService()
    mongo_service.connectToClient()
    mongo_service.connectToCollection("repo", "playlists")

    def get_all_playlists(self):
        get_all_query = {}
        playlists = self.mongo_service.search(get_all_query)
        
        for playlist in playlists:
            playlist['_id'] = str(playlist['_id'])
        
        return playlists

    
    def save(self, playlist):
        playlist_id = self.mongo_service.save(playlist)
        return str(playlist_id)

# Test code
if __name__ == "__main__":
    playlist_mongo_service = PlaylistMongoService()
    playlists = playlist_mongo_service.get_all_playlists()
    print(playlists)
