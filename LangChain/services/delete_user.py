from LangChain.utils.mongo_client import get_mongo_client

def delete_user(user):
    users_collection = get_mongo_client()
    users_collection.delete_one({"user"  : user})
    return