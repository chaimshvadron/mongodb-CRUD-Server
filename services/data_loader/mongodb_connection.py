from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, host='mongodb', port=27017, db_name='enemy_soldiers', username=None, password=None):
        import os
        self.host = host
        self.port = port
        self.db_name = db_name
        self.username = username or os.getenv('MONGO_INITDB_ROOT_USERNAME')
        self.password = password or os.getenv('MONGO_INITDB_ROOT_PASSWORD')
        self.client = None
        self.db = None

    def __enter__(self):
        try:
            if self.username and self.password:
                self.client = MongoClient(
                    host=self.host,
                    port=self.port,
                    username=self.username,
                    password=self.password,
                    authSource='admin'
                )
            else:
                self.client = MongoClient(self.host, self.port)
            self.db = self.client[self.db_name]
            print(f"Connected to MongoDB at {self.host}:{self.port}, database: {self.db_name}")
            return self
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")

    def get_db(self):
        return self.db
