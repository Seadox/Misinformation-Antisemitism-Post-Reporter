from lib.instagram.api import InstagramScraper
import httpx
import asyncio
from instagram_private_api.errors import ClientError
import json


async def test(post):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:8000/scraper", json=post, timeout=None)
        print(response.status_code)


async def get_Top_Hashtags():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/top_hashtags", timeout=None)
        return response.json()

if __name__ == '__main__':
    top_Hashtags = asyncio.run(get_Top_Hashtags())

    KEYWORDS = ['savepalestine', 'palestine', 'freepalestine', 'savegaza',
                'palestina', 'gaza', 'alquds', 'islam', 'savepalestina', 'muslim',
                'freedom', 'savesheikhjarrah', 'gazaunderattack', 'prayforpalestine',
                'westbank', 'ramallah', 'occupation', 'arab']

    print(f"Top {len(top_Hashtags)} Hashtags: {top_Hashtags}")

    USERNAME = ""  # Your Instagram username
    PASSWORD = ""  # Your Instagram password

    instagram_scraper_client = InstagramScraper.init_client(
        config={"user_name": USERNAME, "password": PASSWORD})

    if instagram_scraper_client is not None:
        instagram_scraper = InstagramScraper(instagram_scraper_client)
    else:
        instagram_scraper = None

    posts = []

    for keyword in top_Hashtags:
        if instagram_scraper is not None:
            posts += instagram_scraper.get_text_messages_by_keywords([keyword])

    if len(posts) > 0:
        # print(f"posts: {posts}")
        asyncio.run(test(posts))

    exit(0)
