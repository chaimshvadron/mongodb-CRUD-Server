from bson import ObjectId
from mongodb_connection import MongoDBConnection
from soldier import Soldier

class SoldierDAL:
    def __init__(self, collection_name="soldier_details"):
        self.collection_name = collection_name

    def get_all_soldiers(self):
        with MongoDBConnection() as mongo_conn:
            db = mongo_conn.get_db()
            collection = db[self.collection_name]
            soldiers = []
            for doc in collection.find({}):
                soldier = Soldier.from_dict(doc)
                soldiers.append(soldier)
            return soldiers
        
    def create_soldier(self,soldier):
        with MongoDBConnection() as mongo_conn:
            db = mongo_conn.get_db()
            collection = db[self.collection_name]
            sold_doc = collection.insert_one(soldier)
            print(f'Soldier created with ID: {sold_doc.inserted_id}')

    def delete_soldier(self,id):
        with MongoDBConnection() as mongo_conn:
            try:
                db = mongo_conn.get_db()
                collection = db[self.collection_name]
                collection.delete_one({'_id': ObjectId(id)})
                print(f'Soldier ID {id} deleted!')
            except Exception as e:
                print(f"Error deleting soldier ID {id}: {e}")

    def update_soldier_details(self, soldier):
        with MongoDBConnection() as mongo_conn:
            try:
                db = mongo_conn.get_db()
                collection = db[self.collection_name]
                collection.update_one({'_id': ObjectId(soldier['_id'])}, {"$set": soldier.remove('_id', None)})
                print(f'Soldier {soldier['_id']} up to date!')
            except Exception as e:
                print(f"Error updating soldier {soldier['_id']}: {e}")