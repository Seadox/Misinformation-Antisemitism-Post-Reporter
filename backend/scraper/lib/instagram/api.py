import re
import traceback
import json
import os

from instagram_private_api import Client
from instagram_private_api.errors import ClientError
from ..instagram.settings import Settings

from ..scraper_abs import ScraperAbs

class InstagramScraper(ScraperAbs):
    __PATH = "backend/scraper/lib/instagram/settings"
    def __init__(self, client, max_messages: int = 100, max_req_delay: int = 3, min_req_delay: int = 1, req_retries: int = 2, source: str = "instagram"):
        super().__init__(client, max_messages, max_req_delay, min_req_delay, req_retries, source)


    @classmethod
    def init_client(self, config: dict = {}):
        username = config.get("user_name")
        password = config.get("password")
        user_settings = config.get("filename", f"{self.__PATH}/{username}_settings.json")

        try:
            if not os.path.isfile(user_settings):
                # settings file does not exist
                print('Unable to find file: {0!s}'.format(user_settings))

                # login new
                api = Client(
                    username, password,
                    on_login=lambda x: Settings.onlogin_callback(x, user_settings))
            else:
                with open(user_settings) as file_data:
                    cached_settings = json.load(file_data, object_hook=Settings.from_json)
                print(f'instagram_scraper -- init_client() -- Reusing settings: {0!s}'.format(user_settings))

                device_id = cached_settings.get('device_id')
                # reuse auth settings
                api = Client(
                    username, password,
                    settings=cached_settings)
            return api
        except ClientError:
            print("%s_scraper -- init_client() -- try different credentials" % "instagram")
            return None
        
    

    def client_logout(self):
        self._client.logout()

    def get_text_messages_by_keywords(self, keywords: list = []) -> list:
        result = []

        try:
            for hash_tag in keywords:
                response = self._client.tag_section(hash_tag)
                print("%s_scraper -- get_text_messages_by_keywords() -- found %s posts for hash_tag \"%s\"" % (self._source, str(len(response["sections"])), str(hash_tag)))

                for post in response["sections"]:
                    video_url = None
                    
                    if post["feed_type"] == "channel":
                        post = post['layout_content']['fill_items']
                    elif post["feed_type"] == 'media':
                        post = post['layout_content']['medias']
                    else:
                        # print("%s -- get_text_messages_by_keywords() -- skipping unsupported media_type" % (self._source, str(len(subreddits))))
                        continue

                    post_data = post[0]['media']
                    caption = post_data['caption']

                    media_type = post_data['media_type']
                    code = post_data['pk']

                    post_text = re.sub(r'[^\x00-\x7F]+', ' ', caption['text'])
                    username = caption['user']['username']

                    if media_type == 2:  # video
                        video_url = post_data['video_versions'][0]['url']
                        media_type = "video"
                    elif media_type == 1:  # image
                        video_url = post_data['image_versions2']['candidates'][0]['url']
                        media_type = "image"
                    elif media_type == 8:  # album
                        media_type = 'album'

                    result.append(
                        self.text_input_obj(
                            username,
                            post_text,
                            str(code),
                            self._source,
                            video_url,
                            str(media_type)
                        )
                    )

            print("%s_scraper -- get_text_messages_by_keywords() found %s posts, in total" % (self._source, str(len(result))))
            
        except Exception as e:
            print("%s_scraper -- get_text_messages_by_keywords() -- unexpected execution -- %s" % (self._source, str(e)))
            traceback.print_exc()
            
        finally:
            self.delay_after_request()
            return result

    