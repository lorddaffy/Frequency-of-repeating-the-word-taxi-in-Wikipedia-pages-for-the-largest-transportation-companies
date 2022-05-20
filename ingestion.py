import requests
from bs4 import BeautifulSoup
from arangoclient import client
import re

# insert the content of the url in postgres
def _insert_db(wiki_link, content):
    inserted = False
    try:
        db = client.db("free-now", username="root", password="1234")

        if not db.has_collection("article"):
            db.create_collection("article")

        article_col = db.collection("article")
        key= re.sub(r'[^\w]', '', wiki_link)
        new_article = {"url": wiki_link, "content": content, "_key": key}
        article_col.insert(new_article)
        inserted = True    
    except Exception as e:
        print(e)
    finally:
        return inserted           

# get the wiki page then transform from html to string to store  content in db
def _get_article(wiki_link):
    response = requests.get(url=wiki_link)
    soup = BeautifulSoup(response.content, 'html.parser').encode("utf-8")
    soup_str=str(soup)
    return soup_str

def ingest_new_article(wiki_link):
    soup_str = _get_article(wiki_link)
    return _insert_db(wiki_link, soup_str)

