import motor.motor_asyncio

"""URI for connecting to mongodb. Here this <password> part has to be your cluster password."""
uri = "mongodb+srv://shamikshafkat:t14xRE7ds56vrCZ8@cluster0.ebfq3pw.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = motor.motor_asyncio.AsyncIOMotorClient(uri)

# name of the database in cluster
db = client.todo_db

# name of the collection/table in the database
collection_name = db["todo_collection"]