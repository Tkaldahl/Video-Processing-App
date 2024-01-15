from abc import ABCMeta, abstractmethod
from bson import ObjectId
from pymongo import MongoClient

class MongoService:
    __metaclass__ = ABCMeta

    def __init__(self, host = "mongodb+srv://cluster0.y1ghy8y.mongodb.net/", port = 27017, username = "tkaldahl", password = "R0KNG6LbX93QnO45"):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = None
        self.collection = None
        self.dbName = None
        self.collectionName = None


    def connectToClient(self):
        try:
            self.client = MongoClient(username = self.username, password = self.password, host = self.host, port = self.port)
            print("Connected to MongoDB")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")

    def connectToCollection(self, dbName, collectionName):
        try:
            self.dbName = dbName
            self.collectionName = collectionName
            self.collection = self.client.get_database(dbName).get_collection(collectionName)
            print(f"Connected to collection {dbName}.{collectionName}")
        except Exception as e:
            print(f"Failed to connect to collection {dbName}.{collectionName}: {e}")

    def disconnect(self):
        if self.client:
            self.client.close()
            print("Disconnected from MongoDB")

    @abstractmethod
    def save(self, document):
        if self.collection == None:
            try:
                self.connectToClient()
                self.connectToCollection(self.dbName, self.collectionName)
            except Exception as e:
                print(f"Failed to save to MongoDB: {e}")

        try:
            return self.collection.insert_one(document).inserted_id
        except Exception as e:
            print(f"Failed to save doc to MongoDB: {e}")

    @abstractmethod
    def get(self, query):
        if self.collection == None:
            try:
                self.connectToClient()
                self.connectToCollection(self.dbName, self.collectionName)
            except Exception as e:
                print(f"Failed to delete doc from MongoDB: {e}")
        
        try:
            return list(self.collection.find(query))

        except Exception as e:
            print(f"Failed to get doc from MongoDB: {e}")

    @abstractmethod
    def search(self):
        print("Searching doc in MongoDB")
        # TODO: Implement this method

    @abstractmethod
    def update(self):
        print("Updating doc in MongoDB")
        # TODO: Implement this method

    @abstractmethod
    def deleteById(self, docId):
        if self.collection == None:
            try:
                self.connectToClient()
                self.connectToCollection(self.dbName, self.collectionName)
            except Exception as e:
                print(f"Failed to delete doc from MongoDB: {e}")
        
        try:
            self.client.get_database(self.dbName).get_collection(self.collectionName).delete_one({"_id": ObjectId(docId)})
            print("Successfully deleted {docId} from MongoDB")
        except Exception as e:
            print(f"Failed to delete doc from MongoDB: {e}")


# Test code
if __name__ == "__main__":
    mongo_service = MongoService()
    mongo_service.connectToClient()
    mongo_service.connectToCollection("repo", "playlists")
    # mongo_service.dbName = "repo"
    # mongo_service.collectionName = "playlists"

    test_doc = {
        "name": "Test Playlist",
        "playlist": [
            'https://www.youtube.com/watch?v=Pqbl3gbj_kQ',
            'https://www.youtube.com/watch?v=95L_kFa8Rb4',
            'https://youtu.be/MljSdI-_Lls?si=l520wUc-KHIKXd1o',
            'https://www.youtube.com/watch?v=95L_kFa8Rb4',
            'https://youtu.be/tcAwvku-LEo?si=D_gNq8QRqKkyeTCJ'
        ]
    }

    docId = mongo_service.save(test_doc)
    print(docId)

    newDoc = mongo_service.get({"_id": docId})
    print(newDoc)

    mongo_service.deleteById(docId)
    print("Deleted doc")

