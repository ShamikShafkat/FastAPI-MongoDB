from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

"""URI for connecting to mongodb. Here this <password> part has to be your cluster password."""
uri = "mongodb+srv://shamikshafkat:t14xRE7ds56vrCZ8@cluster0.ebfq3pw.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# name of the database in cluster
db = client.todo_db

# name of the collection/table in the database
collection_name = db["todo_collection"]