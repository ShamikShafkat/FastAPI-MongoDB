from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from routes.route import router

"""Creating an app object for FastAPI."""
app = FastAPI()

"""create a route to the routes folder"""
app.include_router(router)