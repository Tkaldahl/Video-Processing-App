import string
from ...utilities.services.mongo_service import MongoService
from bson.objectid import ObjectId
import uuid

class PlaylistMongoService:
    mongo_service = MongoService()
    mongo_service.connectToClient()
    mongo_service.connectToCollection("repo", "playlists")

    def get_all_playlists(self):
        get_all_query = {}
        playlists = self.mongo_service.search(get_all_query)
        
        return self.clean_mongo_ids(playlists)

    def save(self, playlist):
        if "_id" in playlist and playlist["_id"]:
            if isinstance(playlist["_id"], str):
                playlist["_id"] = ObjectId(playlist["_id"])
            self.mongo_service.update(playlist)
            return str(playlist["_id"])

        playlist_id = uuid.uuid4().hex[:24]
        playlist["_id"] = ObjectId(playlist_id)
        self.mongo_service.save(playlist)
        return playlist_id

    def get_playlist_by_id(self, playlist_id: string):
        playlist = self.mongo_service.search_by_id(playlist_id)
        playlist['_id'] = str(playlist['_id'])
        return playlist
    
    def search_playlists(self, search_query: dict):
        playlists = self.mongo_service.search(search_query)
        return self.clean_mongo_ids(playlists)

    def delete_playlist(self, playlist_id: string):
        playlist_id = self.mongo_service.delete_by_id(playlist_id)
        return str(playlist_id)

    def clean_mongo_ids(self, playlists):
        for playlist in playlists:
            playlist['_id'] = str(playlist['_id'])
        return playlists
    
# Test code
if __name__ == "__main__":
    playlist_mongo_service = PlaylistMongoService()
    playlists = playlist_mongo_service.get_all_playlists()
    print(playlists)
