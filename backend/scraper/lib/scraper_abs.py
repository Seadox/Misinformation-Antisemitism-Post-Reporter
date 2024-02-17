from random import randint
from time import sleep

class ScraperAbs():
    def __init__(self, client, max_messages: int, max_req_delay: int, min_req_delay: int, req_retries: int, source: str):
        self._client = client
        self._max_messages = max_messages
        self._max_req_delay = max_req_delay
        self._min_req_delay = min_req_delay
        self._req_retries = req_retries
        self._source = source

    @classmethod
    def init_client(self, config: dict = {}):
        pass
        
    @classmethod
    def text_message_valid(cls, msg) -> bool:
        pass
    
    @classmethod
    def text_input_field_valid(cls, val: str) -> bool:
        return val is not None and len(val) > 0

    @classmethod
    def text_input_obj(cls, author: str, post_text: str, post_id: str, source: str, extra_data_link: str = None, media_type: str = None):
        result = {
            "post_author": author if cls.text_input_field_valid(author) else "unknown",
            "post_text": post_text if cls.text_input_field_valid(post_text) else "unknown",
            "post_id": post_id if cls.text_input_field_valid(post_id) else "unknown",
            "source": source if cls.text_input_field_valid(source) else "unknown"
        }

        if extra_data_link is not None:
            result["extra_data_link"] = extra_data_link if cls.text_input_field_valid(extra_data_link) else "unknown"

        if media_type is not None:
            result["media_type"] = media_type if cls.text_input_field_valid(media_type) else "unknown"

        return result

    def delay_after_request(self) -> None:
        sleep(randint(self._min_req_delay, self._max_req_delay))
    
    def get_text_messages(self, params: dict = {}) -> list:
        pass

    async def get_text_messages_async(self, output: list = [], params: dict = {}) -> None:
        pass

    def get_text_messages_by_keywords(self, keywords: list = []) -> list:
        pass