from fastapi import FastAPI
from facebook_scraper import get_posts
from mongo_service import *

app = FastAPI()


@app.get("/scrap/{page_name}")
async def scrap(page_name):
    posts = []
    try:
        posts = list(get_posts(page_name, pages=1))
        posts = [ delete_none(post) for post in posts ]
        insert_posts(posts)
    except :
        pass
    return posts

@app.get("/read")
async def find_all_pages():
    return find_posts()

@app.get("/read/{page_name}")
async def find_pages(page_name):
    return find_posts(page_name)

@app.get("/scrap/{page_name}/{pages_count}")
async def scrap_pages(page_name, pages_count):
    return list(get_posts(page_name, pages=int(pages_count)))


def delete_none(d):
    new_dict = dict()
    for k, v in d.items():
        if v:
            new_dict[k] = v
    new_dict['_id'] = new_dict['post_id']
    return new_dict