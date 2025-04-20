from LangChain.utils.mongo_client import get_mongo_client

def get_history(user):
    users_collection = get_mongo_client()
    users = list(users_collection.find({"user"  : user}))
    return users[0]['history'] if users else None