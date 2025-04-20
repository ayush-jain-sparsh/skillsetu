from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

def get_mongo_client():
    """
    Create a MongoDB client using the connection string from environment variables.
    """

    load_dotenv()
    uri = os.getenv("DB_URI")
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["History"]
    users_collection = db["ChatBot"]
    return users_collection
