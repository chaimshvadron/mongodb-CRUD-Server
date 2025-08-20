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
            collection.insert_one(soldier)
            print('Soldier created!')

    def delete_soldier(self,id):
        with MongoDBConnection() as mongo_conn:
            db = mongo_conn.get_db()
            collection = db[self.collection_name]
            collection.delete_one({'_ID': id})
            print(f'Soldier ID {id} deleted!')

    def update_soldier_details(self, soldier):
        with MongoDBConnection() as mongo_conn:
            db = mongo_conn.get_db()
            collection = db[self.collection_name]
            collection.update_one(soldier)
            print(f'Soldier {soldier['_ID']} up to date!')