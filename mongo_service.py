from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")
db = client["Facebook_scrapper"]
collection = db["posts"]


def insert_post(post):
    return collection.insert_one(post)

def insert_posts(posts):
    return collection.insert_many(posts)

def find_posts(page_name = None):
    if page_name is None : 
        return list(collection.find())
    return list(collection.find({'username' : page_name}))
