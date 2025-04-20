from LangChain.utils.mongo_client import get_mongo_client

def add_user(user):
    users_collection = get_mongo_client()
    users_collection.insert_one({"user" : user , "history" : ""})