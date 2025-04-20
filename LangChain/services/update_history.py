from LangChain.utils.mongo_client import get_mongo_client

def update_history(user , history):
    users_collection = get_mongo_client()
    users_collection.update_one({"user"  : user} ,  {"$set": {"history": history}})