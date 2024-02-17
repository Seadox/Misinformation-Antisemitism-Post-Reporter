from scraper.lib.instagram.api import InstagramScraper

if __name__ == '__main__':
    keywords = [
        "QudsNen",
        "antisem",
        "israfront",
        "apartheid",
        "eyeonpal",
        "ICRC",
        "israel"
    ]

    USERNAME = ""# Your Instagram username
    PASSWORD = ""# Your Instagram password
    
    instagram_scraper_client = InstagramScraper.init_client(config={"user_name": USERNAME, "password": PASSWORD})


    if instagram_scraper_client is not None:
        instagram_scraper = InstagramScraper(instagram_scraper_client)
    else:
        instagram_scraper = None
    

    for keyword in keywords:
        posts = []
        reported_posts = []

        if instagram_scraper is not None:
            posts = instagram_scraper.get_text_messages_by_keywords([keyword])

        print(f"posts: {posts}")

    exit(0)
